
# Fruit Sales Data Analysis

[![Python Tests](https://github.com/tabner0320/fruit.csv/actions/workflows/python-tests.yml/badge.svg)](https://github.com/tabner0320/fruit.csv/actions/workflows/python-tests.yml)

A Python data-analysis project that uses **pandas** and **Matplotlib** to analyze fruit sales, calculate sales growth, and generate visualizations.

## Project Overview

This project analyzes apple and banana sales from 2017 and 2018. It demonstrates CSV generation, DataFrame manipulation, data aggregation, percentage-growth calculations, data visualization, and automated testing.

## Features

- Create and export a CSV dataset using pandas.
- Calculate yearly sales totals.
- Calculate total sales for each fruit.
- Calculate percentage growth between 2017 and 2018.
- Generate two Matplotlib visualizations.
- Run automated tests with pytest.
- Use GitHub Actions for continuous integration.

## Technologies Used

- Python 3.13
- pandas
- Matplotlib
- pytest
- CSV
- Git and GitHub
- GitHub Actions

## Sales Data

| Year | Apples | Bananas |
|---|---:|---:|
| 2017 | 35 | 21 |
| 2018 | 41 | 34 |

## Analysis Results

| Metric | Apples | Bananas |
|---|---:|---:|
| Total sales | 76 | 55 |
| Growth (2017–2018) | 17.14% | 61.90% |

Total sales increased from **56 in 2017** to **75 in 2018**.

Bananas experienced higher percentage growth, while apples had higher total sales.

## Data Visualizations

### Fruit Sales Comparison

![Fruit Sales Comparison](fruit-sales-comparison.png)

### Fruit Sales Growth

![Fruit Sales Growth](fruit-sales-growth.png)

## Project Structure

```text
fruit.csv/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── .gitignore
├── README.md
├── analysis.py
├── fruit.csv
├── fruit-sales-comparison.png
├── fruit-sales-growth.png
├── requirements.txt
└── test_analysis.py
```

## Installation

Install the required Python packages:

```bash
python -m pip install -r requirements.txt
```

## How to Run

Run the analysis:

```bash
python analysis.py
```

The script generates:

- `fruit.csv`
- `fruit-sales-comparison.png`
- `fruit-sales-growth.png`

## Automated Testing

The project includes five automated pytest tests.

| Test | Description |
|---|---|
| `test_yearly_sales_totals` | Verifies yearly sales totals |
| `test_fruit_sales_totals` | Verifies totals for each fruit |
| `test_sales_growth` | Verifies percentage-growth calculations |
| `test_yearly_totals_with_empty_data` | Tests an empty sales dataset |
| `test_sales_growth_with_decreasing_sales` | Tests negative growth when sales decline |

### Run Tests

```bash
python -m pytest -v
```

### Latest Verified Results

**5 tests passed, 0 failed.**

The tests cover normal sales calculations, empty datasets, and declining sales.

## Continuous Integration

GitHub Actions automatically runs pytest when changes are pushed to configured branches or when pull requests target `main`.

The workflow:

1. Checks out the repository.
2. Sets up Python 3.13.
3. Installs project dependencies.
4. Runs the pytest test suite.

[View GitHub Actions Workflow](https://github.com/tabner0320/fruit.csv/actions/workflows/python-tests.yml)

## Skills Demonstrated

Python programming, pandas DataFrames, CSV processing, data aggregation, percentage-growth calculations, Matplotlib visualization, automated testing with pytest, Git, GitHub, and continuous integration using GitHub Actions.

## Repository

[View Fruit Sales Data Analysis on GitHub](https://github.com/tabner0320/fruit.csv)
