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
