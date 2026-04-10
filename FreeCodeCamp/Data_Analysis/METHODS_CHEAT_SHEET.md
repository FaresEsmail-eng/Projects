# Data Analysis with Python - Cheat Sheet

A comprehensive collection of methods, functions, attributes, and libraries for data analysis in Python.

---

## 1. Pandas (`import pandas as pd`)
Pandas is the core library used for data manipulation and analysis in these projects.

### Data I/O & Initialization
*   `pd.read_csv('file.csv')`: Reads a CSV file into a DataFrame.
    *   `index_col='date'`: Sets a specific column to be the index.
    *   `parse_dates=True`: Automatically parses date columns into Datetime objects.
*   `pd.DataFrame(data)`: Constructs a new DataFrame.
*   `pd.Series(data)`: Constructs a 1D Series (e.g., used to create the years array for sea level predictions).

### Exploration & Information
*   `df.head()`, `df.tail()`: Returns the first/last 5 rows of the DataFrame.
*   `df.info()`: Prints a concise summary of the DataFrame (column data types, missing values, memory usage).
*   `df.describe()`: Generates descriptive statistics (mean, count, min, max, percentiles) for numeric columns.
*   `df.shape`: Returns a tuple representing the dimensionality of the DataFrame `(rows, columns)`.
*   `df.columns`: Returns the column labels.
*   `len(df)`: Returns the number of rows in the DataFrame.
*   `df.copy()`: Creates a deep copy of the DataFrame.

### Handling Missing Data

*   `df.isna()` / `df.isnull()`: Detects missing/NaN values, often chained with `.sum()` to count them (`df.isna().sum()`).
*   `df.dropna()`: Drops rows (or columns with `axis=1`) that contain missing values.
*   `df.fillna(value)`: Fills missing/NaN values with a specified value or method (like forward filling).

### Data Cleaning, Filtering & Boolean Masking
*   **Boolean Indexing**: Filtering rows based on conditions `df[df['Year'] >= 2000]`.
*   **Logical Operators**: `&` (AND), `|` (OR), `~` (NOT). *Example: `(~df['education'].isin(['Bachelors']))`*
*   `df['col'].isin(list)`: Checks if column values are contained in a specified list.
*   `df['col'].quantile(q)`: Returns values at the given quantile (e.g., `0.025` and `0.975` for top/bottom 2.5% filtering).

### Data Manipulation & Reshaping
*   `pd.melt(df, id_vars, value_vars)`: Unpivots a DataFrame from wide to long format (used for the Medical Data Visualizer categorical plot).
*   `df.groupby(['col1', 'col2'])`: Groups DataFrame using a mapper or by a Series of columns.
*   `df.unstack()`: Pivots a level of the (necessarily hierarchical) index labels (used after grouping year and month in the Page View project).
*   `df.reset_index()`: Resets the index of the DataFrame, making the current index a column (useful after grouping or melting).
*   `df.astype(int)`: Casts a pandas object to a specified dtype.
*   `pd.CategoricalDtype(categories=..., ordered=True)`: Creates ordinal/categorical data types, which paired with `.cat.codes` yields numerical codes per category.
*   `df.rename(columns={'oldName':'newName'})`: Renames a specific column label.
*   `df.drop(['colName'], axis=1)`: Drops specified labels from columns (axis=1) or rows (axis=0).
*   `df.apply(lambda row: ..., axis=1)`: Applies a function along an axis of the DataFrame.
*   `df['col'].value_counts()`: Returns a Series containing counts of unique values.
*   `df.groupby(...).size()`: Returns the number of occurrences within each group limit (often used instead of count for categorical summarization).
*   `.get('value')`: Retrieves a value from a Series/Dict by its key.

### Math & Statistics
*   `df.mean()`, `df.min()`, `df.max()`, `df.std()`, `df.var()`, `df.sum()`: Calculates respective statistical metrics over the requested axis.
*   `df.corr()`: Computes the pairwise correlation of columns (used for the heatmap).

### Combining & Sorting Data
*   `pd.concat([df1, df2])`: Appends DataFrames vertically/horizontally. Very common for putting together datasets from multiple files.
*   `pd.merge(df1, df2, on='key_column')`: Joins two DataFrames like a SQL JOIN (inner, outer, left, right).
*   `df.sort_values(by='column_name', ascending=False)`: Sorts the DataFrame by a specified column.

### Datetime Operations
*   `df.index.month_name()`: Gets the name of the month from a DatetimeIndex.
*   `df.index.year`: Extracts the year from a DatetimeIndex.
*   `d.strftime('%b')`: Formats a datetime object into a shortened month string ('Jan', 'Feb', etc.).

---

## 2. NumPy (`import numpy as np`)
Used mostly in the Mean-Variance-Standard Deviation Calculator and to generate the heatmap mask.

*   `np.array(list)`: Converts a Python list into a NumPy array.
*   `arr.reshape(rows, cols)`: Changes the shape of an array without changing its data (e.g., `.reshape(3, 3)`).
*   `arr.tolist()`: Converts a NumPy array back into a standard Python list.
*   **Math Functions**: `np.mean()`, `np.var()`, `np.std()`, `np.max()`, `np.min()`, `np.sum()`.
    *   *Note: Using `axis=0` calculates along columns, `axis=1` calculates along rows.*
*   `np.ones_like(arr, dtype=bool)`: Returns an array of ones with the same shape and type as a given array.
*   `np.triu(arr)`: Upper triangle of an array. Used together with `np.ones_like` to create a mask that hides the upper half of the correlation matrix in the Medical Data Visualizer.

