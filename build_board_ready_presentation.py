from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from pptx import Presentation
from pptx.util import Inches, Pt


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "Marketing_Campaign_Data.csv"
OUTPUT_DIR = BASE_DIR / "deliverables"
CHART_DIR = OUTPUT_DIR / "charts"
OUTPUT_PPT = OUTPUT_DIR / "Marketing_Campaign_Executive_Presentation_Board_Ready.pptx"
SCENARIO_CHART = CHART_DIR / "escenarios_impacto_ingresos.png"


def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_FILE)
    return df.rename(
        columns={
            "Interaction ID": "interaction_id",
            "Campaign Type": "campaign",
            "Channel": "channel",
            "Customer Type": "customer_type",
            "Converted (1=yes, 0=no)": "converted",
            "Time on Site (seconds)": "time_on_site",
            "Sales ($)": "sales",
        }
    )


def compute_metrics(df: pd.DataFrame) -> dict:
    combo = (
        df.groupby(["campaign", "channel"], as_index=False)
        .agg(
            interactions=("interaction_id", "count"),
            conversions=("converted", "sum"),
            conversion_rate=("converted", "mean"),
            revenue=("sales", "sum"),
        )
        .sort_values("revenue", ascending=False)
    )

    top_combo = combo.iloc[0]
    top_new_combo = (
        df[df["customer_type"] == "New"]
        .groupby(["campaign", "channel"], as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
        .iloc[0]
    )

    avg_ticket = df.loc[df["converted"] == 1, "sales"].mean()
    total_revenue = df["sales"].sum()
    conversion_rate = df["converted"].mean()

    baseline_interactions = float(top_combo["interactions"])
    baseline_cr = float(top_combo["conversion_rate"])
    baseline_revenue = float(top_combo["revenue"])

    scenarios = [
        ("Conservador", 0.05, 0.0020),
        ("Base", 0.10, 0.0050),
        ("Agresivo", 0.15, 0.0100),
    ]

    rows = []
    for name, traffic_uplift, cr_pp in scenarios:
        new_interactions = baseline_interactions * (1 + traffic_uplift)
        new_cr = min(baseline_cr + cr_pp, 0.95)
        est_revenue = new_interactions * new_cr * avg_ticket
        incremental = est_revenue - baseline_revenue
        rows.append(
            {
                "escenario": name,
                "trafico_uplift": traffic_uplift,
                "cr_uplift_pp": cr_pp,
                "ingreso_estimado": est_revenue,
                "ingreso_incremental": incremental,
            }
        )

    scenarios_df = pd.DataFrame(rows)

    return {
        "total_revenue": total_revenue,
        "overall_cr": conversion_rate,
        "avg_ticket": avg_ticket,
        "top_combo": top_combo,
        "top_new_combo": top_new_combo,
        "scenarios": scenarios_df,
    }


def build_scenario_chart(scenarios_df: pd.DataFrame) -> Path:
    CHART_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 4.8))
    plt.bar(scenarios_df["escenario"], scenarios_df["ingreso_incremental"], color=["#90be6d", "#f8961e", "#f94144"])
    plt.title("Impacto estimado de ingresos por escenario")
    plt.ylabel("Ingreso incremental estimado ($)")

    for idx, value in enumerate(scenarios_df["ingreso_incremental"]):
        plt.text(idx, value, f"${value:,.0f}", ha="center", va="bottom", fontsize=9)

    plt.tight_layout()
    plt.savefig(SCENARIO_CHART, dpi=240)
    plt.close()
    return SCENARIO_CHART


def add_bullets(slide, title: str, bullets: list[str]) -> None:
    slide.shapes.title.text = title
    body = slide.shapes.placeholders[1].text_frame
    body.clear()
    body.text = bullets[0]
    body.paragraphs[0].font.size = Pt(22)
    for line in bullets[1:]:
        p = body.add_paragraph()
        p.text = line
        p.level = 0
        p.font.size = Pt(18)


