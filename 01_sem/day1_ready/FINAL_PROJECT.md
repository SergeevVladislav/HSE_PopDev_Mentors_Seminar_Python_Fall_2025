# Final research project — Population and Development

Produce a small, original study connected to demography, population and development, or public administration. Review the relevant literature, justify your method, and carry out a **qualitative or quantitative analysis using Python**.

The research project determines **100% of the final course grade**.

| Requirement | What to submit |
|---|---|
| Article | A self-written research paper in PDF format, **no more than 15 pages in total**. |
| Analysis | Python notebooks or scripts that document the analysis and reproduce its reported outputs. |
| Publication | The article and code in your own **public GitHub repository**. |
| Registration | Your research topic and public repository URL in your row of the course Google Sheet. |
| Topic deadline | **24 November 2026**. |
| Final project deadline | **25 December 2026**. |

## 1. Choose an original and manageable question

Aim for a focused study that can be completed in about one month. A modest contribution is sufficient: a comparison of particular places, a different period, a carefully selected set of documents, or a small extension of an existing study.

Define one main question, its population or cases, the period, and the evidence you need. Check that you can access the data before committing to the topic. A focused descriptive or qualitative study is suitable when its method answers the question.

Your work must include your own research decisions and analysis. Reproducing a classroom notebook or copying an existing paper with a different title is not an original project. A replication can be useful if you explain what you reproduce, cite it, and add a clear extension or comparison.

Examples of a feasible scope:

| Approach | Possible question | A manageable design |
|---|---|---|
| Quantitative demography | How do changes in older population shares compare with changes in older population counts? | Select a small set of countries and years; justify the selection, calculate indicators, and compare trends. |
| Quantitative public policy | How does a selected service or development indicator vary across a few comparable places? | Define comparable units and a common period; check missingness and use appropriate summaries or a simple model. |
| Qualitative policy analysis | How do selected local policy documents describe support for an ageing population? | Select a small corpus, define a coding scheme, read and code the documents, and compare themes with supporting extracts. |
| Qualitative case comparison | How is the same public service framed in documents from different institutions? | Explain case selection, document definitions and coding decisions, and compare similarities and differences. |

These are examples of scope, not assigned topics. Choose your own question, evidence, and comparison. For a document study, a small corpus such as 6–12 documents may be feasible; this is a planning suggestion, not a required sample size.

## 2. Conduct a literature review

Read relevant academic sources and explain how your question relates to existing research. A working target is **5–10 relevant academic sources**, supplemented by data documentation or policy documents where needed. Source relevance and careful reading matter more than reaching a large number.

The review should:

- Define the main concepts and explain relevant findings.
- Compare approaches, methods, and disagreements across studies.
- Identify the specific issue or comparison your project addresses.
- Explain how the literature informs your question and method.

Write a synthesis in your own words. Cite ideas and findings, not only direct quotations. Clearly mark quoted text and give its source. Read and verify the sources you cite; do not use invented references or an LLM-generated literature review.

## 3. Choose and justify a method

Explain why the method fits the question and the available evidence. Describe the unit of observation, case or sample selection, period, variables or coding categories, and limitations.

### Quantitative analysis

Suitable options include descriptive statistics, group comparisons, time trends, associations, or a simple statistical model that you understand and can justify. Check data types, missing values, duplicate keys, units, and denominators. State relevant assumptions and distinguish descriptive or associational results from causal claims.

Use Python to load and prepare the data, perform the analysis, and produce the reported tables and figures. A more complex model does not automatically make a better project.

### Qualitative analysis

Suitable options include thematic analysis, qualitative content analysis, or a focused comparison of cases or documents. Explain how you selected the material and developed the coding scheme. Read the material yourself, record coding decisions, and support your interpretation with identifiable evidence and accurately attributed extracts.

Python must support the analysis in a meaningful way. For example, use it to organise document metadata and extracts, maintain a coding table, compare coded themes across cases, or create an audit trail and summary figures. Explain what the Python steps contribute to the method. Word counts alone do not establish the meaning or importance of a theme.

## 4. Write the article yourself

The **entire PDF must fit within 15 pages**, including the title page if used, abstract, tables, figures, references, and any appendices. Put the code in GitHub rather than using pages for long code listings. Keep the text, tables, and figures readable.

Recommended structure:

1. **Title and short abstract:** question, evidence, method, and main finding.
2. **Introduction:** the question, its relevance, and the scope of the study.
3. **Literature review:** relevant research and the place of your contribution.
4. **Data or materials:** source, coverage, observational unit or cases, and limitations.
5. **Method:** analytical choices, assumptions, and procedures.
6. **Results:** findings supported by the analysis, with useful tables, figures, or extracts.
7. **Discussion and conclusion:** answer to the question, limitations, and implications.
8. **References.**

