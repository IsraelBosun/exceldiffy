# 📊 exceldiffy: Compare Excel Sheets & DataFrames Effortlessly

**exceldiffy** is a Python package for comparing specific columns between two Excel sheets or pandas DataFrames, using composite keys to match rows and highlighting absolute/percentage changes. Whether you’re working in finance, auditing, or general data analysis, it helps you spot changes quickly and export the results to Excel.

---

## 🚀 Features

- 🔍 Compare one or multiple columns between two datasets.
- 🧠 Uses composite keys to accurately match rows.
- 📈 Calculates **absolute** and **percentage** changes for numeric values.
- 💡 Optionally shows **all rows** or just differences.
- 📁 Exports differences to an easy-to-read Excel file — with one sheet per column.
- ✅ Works in **Google Colab**, **Jupyter Notebook**, or your own scripts.
- 😍 Clean display with `display()` for better visual output in notebooks.

---

## 📦 Installation

```bash
pip install exceldiffy
```

## 🧠 How It Works

You initialize the Comparator, pass two DataFrames, and specify:

- `key_columns`: which columns define a "matching row" across datasets (e.g. `['Asset ID']`)
- `compare_columns`: which columns to check for changes (e.g. `['Market Value', 'Rating']`)

### Example

```python
from exceldiffy import Comparator
import pandas as pd

df1 = pd.read_excel("portfolio_jan.xlsx")
df2 = pd.read_excel("portfolio_feb.xlsx")

comp = Comparator()
results = comp.compare_dataframes(
    df1, df2,
    key_columns=["Asset ID"],
    compare_columns=["Market Value", "Rating"]
)

comp.display_comparison(results)
comp.export_to_excel(results, filename="changes_report.xlsx")
```

## 📤 Output Example

Each changed column generates a table like this:

| key    | Market Value_before | Market Value_after | absolute_change | pct_change |
|--------|--------------------|--------------------|-----------------|------------|
| ABC123 | 1,000,000          | 1,200,000          | 200,000         | 20.0%      |
| XYZ789 | 500,000            | 450,000            | -50,000         | -10.0%     |

And you can export all these into Excel with a single line!

## 📁 Excel Export

```python
comp.export_to_excel(results, filename="comparison_results.xlsx")
```

This creates an Excel file with each compared column on a separate sheet, neatly formatted.

✅ In Google Colab? It even triggers a file download automatically!

## ✅ Use Cases

- 🔄 Comparing portfolio snapshots between months
- 🕵️ Spotting data entry or update errors
- 📚 Auditing financial changes across versions
- 📊 Visualizing trends in numeric data fields

## 🧰 Requirements

- pandas
- numpy
- XlsxWriter (automatically installed via pip)

## 🙋‍♂️ Why Use exceldiffy?

Because manual Excel comparisons are painful.

exceldiffy makes it:

- 🔥 Fast
- 😌 Simple
- 💼 Professional
- 💻 Notebook & script-friendly

## 🔧 Advanced Options

- `show_all=True`: show rows even if there's no change (great for audits).
- `top_n`: limit how many top changes to display.
- Handles duplicated composite keys and missing data gracefully.

## 🛠 Maintainer

Built and maintained by Israel Bosun.

## 📄 License

MIT License — use freely, contribute gladly!

## 📬 Feedback or Suggestions?

Open an issue or reach out!
