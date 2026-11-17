# Week 1 — Python for Population and Development

Two online seminars of 90 minutes each. Teaching language: English. No previous programming experience is required. We work in **local Jupyter**, write code together, and then complete short independent tasks.

**Today’s route:** a 45-minute introduction, 45 minutes of classical Python, then 90 minutes of NumPy, pandas, Matplotlib, and seaborn. The student notebooks contain instructions and **empty code cells**, including the demonstration tasks. The instructor will type the code on screen.

## Start here

1. Download and extract [student_materials.zip](day1_ready/student_materials.zip). Extract the whole archive, including `data`.
2. Follow the setup instructions below. If Jupyter already works, use the existing environment and run the setup check.
3. Open [00_setup_check.ipynb](day1_ready/00_setup_check.ipynb) **through Jupyter**, not as a text file or a browser download preview.
4. Open the student notebooks in the order shown below. Keep the data folder beside them.

| Order | File | What you will do |
|---|---|---|
| Before class | [00_setup_check.ipynb](day1_ready/00_setup_check.ipynb) | Check Python, packages, and data paths; this diagnostic notebook has prepared code. |
| Introduction | [Lecture PDF](day1_ready/Intro_Seminar_Week1.pdf) | Course logistics, assessment, research questions, and the Python workflow. |
| 1 | [01_python_basics_student.ipynb](day1_ready/01_python_basics_student.ipynb) | Variables, types, lists, dictionaries, conditions, loops, and functions. |
| 2 | [02_numpy_student.ipynb](day1_ready/02_numpy_student.ipynb) | Arrays, arithmetic, Boolean masks, and population shares. |
| 3 | [03_pandas_student.ipynb](day1_ready/03_pandas_student.ipynb) | Read, check, select, transform, and summarise a demographic table. |
| 4 | [04_visualization_student.ipynb](day1_ready/04_visualization_student.ipynb) | Line, bar, and scatter plots with Matplotlib and seaborn. |

## Why these skills matter for Pop&Dev

