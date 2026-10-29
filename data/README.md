# Data

## Sources

| Source | Publisher | URL | Accessed on | License / terms |
|---|---|---|---|---|
| Migration cost caps for 16 countries, as stated by the Minister of Expatriates' Welfare in parliament (2017 revision) | The Financial Express | https://thefinancialexpress.com.bd/economy/record-number-of-workers-went-abroad-in-2017-1516033631 | 2026-10-29 | News article; only the figures are used, no text copied |
| Malaysia migration cost cap of Tk 78,990 (July 2022) | The Business Standard | https://www.tbsnews.net/bangladesh/migration-cost-malaysia-fixed-tk78990-454158 | 2026-10-29 | News article; only the figure is used |
| Same Malaysia figure, second report | The Daily Star | https://www.thedailystar.net/nrb/migration/news/govt-sets-tk-78990-max-migration-cost-bangladesh-workers-going-malaysia-3066141 | 2026-10-29 | Used only to confirm the figure |
| Singapore figure of Tk 262,200 (differs from Tk 262,270 above) | The Financial Express (2019) | https://thefinancialexpress.com.bd/trade/migration-cost-may-go-up-as-airfare-medical-fees-rise-1554871594 | 2026-10-29 | Recorded in the `note` column |
| Cost of Migration Survey 2020 | Bangladesh Bureau of Statistics | *(to be added)* | | |

## Files

- `clean/fee_caps.csv`: one row per destination (Saudi Arabia has two rows: male and female workers). Columns: destination, cap in taka, who it applies to, year set, who reported it, report date, report link, status, note.

## What could not be checked

- The official notices: the Ministry of Expatriates' Welfare website (probashi.gov.bd) was searched but the notices were not found in its listings, and its document storage host (objectstorage.ap-dcc-gazipur-1.oraclecloud15.com) reset the connection. bmet.gov.bd and bbs.gov.bd fail with a certificate error. Every cap is therefore marked "reported in news; official notice not found online".
- Whether any cap other than Malaysia's has been changed since 2017.
