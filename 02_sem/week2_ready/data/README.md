# Data sources and variables

## World Bank World Development Indicators

`wdi_population.csv` is the unchanged Week 1 snapshot, retrieved on 17 November 2026. There are 32 rows: Brazil, China, Germany, India, Japan, Mexico, the Russian Federation, and South Africa for 2010, 2015, 2020, and 2023. One row is one country-year. These countries and years were selected for teaching; they are not a representative sample of the world.

| Column | Meaning | Source indicator |
| --- | --- | --- |
| `country_code`, `country`, `year` | Identifiers | World Bank country codes |
| `population` | Total population, people | `SP.POP.TOTL` |
| `share_65_plus` | Population aged 65+, percent of total | `SP.POP.65UP.TO.ZS` |
| `life_expectancy` | Life expectancy at birth, years, both sexes | `SP.DYN.LE00.IN` |
| `urban_share` | Urban population, percent of total | `SP.URB.TOTL.IN.ZS` |

Percent columns are already on a 0–100 scale. Do not multiply them by 100 again.
Population counts and population shares answer different questions. An average of country percentages is not automatically a pooled population percentage.

Original indicator pages: [population](https://data.worldbank.org/indicator/SP.POP.TOTL), [aged 65+](https://data.worldbank.org/indicator/SP.POP.65UP.TO.ZS), [life expectancy](https://data.worldbank.org/indicator/SP.DYN.LE00.IN), [urban share](https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS).

Direct CSV ZIP downloads: [population](https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv), [aged 65+](https://api.worldbank.org/v2/en/indicator/SP.POP.65UP.TO.ZS?downloadformat=csv), [life expectancy](https://api.worldbank.org/v2/en/indicator/SP.DYN.LE00.IN?downloadformat=csv), [urban share](https://api.worldbank.org/v2/en/indicator/SP.URB.TOTL.IN.ZS?downloadformat=csv).

The snapshot's original API requests and checksums are preserved in `provenance.json`. WDI data are provided under the [World Bank dataset terms](https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets), subject to dataset-specific notices. Cite the World Bank and the indicator codes.

## United Nations World Population Prospects 2024

`wpp_life_tables.csv` contains 6,336 rows: four countries × 24 years × three sex categories × 22 age intervals. The country codes are DEU, ITA, JPN, and RUS; years are 2000–2023; sex categories are Male, Female, and Total. Total is the published both-sexes series, not an additional group to average with the other two.

The file was extracted on 20 November 2026 from the course's existing `WPP2024_Life_Table_Abridged_Medium_1950-2023.csv.zip`. The original download date of that archive is unknown. The preparation kept the selected countries, years, and columns, sorted rows, and preserved published numeric values. It did not estimate, impute, or reconstruct life tables. WPP 2024 estimates end in 2023; the exercise does not use projections.

Source: United Nations, Department of Economic and Social Affairs, Population Division (2024). *World Population Prospects 2024*. Online Edition.

- [WPP website and downloads](https://population.un.org/wpp/)
- [Official download catalogue and variable definitions](https://population.un.org/wpp/assets/downloads.json)
- [Original abridged life tables, 1950–2023, CSV gzip](https://population.un.org/wpp/assets/Excel%20Files/1_Indicator%20%28Standard%29/CSV_FILES/WPP2024_Life_Table_Abridged_Medium_1950-2023.csv.gz)
- [Life expectancy definitions](https://population.un.org/dataportal/data/indicators/61,75,76/locations/900/start/1990/end/2023/metadata)
- [WPP methodology](https://population.un.org/wpp/assets/Files/WPP2024_Methodology.pdf)

UN WPP material is attributed to the United Nations under [CC BY 3.0 IGO](https://creativecommons.org/licenses/by/3.0/igo/). This teaching extract is a filtered version, not a UN-endorsed product. It is a fixed snapshot; later downloads may be revised.

| Column | Meaning / unit |
| --- | --- |
| `ISO3_code`, `Location`, `Time`, `Sex` | Country code/name, calendar year, published sex category |
| `AgeGrp` | Age interval label: 0, 1–4, 5–9, …, 100+ |
| `AgeGrpStart` | Age at the start of the interval, years |
| `AgeGrpSpan` | Interval width; -1 denotes the terminal open interval, not a negative duration |
| `mx` | Central death rate for the age interval, per person-year |
| `qx` | Probability of dying within the interval conditional on reaching its start |
| `px` | Probability of surviving the interval; 1 − qx |
| `lx` | Survivors at the start age, per 100,000 life-table births |
| `dx` | Life-table deaths within the interval, from that hypothetical cohort |
| `Lx` | Person-years lived within the interval |
| `Tx` | Person-years remaining above the start age |
| `ex` | Expected remaining years of life at the start age; Tx / lx |
| `ax` | Average years lived within the interval by those dying within it |

Capitalisation matters: `lx` and `Lx` are different quantities. The life-table cohort is hypothetical. `lx` is not the country's actual population at an age; `dx` is not an observed national death count. `qx` is a probability and `mx` is a rate with a person-time denominator. Period life expectancy uses one period's mortality conditions and is not an individual forecast. At age 65, `ex` is conditional on reaching 65; it is not `e0 − 65`.

For 100+, use the published values. Do not substitute a five-year width or extend the curve to a fabricated zero at age 105. Birth and age-1 intervals also have different widths from five-year intervals.

## RLMS-HSE: local preparation required

The microdata are **not included** in the Week 2 distribution. Download English longitudinal individual Stata data through [HSE](https://www.hse.ru/en/rlms/downloads), follow its [access conditions](https://www.hse.ru/en/rlms/reg), and run `prepare_rlms.py` as described in the [README](../README.md#rlms-hse-data). Consult the [codebooks](https://www.hse.ru/en/rlms/code), [questionnaires](https://www.hse.ru/en/rlms/questionnaires), and [citation instructions](https://www.hse.ru/en/rlms/reference).

Credit the Russia Longitudinal Monitoring Survey, RLMS-HSE, its producers at HSE University, OOO Demoscope, and the Institute of Sociology of FCTAS RAS. Use the acknowledgement prescribed on the official citation page in research publications.

The local file `rlms_2024_earnings.csv` selects year 2024, verifies one record per person, drops personal identifiers, and retains eight variables. No outcome or age filters are applied during preparation. Special numeric response codes remain; blank CSV fields represent system missing values. Variable labels and source checksums are saved in the local `rlms_local_provenance.json` file. This file and the CSV must stay outside public version control.

| Teaching column | Original variable | Meaning |
| --- | --- | --- |
| `year` | `year` | Survey year; 2024 in the extract |
| `age` | `age` | Completed years of age |
| `sex_code` | `h5` | Source's recorded categories: 1 Male, 2 Female |
| `work_status` | `j1` | Current work status; 1 currently working |
| `earnings_rub` | `j10` | After-tax money received from the main job in the last 30 days, nominal rubles |
| `hours_week` | `j6_2` | Usual weekly hours in the main job |
| `education_code` | `diplom` | Completed education group, categorical |
| `person_weight` | `inwgt` | Individual sample weight; retained for reference, not used in the basic exercise |

Missing-response codes: 99999997 does not know; 99999998 refuses; 99999999 no answer. For hours, 99999995 is other and 99999996 is irregular hours; neither supplies a numerical weekly total. These codes must not enter numerical summaries as actual earnings, hours, or education levels.

Completed education groups (`diplom`): 1 = 0–6 school grades; 2 = incomplete secondary (7–8 grades); 3 = incomplete secondary plus other education; 4 = secondary school diploma; 5 = vocational secondary diploma; 6 = higher-education diploma or above. Treat these as categories. The source variable `educ` also uses categories; it is not automatically years of education.

The main exercise selects currently working respondents aged 18–65 with recorded sex 1 or 2, positive observed earnings, and observed usual hours from 1 to 168. Both main models use the same selected sample. We do not trim extreme earnings by default. Excluding respondents with irregular/missing hours is an analytical choice that should be reported.

The outcome is monthly receipts from the main job, not hourly pay or an annual salary. Usual weekly hours and receipts in the last 30 days refer to different time concepts. The unweighted models do not adjust for the full survey design, and HC3 standard errors do not remove this limitation. Do not interpret their sample gaps as official national estimates, causal effects, or direct measurements of discrimination.

The 1994–2024 archive was used to verify these exercises. HSE may supply a newer longitudinal release. Keep its local provenance record; if records are revised, reproduce and report your own results rather than forcing an older count or coefficient.
