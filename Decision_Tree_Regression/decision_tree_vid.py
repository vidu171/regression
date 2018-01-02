#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 11:54:08 2018

@author: vidu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the data set
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2:3].values

#fitting Decision tree regression to the dataset
from sklearn.tree import DecisionTreeRegressor 
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)

#predicing a new Result
y_pred = regressor.predict(6.5)

#visualising the Decision Tree Regression results
X_grid = np.arange(min(X), max (X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y , color ='red')
plt.plot(X_grid, regressor.predict(X_grid), color ='blue')
plt.show()