HSE places Population and Development in **Public Administration**. Its published curriculum connects demography, public economics, public administration, and development policy. These are the substantive contexts for our programming examples. [Programme summary](https://www.hse.ru/en/ma/pd/passport), [curriculum](https://www.hse.ru/en/ma/pd/curriculum).

| Area | Example research question | Python skills practised this week |
|---|---|---|
| Demography | How has the share of people aged 65+ changed across selected countries? | Counts, shares, denominators, selection by country and year, time-series plots. |
| Public administration | What does population ageing imply for investigating service needs? | Briefing tables, absolute numbers versus percentages, readable comparisons, limits of an indicator. |
| Econometrics | How do two indicators vary together, and what would be needed to study a causal effect? | Observational units, comparable samples, panel-shaped data, scatter plots, careful interpretation. |

The programme’s listed **Statistical Analysis II** elective uses Python for applied statistics and econometrics, including regression and panel-data topics. Week 1 builds the programming and data-handling foundation for such work; it does not introduce regression estimation. [Course description](https://www.hse.ru/en/ma/pd/courses/1163615527.html).

By the end of the two seminars, you should be able to:

- Write and run small Python instructions, including a condition, loop, and function.
- Calculate indicators with meaningful units and denominators.
- Load a CSV, identify the unit of observation, and check missingness and duplicate keys.
- Select rows and columns, create a variable, and calculate a grouped summary.
- Make and explain a line chart, a bar chart, and a scatter plot.
- Save a notebook and check that the completed analysis runs in order.

## Schedule for today

The times below are **minutes from the start of each seminar**, not clock times. The break between seminars follows the actual class schedule and is outside the 180 teaching minutes.

### Seminar 1 — 90 minutes

| Minutes | Activity |
|---|---|
| 00–17 | Introduction: Pop&Dev, demography, public administration, econometrics. |
| 17–26 | Research workflow, the Python tools, and the teaching datasets. |
| 26–38 | Research project, assessment, report format, deadlines, and logistics. |
| 38–45 | Python / pip / Jupyter setup overview and transition to practice. |
| 45–57 | First cells, variables, arithmetic, strings, and types. |
| 57–65 | Lists and dictionaries. |
| 65–72 | Comparisons and `if` / `else`. |
| 72–78 | A `for` loop. |
| 78–84 | A small function with `def` and `return`. |
| 84–88 | Independent population-change task. |
| 88–90 | Save and recap. |

The introduction takes approximately **45 minutes** and is followed by Python practice.

### Seminar 2 — 90 minutes

| Minutes | Activity |
|---|---|
| 00–12 | NumPy arrays, calculations, masks, and summaries. |
| 12–18 | Independent population-share task. |
| 18–33 | pandas: read and inspect the table, select 2023, select columns, sort. |
| 33–48 | Check missingness and keys, create an older-population estimate, group by year. |
| 48–56 | Independent policy-briefing table and interpretation. |
| 56–59 | Three-minute screen break. |
| 59–71 | Plotting setup and a Matplotlib line chart. |
| 71–79 | A seaborn bar chart. |
| 79–86 | Independent scatter plot and interpretation. |
| 86–90 | Exit ticket, save, and next steps. |

Sections marked **Extra practice after class** are outside this timed route. They include two-dimensional NumPy arrays, additional work with the Adult dataset, a histogram, and exporting tables and figures.

## Assessment and research deadlines

**Final grade = 100% Research.** Seminar participation and the Week 1 exercises have no separate percentage in the course grade. They prepare you for the research project.

| Milestone | Deadline |
|---|---|
| Choose a research topic | **Tuesday, 24 November 2026** |
| Submit the research project | **Friday, 25 December 2026** |

No submission hour or early-submission bonus is specified here. Do not use the dates or grade formula in the archived 2025 presentation.

For topic selection, prepare a focused question, a possible data source, the observational unit, the period, and a short analysis plan. Check that you can access the data before choosing a question that depends on it.

The report format retained from the previous course materials is **up to 10 pages**, with a literature discussion using **5–10 sources**:

1. Research question and rationale.
2. Relevant literature.
3. Data source, definitions, observational unit, coverage, and limitations.
4. Exploratory analysis: summary statistics, tables, and figures.
5. Analysis appropriate to the question, with explanations of methods and results.
6. Conclusions, limitations, and references.

Provide the PDF report and a repository containing the Python notebooks and documented data or retrieval instructions. The previous course submission contact is retained: **va.sergeev@hse.ru**. Include the repository link with the research PDF. Use the topic-submission channel indicated by the instructor; the old Google Sheet is not assumed to be the current channel.

A good project connects its question, data, method, and interpretation. Correctness and reproducibility matter more than adding an unnecessarily complex model. Descriptive work should make descriptive claims; a causal question needs a suitable design and assumptions. These are quality principles, not an additional weighted grading formula.

## Materials and folder layout

After extracting the student archive, the working folder contains:

```text
popdev_week1/
├── README.md
├── SETUP_EN.txt
├── requirements.txt
├── Intro_Seminar_Week1.pdf
├── 00_setup_check.ipynb
├── 01_python_basics_student.ipynb
├── 02_numpy_student.ipynb
├── 03_pandas_student.ipynb
├── 04_visualization_student.ipynb
└── data/
    ├── wdi_population.csv
    ├── wdi_provenance.json
    ├── adult.data.csv
    └── DATA_NOTE_EN.txt
```

If you downloaded the whole GitHub repository, the equivalent working folder is `01_sem/day1_ready`. Start Jupyter there. The original files directly under `01_sem` are last year’s source materials; the Week 1 route above uses the revised files.

Course repository: [HSE Population and Development mentors seminar](https://github.com/SergeevVladislav/HSE_PopDev_Mentors_Seminar_Python_Fall_2025).

## Setup: what each component does

| Component | Purpose |
|---|---|
| Python | Interpreter that executes the code. These materials were checked with Python 3.12. |
| Virtual environment (`.venv`) | Keeps this project’s installed packages separate from other projects. |
| `pip` | Installs packages into a Python environment. |
| Jupyter Notebook / JupyterLab | Browser interface for writing cells, seeing output, and adding explanations. |
| Kernel | The running Python process behind a notebook. It must use the environment containing your packages. |
| `import` | Makes an installed library available inside the current Python session. |

Installation needs internet access. After setup, the notebooks use local files and can run offline. You do not need a GPU, a paid service, or a cloud notebook account.

### If Python and Jupyter already work

Keep your existing environment. Open `00_setup_check.ipynb` and run its prepared cells.

If a library is missing, run this **inside a Jupyter Python code cell**:

```python
%pip install numpy pandas matplotlib seaborn
```

Restart the kernel, then repeat the check. `%pip` uses the environment of the current IPython kernel. It is a notebook command, not a line to copy into an ordinary `.py` file. See [IPython documentation](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pip).

### Fresh installation: Windows

1. Install a supported Python 3 from [python.org](https://www.python.org/downloads/), if Python is not installed. If the installer offers **Add Python to PATH**, enable it. Close and reopen your terminal after installation.
2. Extract the course archive. Open **Command Prompt or PowerShell in the extracted folder**.
3. Check the Python launcher:

```powershell
py --version
```

4. Create a local environment, install the listed packages, and launch Jupyter:

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m notebook
```

If `py` is unavailable but `python --version` works, use `python -m venv .venv` for the first line. The remaining commands are unchanged. These commands use the environment’s Python directly, so activation and PowerShell activation-policy changes are not needed.

### Fresh installation: macOS

1. Install a supported Python 3 from [python.org](https://www.python.org/downloads/), if needed.
2. Open Terminal in the extracted materials folder. Check Python, create an environment, install packages, and start Jupyter:

```bash
python3 --version
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m notebook
```

Do not modify the operating system’s Python installation to run this course. Use the project environment.

### Fresh installation: Linux

In a terminal inside the materials folder:

```bash
python3 --version
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m notebook
```

If Python or its `venv` support is missing, install it using your distribution’s normal package manager or ask for setup help. On Debian/Ubuntu the relevant system packages are commonly `python3`, `python3-venv`, and `python3-pip`. Do not use `sudo pip` or disable an externally-managed-environment protection to install course libraries.

Keep the terminal running while Jupyter is open. The notebook interface is displayed in a browser, but the code executes on your own computer. These steps follow the [Python packaging guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) and [Jupyter installation documentation](https://jupyter.org/install).

### Packages and kernels

`requirements.txt` installs Jupyter Notebook, ipykernel, NumPy, pandas, Matplotlib, and seaborn. Seaborn 0.13 or newer supports the plotting syntax used here. Installation selects compatible versions for your Python. Run `00_setup_check.ipynb` to check your environment before class.

If Jupyter opens but uses the wrong Python, inspect the selected interpreter in a code cell:

```python
import sys
print(sys.executable)
```

If necessary, register the environment as a named kernel. Run the appropriate line **in the terminal**, from the materials folder:

```powershell
# Windows
.venv\Scripts\python.exe -m ipykernel install --user --name popdev-week1 --display-name "Python (PopDev Week 1)"
```

```bash
# macOS / Linux
.venv/bin/python -m ipykernel install --user --name popdev-week1 --display-name "Python (PopDev Week 1)"
```

Then select **Python (PopDev Week 1)** in Jupyter’s kernel menu and rerun the imports. This is an optional fix; it is not necessary if your existing kernel already passes the setup check.

## How to work in Jupyter

1. Open an `.ipynb` file through Jupyter’s file browser and select a Python kernel if prompted.
2. Read the task above the empty code cell.
3. Watch the instructor type a short piece of code, then type it yourself. Use straight quotes and a decimal point.
4. Press **Shift + Enter** to run a cell and move to the next one. **Ctrl + Enter** runs it without moving.
5. Read the result, not just the code. Check its unit and whether it answers the question.
6. Save with **Ctrl + S** or **Cmd + S** on macOS.
7. After completing the work, restart the kernel and run the notebook from the beginning. Menu wording differs between Jupyter versions.

Code cells run Python; Markdown cells contain explanations. Editing a cell does not rerun it. The kernel remembers the order in which cells actually ran. Importing pandas in one notebook does not import it in a different notebook’s kernel.

Do not type `pip install ...` as ordinary Python. Use the terminal commands above or `%pip` in a notebook. Do not paste the `>>>` prompt from a Python documentation example into your cell.

Online routine: write **done** or **help** in the chat. When asking about an error, give the task label, such as `PY-04` or `PD-02`, and the last line of the error message. Keep a local copy of your work.

## Data and interpretation

### Main data: World Bank demographic indicators

The supplied `wdi_population.csv` contains **32 rows and 7 columns**: eight countries, each observed in 2010, 2015, 2020, and 2023. Values are taken from World Bank indicator downloads. No missing values were imputed. The extract is kept fixed for class; `wdi_provenance.json` records retrieval details, source URLs, and the selected original values.

| Column | Meaning | Unit / role |
|---|---|---|
| `country_code` | Three-letter country identifier | Part of the observation key |
| `country` | Country name supplied by the source | Label |
| `year` | Reference year | Part of the observation key |
| `population` | Total population, `SP.POP.TOTL` | People |
| `share_65_plus` | Population aged 65+, `SP.POP.65UP.TO.ZS` | Percent of total population |
| `life_expectancy` | Life expectancy at birth, `SP.DYN.LE00.IN` | Years |
| `urban_share` | Urban population, `SP.URB.TOTL.IN.ZS` | Percent of total population |

Sources and definitions: [total population](https://data.worldbank.org/indicator/SP.POP.TOTL), [population aged 65+](https://data.worldbank.org/indicator/SP.POP.65UP.TO.ZS), [life expectancy](https://data.worldbank.org/indicator/SP.DYN.LE00.IN), [urban population](https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS).

The countries were selected for a manageable teaching example; they are not a random or representative world sample. A country-year is not a person. Summing population across different years does not give a meaningful single-year population total. An unweighted mean of country shares gives every country equal weight; a combined population share requires population weights or appropriate sums of counts. Derived numbers of older people are approximate combinations of published estimates.

Life expectancy at birth is a period life-table measure, not the average age at death in a sample. Urban definitions and country estimates have source-specific limitations. Use the indicator documentation in substantive research. A scatter plot shows a pattern in the selected observations; it does not establish causation.

### Additional data: Adult Income

The existing `adult.data.csv` is retained for after-class exercises. It contains 32,561 historical individual records and 15 original columns. Question marks denote missing categories. The local `salary` field gives an annual income category, not exact earnings. Classroom summaries are unweighted descriptions of this file. [UCI dataset documentation](https://www.archive.ics.uci.edu/dataset/2/adult).

All small town examples in the Python and NumPy notebooks are **fictional**, and their assumed thresholds or growth rates are classroom scenarios, not policy standards or forecasts.

## Troubleshooting

| Symptom | First thing to check |
|---|---|
| `ModuleNotFoundError` | Is the package installed in the kernel’s environment? Use `sys.executable`, then `%pip` if needed. Restart after installation. |
| `FileNotFoundError` | Was the whole archive extracted? Is `data` beside the notebook? Check the working folder below. |
| `NameError` | Check spelling and capitalisation. Run the cell defining the name or import first. |
| `SyntaxError` | Check quotes, brackets, commas, and colons. Terminal commands are not Python syntax. |
| `IndentationError` | Use consistent four-space indentation after `if`, `else`, `for`, and `def`. |
| `KeyError` | Use the exact column or dictionary key, including spelling and punctuation. |
| A cell remains busy | Wait briefly, then interrupt the kernel if necessary. Restart and run earlier cells again. |
| A plot is blank | Run the data preparation and plotting cell; include `plt.show()`. Check that the filter selected observations. |
| Results differ after restart | The earlier run depended on execution order or a missing definition. Read the notebook from the top. |

To diagnose a file path, run this in a code cell:

```python
from pathlib import Path
print(Path.cwd())
print(Path("data/wdi_population.csv").exists())
```

The second result should be `True`. If it is `False`, reopen Jupyter in the materials folder or use the actual full file path. Do not download a different dataset to solve a local path problem.

If installation is not ready during class, follow the shared screen, predict outputs, and take part in the chat. Finish setup after the session; avoid repeatedly reinstalling a working environment.

## Practice after class

- Finish the core tasks you did not complete, write short interpretations, and check each completed notebook with a fresh kernel.
- Try the clearly marked extra sections: a two-dimensional array, real missing values in Adult, a histogram, and exports.
- Draft a research question for the topic deadline. Identify an accessible source, the observation unit, relevant variables, and a plausible analysis.

## Reference documentation

- [Python introduction](https://docs.python.org/3/tutorial/introduction.html) and [control flow](https://docs.python.org/3/tutorial/controlflow.html).
- [NumPy beginner guide](https://numpy.org/doc/stable/user/absolute_beginners.html).
- [pandas introductory tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html).
- [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html).
- [seaborn scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html) and [barplot](https://seaborn.pydata.org/generated/seaborn.barplot.html).
- [Jupyter notebook basics](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html).
