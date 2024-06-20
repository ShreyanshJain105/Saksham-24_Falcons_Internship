# ==================Handling Null (missing value )========================================#

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
import seaborn as sns

sns.get_dataset_names()


# to load dataset 

data=sns.load_dataset('attention')
data.head()

# for null value 

#data.isnull()
data.isnull().value_counts()

# for read csv file 
df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

data.isnull().value_counts()


# load dataset from dataset file 
pl=sns.load_dataset('planets')
pl.isnull().value_counts()


pl.shape

# for drop value 
pl1=pl.dropna()

pl.shape

pl1.shape

# for changing null value 
my_data=pl.fillna('my value')

my_data

pl.sample(10)

value1=pl['orbital_period'].mean().round(5)

value1

pl.fillna(value1)
pl

# for changing value in original excel file
pl.fillna(value1 , inplace=True )


pl


