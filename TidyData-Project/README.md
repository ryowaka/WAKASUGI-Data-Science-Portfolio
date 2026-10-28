# 📊 Tidy Data Project

## Overview

In this project, I used Python and pandas to clean and visualize federal R&D budget data. Tidy data means that each variable has its own column, each observation has its own row, and different types of observations are stored in separate tables.

I wanted to compare R&D budgets across departments and see how federal spending changed over time.

## Dataset

I used the [Federal R&D Spending dataset](https://github.com/rfordatascience/tidytuesday/blob/main/data/2019/2019-02-12/fed_r_d_spending.csv) from TidyTuesday.

The dataset includes R&D budgets for different departments, federal spending, and GDP from 1976 to 2017.

## What I Did

I separated the data into department and national data. I used `drop_duplicates()`, `pd.melt()`, `str.split()`, and `str.replace()` to organize the data.

I also made a pivot table to calculate average R&D budgets and created two graphs.

- A bar chart comparing the top five departments by average R&D budget.
- A line chart showing how federal spending changed over time.

## How to Run

1. Download the repository and open it in VS Code.
2. Install pandas and matplotlib using `pip install pandas matplotlib`.
3. Open `tidy_data.ipynb` in VS Code with the Jupyter extension.
4. Run the notebook.

The CSV file is in the `data` folder.

## References

- [Federal R&D Spending Dataset](https://github.com/rfordatascience/tidytuesday/blob/main/data/2019/2019-02-12/fed_r_d_spending.csv)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Tidy Data Paper](https://vita.had.co.nz/papers/tidy-data.pdf)
