# -*- coding: utf-8 -*-
"""housing_production_2005-present.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gDoEEk0ancLZs9Bxg-NOV8XKdjzcF895

Import Libraries
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""Upload and Read the Dataset"""

from google.colab import files
uploaded = files.upload()

"""Load the csv"""

df = pd.read_csv("housing_production_2005-present.csv")
df.head()

"""Understand the Data"""

df.info()
df.describe()
df.columns
df.isnull().sum()

"""Total Net Units Issued Per Year"""

df['issued_date'] = pd.to_datetime(df['issued_date'], errors='coerce')
df['Year'] = df['issued_date'].dt.year

df.groupby('Year')['net_units'].sum().plot(kind='bar', color='lightblue')
plt.title("Net Units Issued by Year")
plt.xlabel("Year")
plt.ylabel("Net Units")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

"""Pie Chart of Permit Types"""

df['permit_type'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(6,6), startangle=90)
plt.title("Distribution of Permit Types")
plt.ylabel("")  # hides the y-axis label
plt.show()

"""Bar Plot of Affordable Units vs Market Rate Units"""

df[['affordable_units', 'market_rate_units']].sum().plot(kind='bar', color=['green', 'orange'])
plt.title("Total Affordable vs Market Rate Units")
plt.ylabel("Units")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

"""DATA CLEANING

Remove Duplicates
"""

df = df.drop_duplicates()

"""Handle Missing Values"""

df.isnull().sum()

"""DATA NORMALIZATION"""

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

cols_to_normalize = ['net_units', 'affordable_units', 'market_rate_units']
df[cols_to_normalize] = scaler.fit_transform(df[cols_to_normalize])

df[cols_to_normalize].head()