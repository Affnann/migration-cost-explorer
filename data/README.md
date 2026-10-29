# Data

## Sources

| Source | Publisher | URL | Accessed on | License / terms |
|---|---|---|---|---|
| *Cost of Migration Survey 2020* (406 pages, scanned) | Bangladesh Bureau of Statistics, with ILO support | https://www.ilo.org/wcmsp5/groups/public/---asia/---ro-bangkok/---ilo-dhaka/documents/publication/wcms_766198.pdf (ILO Dhaka's copy; bbs.gov.bd could not be reached because of a certificate error) | 2026-10-29 | No reuse terms stated. Only the published table figures are used; the report itself is not posted here. SHA-256 of the file used: `75b25ae3c25dd7ea9d14a77ee0fb93d94079febb139feb282e5c1d14932213a1` |
| Migration cost caps for 16 countries, as stated by the Minister of Expatriates' Welfare in parliament (2017 revision) | The Financial Express | https://thefinancialexpress.com.bd/economy/record-number-of-workers-went-abroad-in-2017-1516033631 | 2026-10-29 | News article; only the figures are used |
| Malaysia migration cost cap of Tk 78,990 (July 2022) | The Business Standard | https://www.tbsnews.net/bangladesh/migration-cost-malaysia-fixed-tk78990-454158 | 2026-10-29 | News article; only the figure is used |
| Same Malaysia figure, second report | The Daily Star | https://www.thedailystar.net/nrb/migration/news/govt-sets-tk-78990-max-migration-cost-bangladesh-workers-going-malaysia-3066141 | 2026-10-29 | Used only to confirm the figure |
| Singapore figure of Tk 262,200 (differs from Tk 262,270 above) | The Financial Express (2019) | https://thefinancialexpress.com.bd/trade/migration-cost-may-go-up-as-airfare-medical-fees-rise-1554871594 | 2026-10-29 | Recorded in the `note` column |

## Files

- `clean/survey_cost_by_destination.csv`: Tables 5.5 (page 57) and 9.5 (page 123) of the survey report. Rows: Saudi Arabia, Oman, Malaysia, Qatar, Singapore, other countries, all countries.
- `clean/survey_borrowing_by_sex.csv`: Table 5.9 (page 64). Counts are the survey's estimates for all workers who left 2015–2018, not the number interviewed.
- `clean/fee_caps.csv`: one row per destination and cap (Saudi Arabia has rows for men and women; Malaysia has its 2017 and 2022 caps). The `current` column marks the cap used by the calculator.
- `clean/cap_vs_paid.csv`: built by `code/03_compare.py`.

## How the survey tables were read

The report has no text layer. Each table was read three ways: text recognition at 170 dpi, again at 300 dpi, and by eye from the page image. All three agreed. `code/02_check_survey.py` then checks the figures against the report's own arithmetic.

One inconsistency is in the report itself: the text on page 123 gives the overall average cost as Tk 408,951, while its Table 9.5 and every other table give Tk 416,789. The table figure is used.

## What could not be checked

- The official cap notices: probashi.gov.bd was searched but they were not found in its listings, and its document storage host (objectstorage.ap-dcc-gazipur-1.oraclecloud15.com) reset the connection. bmet.gov.bd and bbs.gov.bd fail with a certificate error.
- Whether any cap other than Malaysia's has changed since 2017, and what caps applied before the 2017 revision.
