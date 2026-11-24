# Data definitions and provenance

All five CSV files are included in the [student package](../student_materials.zip). Original download links and preparation details are below; hashes are recorded in [provenance.json](provenance.json).

## Cultural-domain examples: entirely synthetic

The question used to construct the examples is: “What comes to mind when you think about support for older residents?” There were **no interviews, real participants, or real service observations**. The examples were authored for this course; observed patterns are properties of the fixture, not research findings.

| File | Unit and columns |
| --- | --- |
| `synthetic_freelists.csv` | 24 fictional respondents; `respondent_id`, ordered responses `item_1`–`item_5`; shorter lists have blank trailing cells |
| `synthetic_respondents.csv` | One row per fictional respondent; `respondent_id`, `age_group`; eight records in each group: 18–39, 40–64, 65+ |
| `synthetic_piles.csv` | 192 placements; one row per fictional respondent and card; `respondent_id`, `item`, `pile_id` |

The free lists deliberately include variable list lengths, capitalisation/spacing variation, and two within-list synonym duplicates. Preserve the raw text. The teaching codebook maps `bus service` and `buses` to `transport`, and `home care` to `home support`. Keep the earliest mention after normalisation and recompute consecutive ranks and list lengths. These are explicit coding choices; real projects must justify their own decisions.

All fictional respondents have non-empty lists. The denominator for frequency percentages and Smith's S is therefore all 24 cleaned non-empty lists. If applying the method to other data, distinguish a genuine non-mention from a missing interview or an unusable list and state the denominator policy.

For Smith's S, a listed item contributes `(L - r + 1) / L`, where L is cleaned list length and r starts at 1. Unmentioned items contribute zero. Average across all eligible lists. This differs from `frequency / (N * mean_rank)`, another salience measure: do not label different formulas interchangeably. See [Smith and Borgatti](https://qualquant.org/wp-content/uploads/cda/%2Asmith%20and%20borgatti%201997%20salience%20and%20accuracy.pdf) and the [AnthroTools guide](https://anthrotools.wordpress.com/wp-content/uploads/2016/05/anthrotools_guide.pdf).

Every fictional sorter places the same eight cards exactly once. Pile labels are respondent-specific; P1 is not a common theme across people. Six authored sorting templates repeat across the 24 records. This intentionally simple structure cannot support claims about discovered cultural groups. Co-sorting similarity is the share of these sorters placing a pair together. It is neither a correlation coefficient nor proof that two concepts have the same meaning.

The synthetic files may be reused as teaching fixtures with course attribution; preserve their synthetic designation.

## Card–Krueger restaurant survey: real research data

**Source:** David Card and Alan B. Krueger (1994), *Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania*, American Economic Review, 84(4), 772–793.

- [Author's data page](https://davidcard.berkeley.edu/data_sets)
- [Original ZIP download](https://davidcard.berkeley.edu/data_sets/njmin.zip)
- [Provider README](https://davidcard.berkeley.edu/readme/njmin-readme.txt)
- [Original article](https://davidcard.berkeley.edu/papers/njmin-aer.pdf)

The author-hosted ZIP contains `public.dat`, `codebook`, `check.sas`, and survey documentation. The provider README also relates the files to Chapter 2 of *Myth and Measurement*. The extract was prepared on 24 November 2026: read the fixed-width file using the codebook positions, recognise dot-coded missing values, select/rename columns, and retain all **410 rows**. No employment aggregation or row exclusion occurs before the exercise. The source archive checksum and exact column mapping are in the provenance file.

`card_krueger_1992.csv` contains:

| Column | Definition |
| --- | --- |
| `store_id` | Verified unique composite of state and original sheet number, e.g. PA-46 |
| `source_sheet` | Original SHEET code; 407 appears in both states, so this column alone is not a unique ID |
| `state_nj` | 1 = New Jersey; 0 = Pennsylvania |
| `chain` | 1 Burger King; 2 KFC; 3 Roy Rogers; 4 Wendy's |
| `company_owned` | 1 if company-owned, 0 otherwise |
| `status_after` | Follow-up status, defined below |
| `full_time_before`, `full_time_after` | Reported full-time employee counts, excluding managers counted separately |
| `part_time_before`, `part_time_after` | Reported part-time employee counts |
| `managers_before`, `managers_after` | Reported managers/assistant managers |
| `wage_before`, `wage_after` | Starting hourly wage, nominal US dollars |

The before wave was February–March 1992; the after wave was November–December 1992. New Jersey raised its minimum wage from $4.25 to $5.05 on 1 April 1992; Pennsylvania's remained $4.25. These are historical case-study values.

FTE employment is full-time employees + managers + 0.5 × part-time employees. It is not headcount or a direct sum of reported hours. Use explicit arithmetic; a missing component makes the calculated total missing.

| `status_after` | Meaning | Handling in this exercise |
| --- | --- | --- |
| 0 | Refused follow-up | Missing follow-up FTE |
| 1 | Answered follow-up | Calculate from recorded components; preserve component missingness |
| 2 | Closed for renovations | Missing follow-up FTE |
| 3 | Permanently closed | Zero follow-up FTE |
| 4 | Closed for highway construction | Missing follow-up FTE |
| 5 | Closed due to mall fire | Missing follow-up FTE |

The main comparison uses the same restaurants with observed FTE in both waves, including recorded permanent closures. Dropping closures is a separate sensitivity check and changes the population described. A before/after panel does not itself establish parallel untreated trends. One pre-policy wave cannot reveal a pre-trend. Hundreds of restaurants do not create hundreds of independently assigned state policies.

Credit the original authors when using the data. The course's synthetic-data reuse statement does not apply to the original survey or article.

## Training programme: optional synthetic example

`synthetic_training.csv` contains 400 fictional records generated with NumPy seed **20261124**. No real programme or participants are represented.

| Column | Definition |
| --- | --- |
| `person_id` | Unique fictional record ID |
| `age_before` | Age in years before programme participation |
| `earnings_before` | Baseline monthly earnings, arbitrary currency units |
| `unemployment_months_before` | Months unemployed before participation |
| `training` | Simulated participation: 0/1 |
| `earnings_after` | Follow-up monthly earnings, same arbitrary units |

The generation equations and distributions are in [provenance.json](provenance.json). All variables in the propensity model precede treatment in this simulation. Matching does not reveal a real effect, and a finite-sample estimate need not equal the fixed effect used by the generator.

The extension uses nearest controls in estimated log-odds, an explicit caliper, and replacement. Reused controls must retain their multiplicity in balance and outcome calculations. Check balance rather than relying on a non-significant t-test. When treated units are unmatched, describe the retained treated population. Methodological reference: [MatchIt authors' documentation](https://kosukeimai.github.io/MatchIt/reference/matchit.html).