You may combine closely related sections if that makes the argument clearer. Every table or figure should have a title, necessary units, a source, and an explanation in the article. Reported numbers and outputs must agree with the Python analysis.

## 5. LLM use and academic integrity

| Activity | Rule |
|---|---|
| Writing the article, including the abstract and literature review | **No LLM use.** Write the text yourself. |
| Rewriting, paraphrasing, translating, or polishing article text with an LLM | **Not permitted.** This also applies to figure captions and substantive written interpretations. |
| Drafting or debugging Python code with an LLM | **Permitted.** You remain responsible for understanding and checking the code. |
| Explaining Python syntax or a programming error with an LLM | **Permitted as coding assistance.** Verify the explanation and test the resulting code. |
| Generating references, findings, quotations, or the article's interpretation with an LLM | **Not permitted.** Use verifiable sources and your own analysis. |
| Borrowing ideas, text, data, figures, or code | Cite the source; mark quotations and respect applicable reuse conditions. Present only your own work as your own. |

Plagiarism, fabricated evidence, and fabricated references are not acceptable. A citation does not turn copied or LLM-written article prose into your own writing.

If you use an LLM for code, include a short disclosure in the repository README: the tool used, what coding tasks it helped with, the relevant files, and how you checked the result. If you did not use one, state that. Do not include confidential inputs or access credentials in a disclosure.

For qualitative work, make and justify your own coding and interpretation decisions. Permission to obtain help with Python code is not permission to replace the research interpretation or article with LLM output.

## 6. Publish the paper and code on GitHub

### Create an account and a public repository

1. [Create a GitHub account](https://github.com/signup) if needed and verify your email address.
2. Open [New repository](https://github.com/new). Choose your account as owner and give the project a meaningful name.
3. Select **Public**, add a **README**, and create the repository.
4. On the repository page, use **Add file → Upload files** to add your article, notebooks or scripts, and supporting files. Review the files and save the upload with a short commit message.
5. Open the repository URL while signed out, or in a private browser window, and check that the article and code are accessible.

Official instructions: [create a repository](https://docs.github.com/en/get-started/start-your-journey/creating-a-repository-for-your-project-on-github), [upload files](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).

A suitable repository structure is:

```text
my-research-project/
├── README.md
├── paper.pdf
├── requirements.txt
├── notebooks/
│   └── analysis.ipynb
├── data/
│   └── README.md
└── outputs/
    ├── figures/
    └── tables/
```

The README should describe the question, data or materials, method, file structure, installation and run instructions, and any LLM assistance with code. Record the Python environment and required packages. Explain how to reproduce each main result. A `.py` script is also acceptable when its execution steps are documented.

Include data that you are allowed to redistribute, or provide precise source links, retrieval instructions, and the selection used. For qualitative analysis, document the corpus, codebook, and coding table. Keep private participant information, access credentials, and the class roster out of public repositories.

Restart the notebook kernel and run the completed analysis from the beginning. Check that another person can follow the README, access the documented inputs, and connect the article's findings to the code.

## 7. Register the topic and repository

Use the course Google Sheet for topic registration. In your own row, fill in:

- **Research topic:** a focused title or question that identifies the intended comparison.
- **Public GitHub repository:** the full URL in the form `https://github.com/username/repository`.

Register your topic by **24 November 2026**. Add the repository URL when you create it; the initial repository can contain a short project README. The finished paper, code, and correct public repository URL must be available by **25 December 2026**. Keep the same URL updated as the project develops. Edit only your own topic and repository cells.

The article and Python files belong in GitHub. The Google Sheet records the topic and repository link; it is not a second location for uploading the article. Do not copy the course student list into GitHub.

## 8. Final checks

- The question is focused, relevant, and feasible, with a modest original contribution.
- The literature review compares verified sources and motivates the study.
- The method is appropriate, explained, and carried out using Python.
- Claims are supported by the results and acknowledge limitations.
- The article is self-written, correctly cited, and no longer than 15 pages in total.
- The public repository contains the final article, code, and reproduction instructions.
- Any LLM help with code is disclosed; the article contains no LLM-generated or LLM-rewritten text.
- The Google Sheet contains the topic and a working public repository URL.

These are the dimensions used to assess the research project, not additional graded assignments or a new weighted grading formula.

Course contact: [vsergeevmsu@gmail.com](mailto:vsergeevmsu@gmail.com).
