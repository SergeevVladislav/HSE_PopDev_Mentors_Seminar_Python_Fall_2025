# Week 1 — Python for Population and Development

Python for demographic analysis, public administration, and the foundations of econometrics.

## Materials

| Material | Contents |
|---|---|
| [Introduction](Intro_Seminar_Week1.pdf) | Population indicators, policy questions, research design, and reproducible analysis. |
| [Python](01_python_basics_student.ipynb) | Variables, types, lists, dictionaries, conditions, loops, and functions. |
| [NumPy](02_numpy_student.ipynb) | Arrays, arithmetic, Boolean masks, and population shares. |
| [pandas](03_pandas_student.ipynb) | Loading, checking, filtering, transforming, and summarising data. |
| [Matplotlib and seaborn](04_visualization_student.ipynb) | Line charts, bar charts, scatter plots, histograms, and figure export. |
| [Environment check](00_setup_check.ipynb) | Python interpreter, package versions, and local data paths. |

Download and extract [student_materials.zip](student_materials.zip).
Keep the notebooks and the `data` folder together. The exercise notebooks contain task descriptions and empty code cells.

## Analytical questions

| Area | Example question | Concepts |
|---|---|---|
| Demography | How has the share of people aged 65+ changed across selected countries? | Counts, shares, denominators, country-year observations, and time series. |
| Public administration | What additional evidence is needed to plan services for an ageing population? | Absolute numbers, percentages, service coverage, and briefing tables. |
| Econometrics | How do two indicators vary together, and what would be needed to estimate a causal effect? | Observational units, comparable samples, association, and research design. |

## Files and working directory

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

Use `popdev_week1` as the working directory after extracting the archive.
For a clone or download of the full repository, use `01_sem/day1_ready`.
Run the terminal commands below from that directory.

## Python and Jupyter setup

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
2. Extract the materials archive. Open **Command Prompt or PowerShell in the extracted folder**.
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

Do not modify the operating system’s Python installation to run these notebooks. Use the project environment.

### Fresh installation: Linux

In a terminal inside the materials folder:

```bash
python3 --version
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m notebook
```

If Python or its `venv` support is missing, install it using your distribution’s normal package manager or ask for setup help. On Debian/Ubuntu the relevant system packages are commonly `python3`, `python3-venv`, and `python3-pip`. Do not use `sudo pip` or disable an externally-managed-environment protection to install these libraries.

