import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv('cleaned_facebook_liverpool.csv')

# EDA :-

# 1) INFO
print(df.info())

# 2) DESCRIBE 
print(df.describe())

# 3) Find Unique values
print(df.nunique())

# 4) NULL z

print(df.isnull().sum())

# 5) datatypes
print(df.dtypes)

# 6) Correlation 
print(df.corr())

# 7) Mode
print(df['no. of comments'].mode())

print(df.head())

# VIZUALIZATION

# 1) HEATMAP

# print(sns.heatmap(df.corr()))

# 2) BOXPLOT
# print(sns.boxplot(x=df["no. of likes"]))

# 3) LINEPLOT 
# print(sns.lineplot(x=df["no. of likes"],y=df["date"]))

# 4) BARPLOT

# print(sns.barplot(x=df["no. of comments"],y=df["date"]))

# 5) HISTOGRAM
# print(sns.histplot(x=df["no. of likes"]))

# 6) VIOLIN & BOXENPLOT
# print(sns.violinplot(x=df["no. of likes"]))






















