# # Day 16 data analsis (eda ) mini project



import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('file.csv')
print(df.head())


print(df.head())  # Display the first few rows
print(df.shape)  # Get data frame dimensions (rows, columns)
print(df.info())  # View data types and missing values



print(df['Year'].describe())  # Replace 'column_name' with the actual column

# univariate

sns.histplot(df['Year'])
plt.show()


print(df['Industry_code_NZSIOC'].value_counts())


# bivariate 

sns.scatterplot(x='Year', y='Variable_code', data=df)
plt.show()


sns.barplot(x='Year', y='Industry_aggregation_NZSIOC', data=df)
plt.show()


sns.boxplot(x='Year', y='Industry_code_NZSIOC', data=df)
plt.show()


# multivariate 

sns.scatterplot(x='Year', y='Industry_aggregation_NZSIOC', hue='Variable_code', data=df)
plt.show()

sns.scatterplot(x='Value', y='Variable_name', hue='Units', style='Variable_category', data=df)
plt.show()



contingency_table = pd.crosstab(df['Units'], df['Value'])
sns.heatmap(contingency_table, annot=True)
plt.show()



# missing value
print(df.isnull().sum())










