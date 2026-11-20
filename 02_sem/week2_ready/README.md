# Visualization, demography, and earnings

Use Python to explore population indicators, read life tables, compare earnings distributions, and interpret a simple regression.

## Materials

| File | Contents |
| --- | --- |
| [Presentation](Week2_Visualization_Demography_Earnings.pdf) | Chart selection, demographic measures, earnings definitions, and regression interpretation |
| [Setup check](00_setup_check.ipynb) | Python packages, working folder, and data checks |
| [Visualization](01_visualization_student.ipynb) | Line, bar, and scatter plots; axis labels; figure export |
| [Demography](02_demography_student.ipynb) | Period life expectancy, survivorship, and remaining lifetime |
| [Earnings](03_earnings_student.ipynb) | RLMS-HSE data cleaning, descriptive gaps, distributions, and OLS |
| [Student archive](student_materials.zip) | Notebooks, presentation, setup instructions, and public demographic datasets |
| [Data documentation](data/README.md) | Sources, units, response codes, and reproducibility |

The exercise cells are empty. Write your code and interpretations in your own copy of each notebook. Each notebook starts independently; run its cells in order. The earnings notebook includes an optional extension on log earnings and categorical education.

## Installation and launch

The materials use the same Python environment as Week 1, with `statsmodels`, `pyreadstat`, and `py7zr` added. Open a terminal in this folder and use the Python interpreter associated with your Jupyter kernel:

```bash
python -m pip install -r requirements.txt
python -m notebook
```

If you already have Jupyter open, install packages in its active kernel with:

```python
%pip install -r requirements.txt
```

Then restart the kernel. Run [00_setup_check.ipynb](00_setup_check.ipynb). Full Windows, macOS, Linux, environment, and troubleshooting instructions are in [SETUP_EN.txt](SETUP_EN.txt).

## RLMS-HSE data

Download the English **longitudinal individual** dataset from the [official HSE downloads page](https://www.hse.ru/en/rlms/downloads). Follow the [access requirements](https://www.hse.ru/en/rlms/reg) and any registration or agreement shown by the provider. Choose **Individuals / For STATA**. Do not choose households, SPSS, or a reproductive-health module.

The exercise uses **2024**, even if the current longitudinal file also contains later years. The preparation script accepts an English individual `.7z` archive or its extracted `.dta` file. It was verified with `RLMS_IND_1994_2024_eng_DTA.7z`; when using an updated release, it checks required variable labels, the presence of 2024, and unique person records.

From this folder, run the following, replacing the example path with your downloaded file:

```bash
python prepare_rlms.py --input "/path/to/RLMS_IND_1994_2025_eng_DTA.7z"
```

Windows example (replace the username and filename):

```powershell
python prepare_rlms.py --input "C:\Users\YourName\Downloads\RLMS_IND_1994_2025_eng_DTA.7z"
```

For an already extracted file:

```bash
python prepare_rlms.py --input "/path/to/RLMS_IND_1994_2024_eng.dta"
```

The archive is small relative to its expanded contents: the verified version expands to about **14.7 GB (13.7 GiB)**. Allow roughly **16 GB of free temporary disk space**, or more if the current release is larger. The script checks available space before extraction. It reads only the required variables, removes its own temporary unpacked file, and preserves your original download. An interrupted run may leave a folder named `popdev_rlms_*` in the system temporary directory; remove that folder only after the process has stopped.

The script creates:

- `data/rlms_2024_earnings.csv`: eight columns, one row per person in 2024; original response codes retained for the cleaning exercise.
- `data/rlms_local_provenance.json`: your source filename, checksums, and variable labels.

Both files stay local and are excluded from version control. The student ZIP does not contain RLMS microdata. Keep raw data and extracts off your public repository; publish your code, aggregate figures/tables, and source/access instructions. Consult the provider's terms for any other distribution.

## Datasets

`data/wdi_population.csv` is the World Bank teaching snapshot used in Week 1: eight countries, four selected years, population counts, population aged 65+, life expectancy, and urban share.

`data/wpp_life_tables.csv` is a small extract of **UN World Population Prospects 2024**, with Germany, Italy, Japan, and the Russian Federation, 2000–2023, all three published sex categories, and 22 age intervals. It contains published life-table values, including `lx`, `Tx`, and `ex`.

Sources, direct download links, column meanings, transformations, and checksums are in [data/README.md](data/README.md) and [data/provenance.json](data/provenance.json). Public demographic datasets work offline after downloading the archive.

## From exercise to research

State the unit of observation, time period, sample restrictions, and measurement units before reporting a result. Include a source and an informative caption with each figure. Distinguish counts, rates, percentages, and conditional expectations. A regression coefficient describes an association under a specified model; a causal interpretation needs a research design and additional assumptions.

The RLMS exercise is unweighted and uses one year. Its HC3 standard errors do not incorporate the complex survey design. These results describe a selected analytic sample; they are not official estimates for the Russian population. Education codes are categories, not years of schooling. Monthly receipts are not hourly pay.

Panel models and Oaxaca–Blinder decomposition are possible later extensions. Repeated observations alone do not identify causal effects, and an unexplained decomposition component is not automatically discrimination. The core notebooks focus on definitions, plots, sample construction, and simple models.

Optional reading:

- [Panel regression examples](https://bashtage.github.io/linearmodels/panel/examples/examples.html): distinguish differences between people from changes within a person. Consider which variables vary over time and how repeated observations affect uncertainty. The local 2024 teaching extract is a cross-section and cannot estimate individual fixed effects across years.
- [Oaxaca–Blinder decomposition](https://www.statsmodels.org/stable/generated/statsmodels.stats.oaxaca.OaxacaBlinder.html): separate a model-based mean gap into components associated with group characteristics and coefficients. Check the reference structure and included variables; the labels “explained” and “unexplained” do not establish causal mechanisms.

See the [final research project requirements](../../01_sem/day1_ready/FINAL_PROJECT.md): an original, feasible question; a literature review; a justified method; Python analysis; and an article of at most 15 pages. LLM assistance is permitted for code that you understand and verify. The article must be written without LLM assistance or plagiarism.

## Instructions for an assistant helping with setup

1. Work in `02_sem/week2_ready`, or the extracted `popdev_week2` folder. Preserve the notebook/data folder structure and the learner's work.
2. Inspect the active interpreter with `import sys; print(sys.executable)`. Install `requirements.txt` into that interpreter, and restart its Jupyter kernel.
3. Confirm the two public CSVs are present. If RLMS is missing, direct the user to HSE's download/access pages. Do not register, accept an agreement, or supply credentials on the user's behalf.
4. Run `prepare_rlms.py` against the user's own downloaded English individual file. Do not upload, commit, or send the raw file, extract, or local provenance to an external service.
5. Run the setup-check notebook and report missing dependencies/files precisely. A missing RLMS file does not prevent the visualization and demography notebooks from opening.
6. Keep exercise cells available for the learner to complete. Do not replace the research article with generated prose.

## Reference documentation

- [Matplotlib: figure and axes](https://matplotlib.org/stable/users/explain/quick_start.html)
- [Seaborn: statistical visualization](https://seaborn.pydata.org/tutorial.html)
- [statsmodels: formula-based regression](https://www.statsmodels.org/stable/example_formulas.html)
- [UN demographic indicator definitions](https://population.un.org/dataportal/data/indicators/61,75,76/locations/900/start/1990/end/2023/metadata)
- [RLMS-HSE codebooks](https://www.hse.ru/en/rlms/code) and [citation instructions](https://www.hse.ru/en/rlms/reference)
