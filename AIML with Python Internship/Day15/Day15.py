# EDA(Exploratry data analysis)


# EDA univeriate analysis

import seaborn as sns

sns.get_dataset_names()

tit=sns.load_dataset('titanic')

tit.shape
# tit.head()

# tit.tail()

tit.sample(10)


 # what is the data type of each and every column

tit.info()

tit.info()


tit.shape


tit.describe()


tit.duplicated()

tit[886: 887 ]


tit[887:]


tit.info()


#tit.corr()['pclass']

tit.head()


sns.histplot(tit['survived'])
tit['survived'].value_counts()


tit['who'].value_counts()



#tit['parch']
sns.countplot(tit['who'])
# sns.countplot(x='who')


# numerical data ===> continuous

#min , max ,mean

# numerical ==> univarite EDA

import matplotlib.pyplot as plt

plt.hist(tit['age'])
plt.show()



tit.describe()


# charge pay range (0-70)
sns.boxplot(x='fare' , data=tit)
plt.show()


sns.boxplot(tit['age'])

tit['age'].min()

tit['age'].max()

tit['age'].std()

tit['age'].skew()


 # =============================bivariate analysis===================


 tips=sns.load_dataset('tips')
tips.head()


flight=sns.load_dataset('flights')
flight.head()

iris=sns.load_dataset('iris')
iris.head()

iris.sample(10)



# scatter ( numerical -numerical)
# relationship found

# bivariate
sns.scatterplot(x='total_bill' , y='tip' , data=tips)


# multiveriate analysis

sns.scatterplot(x='total_bill' , y='tip' ,hue='sex' ,data=tips)



sns.scatterplot(x='total_bill' , y='tip' ,hue='sex' , style='smoker' ,data=tips)

# multivariate analysis



tips.sample(10)

# hue=> color , category differentiate
# style ==> difference shape according differentiate
# size ==>  size according differentriate


sns.scatterplot(x='total_bill' , y='tip' ,hue='sex' ,style='smoker', size='size' ,data=tips)


tit.head()

#tit.info()

tit.sample(10)
# bar plot==>[numerical , categorical]
sns.barplot(x='pclass',y='age',data=tit)
plt.show()



sns.barplot(x='pclass',y='fare', hue='sex' ,data=tit)
plt.show()


sns.boxplot(x='sex', y='age' , hue='sex' ,data=tit)


# HeatMap [ categorical , categorical]
tit.head()



import pandas as pd

pd.crosstab(tit['pclass'] , tit['survived'])



sns.heatmap(pd.crosstab(tit['pclass'] , tit['survived']))

# relationship between two categories using heatmap


# tit.groupby('pclass').mean()['survived']*100

# clusterMAp ( categorical - categorical)

pd.crosstab(tit['pclass'] , tit['survived'])

