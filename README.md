# Regression Models

Application of Regression models using Python 3


# Linear Regression

Linear Regression Model to understand the relationship between the Profit made by 50 startups and the investments made in diferent sections. The format of the data is as follows.

application are linked below.

| R&D Spend|Administration |Marketing Spend |State |Profit |
|----------|---------------|----------------|------|-------|
165349.2|136897.8|471784.1|New York|192261.83
162597.7|151377.59|443898.53|California|191792.06
153441.51|101145.55|407934.54|Florida|191050.39

#### Training and test set splitting
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
```

### Using The backward Elimination to Build The Model
**Assuming Significance to enter and stay in the model as 0.05**
Recursively Removing the variables with the highest significance Level.
And the result is R&D


# Decision Tree Regression

Decision Tree Regression Model to predict the salary of a future employee of the company based on a dataset containing the salary of different positions.


| Position| Level |Salary |
|----------|---------------|----------------|
Manager | 4 | 80000 |
Country Manager | 5 | 110000
Region Manager|6|150000|

#### Applying thr Decision Tree 
```python
regressor = DecisionTreeRegressor(random_state = 0)
```

#### Graph obtained on 0.01 resolution 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Graph with 0.01 resolution")
