# Marketing Campaign Analysis

## Objective
Identify the best campaign and transmission channel to invest in using a one-week test where every campaign-channel cell received the same ad spend.
Campaign A uses a casual tone. Campaign B uses a sales-oriented tone.

## Executive Recommendation
Invest in **Campaign B + Email**.

Under the equal-spend test assumption, B + Email delivered the highest weekly return in the entire dataset: $533,036.65 from 23,065 interactions, with a 47.77% conversion rate and $23.11 sales per interaction.
It also ranks first among new customers at $225,285.52, so the same investment choice works for both total revenue and acquisition growth.

## EDA Summary
- Rows: 100,000
- Columns: 7
- Missing values: 0
- Duplicate interaction IDs: 0
- Total observed sales: $2,314,742.53
- New-customer share of interactions: 42.60%
- Average time on site: 134.57 seconds

### Customer Mix
| Customer Type | Interactions | Conversion Rate | Total Sales | Sales / Lead | Avg. Time on Site |
| --- | --- | --- | --- | --- | --- |
| Existing | 57,403 | 47.59% | $1,326,214.03 | $23.10 | 134.42 |
| New | 42,597 | 47.86% | $988,528.51 | $23.21 | 134.76 |

Email is the top revenue channel overall at $947,748.87, and it remains the top revenue channel among new customers at $402,652.49.
Instagram is the most efficient new-customer channel on a revenue-per-interaction basis at $23.46, but it does not match Email on scale.

## Overall Performance Ranking
Because every cell had the same investment during the one-week test, total sales is the primary decision metric. Sales per lead and conversion rate are secondary tie-breakers.

| Rank | Campaign | Tone | Channel | Interactions | Conversion | Total Sales | Sales / Lead | Revenue Share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B | Sales-oriented tone | Email | 23,065 | 47.77% | $533,036.65 | $23.11 | 23.03% |
| 2 | A | Casual tone | Email | 18,071 | 47.11% | $414,712.22 | $22.95 | 17.92% |
| 3 | B | Sales-oriented tone | Web Banner | 16,694 | 47.55% | $385,345.70 | $23.08 | 16.65% |
| 4 | B | Sales-oriented tone | Instagram | 16,459 | 47.76% | $382,487.78 | $23.24 | 16.52% |
| 5 | A | Casual tone | Instagram | 12,880 | 48.68% | $302,735.29 | $23.50 | 13.08% |
| 6 | A | Casual tone | Web Banner | 12,831 | 47.60% | $296,424.89 | $23.10 | 12.81% |

The revenue gap between the top option and the runner-up is $118,324.43. The runner-up is A + Email, which is slightly more efficient per interaction but materially smaller in weekly sales.

## New-Customer Confirmation
The acquisition view points to the same answer, which reduces execution risk if the business wants both immediate sales and future customer growth.

| Rank | Campaign | Channel | Leads | Conversion | Total Sales | Sales / Lead | 95% CI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B | Email | 9,700 | 48.18% | $225,285.52 | $23.23 | 47.18% to 49.17% |
| 2 | A | Email | 7,683 | 47.22% | $177,366.97 | $23.09 | 46.11% to 48.34% |
| 3 | B | Instagram | 7,100 | 48.30% | $166,722.17 | $23.48 | 47.13% to 49.46% |
| 4 | B | Web Banner | 7,110 | 47.64% | $164,125.79 | $23.08 | 46.48% to 48.80% |
| 5 | A | Instagram | 5,456 | 48.72% | $127,814.93 | $23.43 | 47.39% to 50.04% |
| 6 | A | Web Banner | 5,548 | 47.12% | $127,213.12 | $22.93 | 45.81% to 48.43% |

## Campaign Tone Comparison
| Campaign | Tone | Overall Sales | Overall Conversion | New-Customer Sales | New-Customer Conversion |
| --- | --- | --- | --- | --- | --- |
| B | Sales-oriented tone | $1,300,870.14 | 47.70% | $556,133.48 | 48.05% |
| A | Casual tone | $1,013,872.40 | 47.72% | $432,395.02 | 47.63% |

Campaign B wins on revenue, but not because it has a clearly superior conversion rate. Overall campaign-level conversion parity is very tight (z = -0.04, p = 0.965), and the new-customer conversion difference is also not statistically decisive (z = 0.87, p = 0.384).
The commercial conclusion is still strong: B wins because it turns equal spend into more revenue at the combinations with the most scale, especially Email.

## Channel-Level Tone Effect
| Channel | B - A Sales | B - A Conversion | B - A Sales / Lead | p-value |
| --- | --- | --- | --- | --- |
| Email | $118,324.43 | +0.67 pp | $0.16 | 0.180 |
| Web Banner | $88,920.81 | -0.05 pp | $-0.02 | 0.927 |
| Instagram | $79,752.49 | -0.93 pp | $-0.27 | 0.116 |

## Final Recommendation
1. Make **Campaign B + Email** the primary investment option for the next budget cycle.
2. Use **Campaign B + Instagram** as the secondary optimization lane because it has the best efficiency among the top-performing combinations.
3. Keep **Campaign A + Instagram** as a learning benchmark for casual-tone creative in social placements.
4. Re-test email subject lines, offer framing, and CTA language inside Campaign B before changing the core channel mix.

## Limitations
- The file does not include media spend, CPA, or margin, so this is a revenue optimization recommendation rather than a full ROI model.
- The sample covers one week only, so seasonality and fatigue effects are not observable.
- Statistical tests here only cover conversion-rate differences; they do not estimate incremental lift against a no-campaign control.