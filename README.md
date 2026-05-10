# 📊 Análisis de campañas de marketing
------------------------------


Un análisis de una campaña de marketing y sus diferentes canales de transmisión, así como de las ventas totales y los nuevos usuarios, para lograr una mayor eficiencia a la hora de invertir en publicidad.


# 🔍 La Campaña


En este proyecto, nuestro cliente, una tienda online, llevó a cabo una campaña de marketing multicanal de una semana de duración, diseñada para evaluar la efectividad de los mensajes y la respuesta de los clientes ante una gama de productos destacados.

La campaña incluyó dos versiones de los mensajes:

## La campaña A utilizó un tono informal y conversacional:

<img width="1277" height="715" alt="Campaign A" src="https://github.com/user-attachments/assets/ac2e7133-9e7c-4cda-b280-14b613945386" />

## La campaña B utilizó un tono más promocional y orientado a las ventas:

<img width="1277" height="679" alt="Campaign B" src="https://github.com/user-attachments/assets/d020f971-bafd-4c8b-a545-27890394d643" />

El cliente utilizó tres canales de marketing:

Correo electrónico

Instagram

Banner en el sitio web


## Lo que el cliente quiere saber:

“¿En qué combinación de campaña y canal deberíamos centrarnos para aumentar las ventas a nuevos clientes, y por qué?”


# 🛠️ Los Datos

El archivo Marketing_Campaign_Data.csv contiene registros de las interacciones de marketing de la campaña semanal; estos registros se utilizarán para analizar la efectividad de las diferentes campañas y canales.

A continuación, se presenta un desglose detallado de la estructura y el contenido del conjunto de datos:


## Resumen de las columnas

El conjunto de datos consta de 7 columnas:

ID de interacción: Un identificador único para cada interacción con el cliente.

Tipo de campaña: Variable categórica con dos grupos, que probablemente representa una prueba A/B.

Canal: La plataforma de marketing utilizada para la interacción.

Tipo de cliente: Clasificación del cliente.

Convertido (1=sí, 0=no): Un indicador binario que indica si la interacción generó una conversión.

Tiempo en el sitio (segundos): La duración que el usuario permaneció en el sitio.

Ventas ($): Los ingresos generados por la interacción.


# 🔍 Análisis y panel de control

El análisis se realizó con bibliotecas de Python utilizando Jupyter Notebooks.

<img width="1338" height="847" alt="Marketing 1" src="https://github.com/user-attachments/assets/8acda37d-6d3c-4e71-bb5d-09fed4a42df1" />

# 🚀 Resultados y recomendaciones

El análisis realizado sobre las campañas de marketing A y B y sus diferentes canales de transmisión, con el objetivo de determinar la mejor opción para invertir en publicidad, concluyó que la campaña B por correo electrónico es la mejor opción para atraer nuevos usuarios, seguida de la campaña A por correo electrónico, la campaña B por Instagram y la campaña B mediante banner web.

El análisis reveló ventas totales de nuevos usuarios por un total de $988,529 y un total de 42,597 nuevos usuarios con una tasa de compra del 47.86%.

La campaña B por correo electrónico adquirió 9,700 nuevos usuarios y generó ventas por $225,285.52, convirtiéndose en la campaña más efectiva en términos de adquisición de nuevos usuarios y conversión de ventas.

Esto podría deberse a la comunicación más formal y personalizada que ofrece el correo electrónico, y al tono más sobrio y corporativo de la campaña B. Esto genera confianza en los consumidores y una sensación de estatus y exclusividad, animándolos a visitar el sitio web y realizar compras.

<img width="2400" height="1400" alt="customer_revenue" src="https://github.com/user-attachments/assets/6ed89bc0-d3f0-4b4b-bd24-501a17be062e" />
<img width="2400" height="1400" alt="revenue_by_channel_campaign" src="https://github.com/user-attachments/assets/9de0f7fd-5516-4cdc-9341-506ced634f75" />
