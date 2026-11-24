# Cultural domains and policy evaluation

Use Python to organise structured qualitative material, compare concepts, and examine a policy using difference in differences. The exercises build on pandas, NumPy, plotting, and simple regression.

## Materials

| Material | Contents |
| --- | --- |
| [Presentation](Week3_Cultural_Domains_Policy_Evaluation.pdf) | Anthropological concepts, free lists and pile sorts, worked examples, counterfactuals, DiD, and project requirements |
| [Environment check](00_setup_check.ipynb) | Package, file, and plotting diagnostics |
| [Cultural domains](01_cultural_domains_student.ipynb) | Functions, text cleaning, reshaping, frequency, Smith's S, joins, pile sorting, and a heatmap |
| [Policy evaluation](02_policy_evaluation_student.ipynb) | FTE employment, sample selection, manual DiD, counterfactual plots, regression, and sensitivity |
| [Optional matching](03_matching_optional_student.ipynb) | Propensity scores, overlap, explicit caliper matching, balance, and estimands |
| [Data documentation](data/README.md) | Definitions, original downloads, synthetic-data descriptions, and provenance |
| [Student package](student_materials.zip) | All exercises, public slides, setup instructions, and the five input CSVs |

Exercise code cells are intentionally empty. Write code and interpretations in your own copy. Each notebook starts independently; execute its cells in order. The matching notebook is an optional extension, not a requirement for the research project.

## Install and open

Download the student ZIP and extract it completely, or clone the course repository. Keep the notebooks alongside their `data` folder.

From this folder, with your Python environment active:

```bash
python -m pip install -r requirements.txt
python -m notebook
```

If Jupyter is already open, run `%pip install -r requirements.txt` in a temporary cell in its active kernel, then restart the kernel. Run [00_setup_check.ipynb](00_setup_check.ipynb). Full platform-specific instructions and troubleshooting are in [SETUP_EN.txt](SETUP_EN.txt).

The main analysis libraries are the same as Week 2. No RLMS download, external account, API key, or large archive is required for these exercises. All inputs are included and work offline after installation.

## Data and interpretation

The cultural-domain data are **fully synthetic examples about support for older residents**. They demonstrate how free lists and pile sorts can be represented and analysed. They contain no real participants, and their patterns are not findings about age groups, service needs, or public attitudes. Record the original text and coding decisions; numerical summaries complement interpretation rather than replacing it.

The policy notebook uses a documented extract of the **Card–Krueger New Jersey–Pennsylvania restaurant survey**. The input retains all 410 source records and employment components, so sample construction is part of the exercise. State coding is **1 = New Jersey, 0 = Pennsylvania**. The source and direct download are on [David Card's data page](https://davidcard.berkeley.edu/data_sets), with the [original archive](https://davidcard.berkeley.edu/data_sets/njmin.zip), [provider README](https://davidcard.berkeley.edu/readme/njmin-readme.txt), and [research article](https://davidcard.berkeley.edu/papers/njmin-aer.pdf).

DiD is first a defined numerical contrast. A causal interpretation additionally requires a defensible comparison, including parallel untreated trends. This extract has one pre-policy wave and two states: it cannot test pre-trends or support ordinary many-state cluster inference. The exercise displays regression coefficients without treating ordinary OLS p-values as policy evidence. It does not reproduce every specification or standard error in the article.

The optional matching data are also **fully synthetic**. Only pretreatment variables enter the score model. Matching is 1:1 with replacement, restricted to controls, with an explicitly enforced caliper. Report overlap, covariate balance, control reuse, and treated coverage. Dropping unmatched treated records changes the population described; good measured balance does not establish that unmeasured confounding is absent.

File definitions, preparation steps, and SHA-256 checksums are in [data/README.md](data/README.md) and [data/provenance.json](data/provenance.json).

## Connect the method to your research question

A qualitative project may use Python to organise documents or extracts, record a human-designed codebook, compare coded material, and preserve an audit trail. Word counts alone do not establish meaning. A quantitative project may use descriptive comparisons or a model that you can explain and justify. Neither DiD nor matching is compulsory.

The [final project requirements](https://github.com/SergeevVladislav/HSE_PopDev_Mentors_Seminar_Python_Fall_2025/blob/main/01_sem/FINAL_PROJECT.md) remain: a focused original question, literature review, justified method, Python analysis, and a self-written article of at most **15 pages in total**. The project determines **100%** of the grade. Register the topic by **24 November 2026**; submit the paper and code by **25 December 2026** in a public GitHub repository and record its link in the course registration sheet.

LLM help with Python code is allowed when you understand, verify, and disclose it. The article, literature review, substantive interpretation, and qualitative coding decisions must be your own. Do not use an LLM to write, rewrite, translate, or polish the article. Do not plagiarise or invent evidence and sources.

## Instructions for an assistant helping with setup

1. Work in `03_sem/week3_ready` or the extracted `popdev_week3` folder. Preserve the learner's existing work.
2. Identify the active Jupyter interpreter using `import sys; print(sys.executable)`. Install `requirements.txt` in that interpreter and restart its kernel.
3. Confirm that the five CSV files listed in `data/provenance.json` are present. Check the working directory before modifying paths.
4. Run the diagnostic notebook and report actual failures. Student exercise cells are intentionally empty; do not treat this as an installation error.
5. Keep generated output in `outputs/`. Do not overwrite the input data or silently change the sample, coding rules, state indicator, or matching design.
6. Distinguish synthetic inputs from the real survey. Keep the data definitions and source attribution with any reused outputs.
7. Help with code and its verification; leave the research article and substantive research decisions to the student.

## References and Python documentation

- [Borgatti: elicitation techniques for cultural domain analysis](https://qualquant.org/wp-content/uploads/text/1998%20Borgatti115%E2%80%93151.pdf)
- [Borgatti: cultural domain analysis](https://qualquant.org/wp-content/uploads/cda/Borgatti%201994%20Cultural%20Domain%20Analysis.pdf)
- [Smith and Borgatti: salience and accuracy](https://qualquant.org/wp-content/uploads/cda/%2Asmith%20and%20borgatti%201997%20salience%20and%20accuracy.pdf)
- [AnthroTools guide](https://anthrotools.wordpress.com/wp-content/uploads/2016/05/anthrotools_guide.pdf)
- [Card and Krueger (1994)](https://davidcard.berkeley.edu/papers/njmin-aer.pdf)
- [Cunningham: difference-in-differences fundamentals](https://mixtape.scunning.com/09-difference_in_differences)
- [pandas: melt](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html) and [merge validation](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)
- [statsmodels: formula examples](https://www.statsmodels.org/stable/example_formulas.html)
- [MatchIt authors: matching methods and target populations](https://kosukeimai.github.io/MatchIt/articles/matching-methods.html)

Course contact: [vsergeevmsu@gmail.com](mailto:vsergeevmsu@gmail.com).