Keep the terminal running while Jupyter is open. The notebook interface is displayed in a browser, but the code executes on your own computer. These steps follow the [Python packaging guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) and [Jupyter installation documentation](https://jupyter.org/install).

### Packages and kernels

`requirements.txt` installs Jupyter Notebook, ipykernel, NumPy, pandas, Matplotlib, and seaborn. Seaborn 0.13 or newer supports the plotting syntax used here. Installation selects compatible versions for your Python. Run `00_setup_check.ipynb` to check the environment.

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

## Using Jupyter

1. Open an `.ipynb` file through Jupyter's file browser and select a Python kernel.
2. Write Python in a code cell. Use Markdown cells for explanations.
3. Press **Shift + Enter** to run a cell and move to the next one; **Ctrl + Enter** runs it without moving.
4. Save with **Ctrl + S**, or **Cmd + S** on macOS.
5. After completing the code, restart the kernel and run the notebook from the beginning to check execution order.

Editing a cell does not rerun it. The kernel remembers variables in the order in which cells actually ran.
Each notebook needs its own imports and definitions. Use straight quotes and a decimal point in Python code.

Terminal commands belong in a terminal. `%pip` is an IPython command that can run inside a notebook.
Do not paste the `>>>` prompt from documentation into a code cell.

## Setup checks for terminal tools and agents

- **Working directory:** the directory containing `requirements.txt`, the notebooks, and `data/`.
- **Interpreter:** use the existing working environment, or the `.venv` interpreter created by the commands above.
- **Dependencies:** install from `requirements.txt` using that interpreter's `-m pip`; do not install into a different Python environment.
- **Verification:** run `00_setup_check.ipynb` in the same environment. All four library imports must succeed, both data-file checks must be `True`, and the demographic table shape must be `(32, 7)`.
- **Launch:** run the environment's Python with `-m notebook` from the working directory. Select the matching kernel.

The environment check contains executable diagnostic cells. The exercise notebooks contain blank cells; running them does not verify an analysis.

## Datasets

### World Bank demographic indicators

[Download the prepared CSV](data/wdi_population.csv?raw=1).
The same file is included in the materials archive at `data/wdi_population.csv`.

The file contains **32 rows and 7 columns**: Brazil, China, Germany, India, Japan, Mexico, the Russian Federation, and South Africa, each observed in **2010, 2015, 2020, and 2023**.
One row is a **country-year**, identified by `country_code` and `year`.

| Column | Meaning | Unit |
|---|---|---|
| `country_code` | Three-letter country identifier | Observation key, with `year` |
| `country` | Country name supplied by the source | Text |
| `year` | Reference year | Calendar year |
| `population` | Total population | People |
| `share_65_plus` | Population aged 65+ | Percent of total population |
| `life_expectancy` | Life expectancy at birth | Years |
| `urban_share` | Urban population | Percent of total population |

Original sources and downloads:

| Indicator | Definition | Full source download |
|---|---|---|
| `SP.POP.TOTL` | [Total population](https://data.worldbank.org/indicator/SP.POP.TOTL) | [CSV archive](https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv) |
| `SP.POP.65UP.TO.ZS` | [Population aged 65+](https://data.worldbank.org/indicator/SP.POP.65UP.TO.ZS) | [CSV archive](https://api.worldbank.org/v2/en/indicator/SP.POP.65UP.TO.ZS?downloadformat=csv) |
| `SP.DYN.LE00.IN` | [Life expectancy at birth](https://data.worldbank.org/indicator/SP.DYN.LE00.IN) | [CSV archive](https://api.worldbank.org/v2/en/indicator/SP.DYN.LE00.IN?downloadformat=csv) |
| `SP.URB.TOTL.IN.ZS` | [Urban population](https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS) | [CSV archive](https://api.worldbank.org/v2/en/indicator/SP.URB.TOTL.IN.ZS?downloadformat=csv) |

To reconstruct the extract, download and unpack the four indicator archives. Read each `API_*.csv` file after its metadata preamble; keep country codes `BRA`, `CHN`, `DEU`, `IND`, `JPN`, `MEX`, `RUS`, and `ZAF`, and year columns `2010`, `2015`, `2020`, and `2023`. Reshape years into rows, join the indicators on country code and year, and use the column names above. The original downloads contain more countries and years than the prepared file.

The saved extract was retrieved on **17 November 2026**. No missing values were imputed.
[Provenance](data/wdi_provenance.json) records source URLs, selected original values, and SHA-256 checksums.
World Bank downloads may be revised; use the included CSV to reproduce this saved extract exactly.

These eight countries are not a random or representative world sample. Summing populations across different years does not give a single-year total. An unweighted mean of country shares gives every country equal weight; a combined population share requires population weights or sums of the corresponding counts.

Life expectancy at birth is a period life-table measure, not the average age at death in a sample. Derived numbers of older people combine published estimates and are approximate. Country-level associations do not establish causal effects or individual-level relationships. Consult each indicator's documentation for definitions and limitations.

### Adult Income

[Download the prepared CSV](data/adult.data.csv?raw=1), also included at `data/adult.data.csv`.
Original source: [UCI Adult documentation](https://archive.ics.uci.edu/dataset/2/adult) and [dataset ZIP](https://archive.ics.uci.edu/static/public/2/adult.zip).

The prepared file contains **32,561 historical individual records and 15 columns**.
It corresponds to the original `adult.data` file, with a header row and the income category named `salary`.
The original UCI file has no header and includes spaces after delimiters; it is not a direct replacement for the prepared CSV.
Question marks (`?`) denote missing categories. `salary` is an annual income category (`<=50K` or `>50K`), not an exact amount.
Unweighted summaries describe this file; they are not estimates of the current population.

All town examples in the Python and NumPy notebooks are fictional. Their thresholds and assumed growth rates are exercise assumptions, not policy standards or demographic forecasts.

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

## Reference documentation

- [Python introduction](https://docs.python.org/3/tutorial/introduction.html) and [control flow](https://docs.python.org/3/tutorial/controlflow.html).
- [NumPy beginner guide](https://numpy.org/doc/stable/user/absolute_beginners.html).
- [pandas introductory tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html).
- [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html).
- [seaborn scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html) and [barplot](https://seaborn.pydata.org/generated/seaborn.barplot.html).
- [Jupyter notebook basics](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html).
