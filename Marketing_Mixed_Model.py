#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 22:18:44 2021

@author: josephthomas
"""

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/josephthomas/Documents/Hallam/MMM_Example/Advertising 2.csv')

########## EDA ##########

########## Correlation Map ##########
corr = df.corr()
sns.heatmap(
    corr, 
    xticklabels = corr.columns, 
    yticklabels = corr.columns, 
    annot = True, 
    cmap = sns.diverging_palette(220, 20, as_cmap=True)
)
# Shows strong correlation between TV and sales (0.78), 
# a moderate correlation between radio and sales (0.58), 
# and a weak correlation between newspaper and sales (0.23)

########## Pairplot ##########
sns.pairplot(df)
# Can see some consistency between our pair plot and our original correlation matrix

########## Feature Importance ##########
# Setting X and y variables
X = df.loc[:, df.columns != 'sales']
y = df['sales']

# Building Random Forest model
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=0)
model = RandomForestRegressor(random_state=1)
model.fit(X_train, y_train)
pred = model.predict(X_test)

# Visualizing Feature Importance
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(25).plot(kind='barh',figsize=(10,10))
#Supports past EDA:  TV is the most important feature, followed by radio, leaving newspaper last

########## Contribution Plot ##########
from sklearn.linear_model import LinearRegression

X = df.drop(columns=['sales'])
y = df['sales']

lr = LinearRegression()
lr.fit(X, y)

weights = pd.Series(
    lr.coef_,
    index=X.columns
)
base = lr.intercept_
unadj_contributions = X.mul(weights).assign(Base=base)
adj_contributions = (unadj_contributions
                     .div(unadj_contributions.sum(axis=1), axis=0)
                     .mul(y, axis=0)
                    ) # contains all contributions for each day
ax = (adj_contributions[['TV', 'radio', 'newspaper']]
      .plot.area(
          figsize=(16, 10),
          linewidth=1,
          title='Predicted Sales and Breakdown',
          ylabel='sales',
          xlabel='Date')
     )
handles, labels = ax.get_legend_handles_labels()
ax.legend(
    handles[::-1], labels[::-1],
    title='Channels', loc="center left",
    bbox_to_anchor=(1.01, 0.5)
)

###################################################################################################

########## Constructing Marketing Mix Model (OLS) ##########

import statsmodels.formula.api as sm
model = sm.ols(formula="sales~TV+radio+newspaper", data=df).fit()
print(model.summary())

########## Plot Actual vs Predicted Values ##########

from matplotlib.pyplot import figure

y_pred = model.predict()
labels = df['sales']
df_temp = pd.DataFrame({'Actual': labels, 'Predicted':y_pred})
df_temp.head()

figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
y1 = df_temp['Actual']
y2 = df_temp['Predicted']

plt.plot(y1, label = 'Actual')
plt.plot(y2, label = 'Predicted')
plt.legend()
plt.show()




