---

## 3. Matplotlib (`import matplotlib.pyplot as plt`)
The fundamental plotting library underlying Seaborn and basic Pandas plotting.

### Figure & Axes
*   `fig, ax = plt.subplots(figsize=(width, height), nrows=..., ncols=...)`: Creates a figure and a set of subplots.
*   `plt.gca()`: Gets the current Axes instance.
*   `fig.savefig('filename.png')`: Saves the current figure to a file.

### Plotting
*   `plt.plot(x, y, color, label)`: Plots lines and/or markers to the Axes (used for the line of best fit).
*   `plt.scatter(x, y)`: Makes a scatter plot of x vs y.
*   `df.plot(kind='bar', ...)`: Uses pandas wrapper around matplotlib to quickly create a bar chart.

### Labels & Configuration
*   `plt.title('...')`, `plt.xlabel('...')`, `plt.ylabel('...')`: Sets the title and axis labels for the current axes.
*   `ax.set(xlabel=..., ylabel=..., title=...)`: Alternative way to set labels when working directly with an axis object.
*   `plt.legend()`: Places a legend on the Axes.

---

## 4. Seaborn (`import seaborn as sns`)
Used for generating attractive statistical graphics.

### Configuration
*   `sns.set_theme(style='darkgrid')`: Changes the visual theme of the plots.
*   `sns.color_palette(...)`: Configures the color palette.

### Plot Types
*   `sns.catplot(data=..., x=..., y=..., hue=..., col=..., kind='bar')`: Figure-level interface for drawing categorical plots onto a FacetGrid.
*   `sns.heatmap(data=..., mask=..., annot=True, fmt='.1f')`: Plots rectangular data as a color-encoded matrix.
    *   `annot=True`: Writes the data value in each cell.
    *   `fmt='.1f'`: Formats the annotations to one decimal place.
*   `sns.lineplot(data=..., x=..., y=..., ax=...)`: Draws a line plot with possibility of several semantic groupings.
*   `sns.barplot(data=..., x=..., y=..., hue=...)`: Shows point estimates and confidence intervals as rectangular bars.
*   `sns.boxplot(data=..., x=..., y=..., ax=..., order=...)`: Draws a box plot to show distributions with respect to categories.

### Additional Seaborn Utilities (observed in Testing.ipynb)
*   `sns.scatterplot(data, x='col', y='col', hue=..., size=..., style=...)`: Figure-level scatter with semantic mappings.
*   `sns.relplot(..., kind='scatter'|'line')`: High-level interface for relational plots that can create multiple subplots with `col`/`row` facets.
*   `sns.load_dataset('name')`: Loads example datasets bundled with Seaborn (e.g., `tips`, `iris`, `dowjones`, `titanic`).
*   `sns.displot(data, x='col', kind='hist')`: High-level distribution plot; wrapper around `histplot` and `kdeplot`.
*   `sns.kdeplot(data, x='col', y='col', hue=..., fill=True)`: Kernel density estimation plot for continuous variables.
*   `sns.ecdfplot(data, x='col')`: Empirical cumulative distribution function plot.
*   `sns.rugplot(data, x='col')`: Adds small vertical lines (rugs) at each data point on the x-axis.
*   `sns.catplot(..., kind='strip'|'box'|'bar')`: Figure-level categorical plotting (strip, box, bar, violin, etc.).
*   `sns.violinplot(data, x='col', y='col')`: Combines a kernel density estimate with a boxplot-like summary.
*   `sns.pairplot(data)`: Plots pairwise relationships in a dataset; useful for a quick EDA.
*   `sns.jointplot(data, x='col', y='col')`: Shows bivariate distributions (scatter + marginal distributions).
*   `sns.clustermap(data)`: Shows hierarchical clustering with a heatmap for rows/columns.

---

## 5. SciPy (`from scipy.stats import linregress`)
Used for advanced statistical operations in the Sea Level Predictor project.

*   `res = linregress(x_array, y_array)`: Calculates a linear least-squares regression for two sets of measurements.
*   **Result Attributes**: 
    *   `res.slope`: Slope of the regression line ($m$).
    *   `res.intercept`: Intercept of the regression line ($b$).
    *   *Equation of the line of best fit: `y = (res.slope * x) + res.intercept`*

---

## 6. Built-in Python Essentials
*   **Dictionaries**: Mapped statistics in the mean-variance calculator (`{'mean': [...], 'variance': [...]}`).
*   **List Comprehensions**: `[d.year for d in df_box.date]` (Extracting attributes efficiently in one line).
*   `range(start, stop)`: Generates a sequence of numbers (used to create the future years from 2000 to 2050).

### Pandas Helpers & Shortcuts used in Testing.ipynb
*   `df.info()`: See non-null counts and dtypes (handy for debugging column parsing issues).
*   `df.describe(include='all')`: Describe both numeric and non-numeric columns.
*   `df.drop(['col'], axis=1)`: Remove columns.
*   `df.sort_values(by='col')`: Sorting before plotting or aggregating.
*   `df.groupby('col').size()` : Counts per group - used to compute totals for categorical plots.

### Quick tips extracted from your notebook
*   Use `sns.set_theme(style='darkgrid')` at the top of the notebook to apply a consistent look across all plots.
*   Keep a single `plt.figure()` or `fig, ax = plt.subplots()` per figure to avoid overlapping figures when iteratively plotting in notebooks.
*   Use `%matplotlib inline` (or the appropriate backend) when working in notebooks to render images inline.