def create_presentation(metrics: dict, chart_path: Path) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    prs = Presentation()

    top_combo = metrics["top_combo"]
    top_new = metrics["top_new_combo"]
    scenarios_df = metrics["scenarios"]

    # 1) Portada
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = "Plan Ejecutivo de Crecimiento de Marketing"
    slide.placeholders[1].text = "Comite de Direccion | Campanas A/B y canales de difusion"

    # 2) Snapshot ejecutivo
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    add_bullets(
        slide,
        "Snapshot Ejecutivo (situacion actual)",
        [
            f"Ingresos totales actuales: ${metrics['total_revenue']:,.2f}",
            f"Conversion global: {metrics['overall_cr'] * 100:.2f}%",
            f"Ticket promedio por conversion: ${metrics['avg_ticket']:.2f}",
            f"Combinacion lider actual: {top_combo['campaign']} + {top_combo['channel']} (${top_combo['revenue']:,.0f})",
            f"Mejor palanca de nuevos clientes: {top_new['campaign']} + {top_new['channel']} (${top_new['sales']:,.0f})",
        ],
    )

    # 3) Decision ejecutiva
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    add_bullets(
        slide,
        "Decision solicitada hoy",
        [
            "Aprobar piloto de 4 semanas con reasignacion de presupuesto hacia B + Email.",
            "Objetivo: aumentar ingresos sin deteriorar conversion ni ticket promedio.",
            "Alcance: creatividad, landing page y segmentacion por cliente nuevo/existente.",
            "Gobernanza: revision semanal con reglas de corte por KPI.",
        ],
    )

    # 4) Impacto economico esperado
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = "Impacto economico esperado"
    slide.shapes.add_picture(str(chart_path), Inches(0.7), Inches(1.2), width=Inches(7.0))

    left = Inches(8.0)
    top = Inches(1.3)
    width = Inches(4.8)
    height = Inches(4.6)
    textbox = slide.shapes.add_textbox(left, top, width, height)
    tf = textbox.text_frame
    tf.text = "Escenarios de uplift (sobre combinacion lider)"
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.size = Pt(15)

    for _, r in scenarios_df.iterrows():
        p = tf.add_paragraph()
        p.text = f"{r['escenario']}: +${r['ingreso_incremental']:,.0f}"
        p.font.size = Pt(14)

    # 5) Plan 30-60-90
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    add_bullets(
        slide,
        "Plan 30-60-90 dias",
        [
            "0-30: activar piloto, definir baseline y tablero de seguimiento.",
            "31-60: ejecutar pruebas A/B por canal (mensaje, CTA, landing).",
            "61-90: escalar ganadores y formalizar regla de rebalanceo de presupuesto.",
            "Responsables sugeridos: Marketing Performance, BI y Ventas.",
        ],
    )

    # 6) Riesgos y mitigaciones
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    add_bullets(
        slide,
        "Riesgos clave y mitigaciones",
        [
            "Riesgo: fatiga de audiencia en canal lider.",
            "Mitigacion: rotacion creativa semanal y frecuencia maxima por segmento.",
            "Riesgo: mejora de volumen con menor calidad.",
            "Mitigacion: umbrales minimos de conversion y ticket antes de escalar.",
            "Riesgo: sesgo por estacionalidad.",
            "Mitigacion: comparar contra control historico de 4 semanas previas.",
        ],
    )

    # 7) KPI tree / gobernanza
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    add_bullets(
        slide,
        "Gobernanza semanal de KPIs",
        [
            "KPIs primarios: Ingresos, Conversion.",
            "KPIs secundarios: Ticket promedio, Share de nuevos, Tiempo en sitio.",
            "Regla de accion: pausar tacticas con -10% de conversion vs baseline por 2 semanas.",
            "Comite semanal: validar resultados y reasignar presupuesto por evidencia.",
        ],
    )

    # 8) Cierre / next step
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    add_bullets(
        slide,
        "Siguiente paso para aprobacion",
        [
            "Aprobacion requerida hoy: piloto de 4 semanas y presupuesto asociado.",
            "Fecha de checkpoint ejecutivo: semana 2.",
            "Criterio de exito: uplift positivo de ingresos con conversion estable o mejor.",
            "Entregable final: plan de escalamiento trimestral basado en resultados.",
        ],
    )

    prs.save(OUTPUT_PPT)
    return OUTPUT_PPT


def main() -> None:
    df = load_data()
    metrics = compute_metrics(df)
    chart_path = build_scenario_chart(metrics["scenarios"])
    ppt_path = create_presentation(metrics, chart_path)
    print(f"Generated board-ready presentation: {ppt_path}")


if __name__ == "__main__":
    main()
