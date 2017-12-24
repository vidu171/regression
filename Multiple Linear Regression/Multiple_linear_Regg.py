# Importing 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Loading the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values  
y = dataset.iloc[:,-1:].values

# Handeling the missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(X[:,:-1])
X[:,:-1] = imputer.transform(X[:,:-1])

# Encoding the categorial data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,3] = labelencoder_X.fit_transform(X[:,3])
onehotencoder = OneHotEncoder(categorical_features =[3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the data into the Training set and Test Set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Fitting Multiple Linear Regression Model into the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test Set
y_pred = regressor.predict(X_test)

# Plotting the graph for training model with all the variables
#plt.scatter(X_test, y_test, color='red')
#plt.plot(X_test, y_pred, color='blue' )
#plt.title('Startups')
#plt.xlabel('Dependent Variables')
#plt.ylabel('Profit made')
#plt.show()

#Building the optimal model using Backward elemination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50,1)).astype(int), values = X_train, axis=1) #adds an array of ones in the bigginig of the dataset
""" assuming the significance level as 0.05 """
X_opt = X[:, [0 , 1 , 2 ,3 ,4 ,5]]
regressor_OLS = sm.OLS(endog= y, exog= X_opt).fit()
regressor_OLS.summary()
        # The P index of variable 2 ie. X[2] is the highest and is greater than significance level
X_opt = X[:, [0 , 1 ,3 ,4 ,5]]
regressor_OLS = sm.OLS(endog= y, exog= X_opt).fit()
regressor_OLS.summary()

        # The P index of variable 1 ie. X[1] is the highest and is greater than significance level
X_opt = X[:, [0  ,3 ,4 ,5]]
regressor_OLS = sm.OLS(endog= y, exog= X_opt).fit()
regressor_OLS.summary()

        # The P index of variable 2 ie. X[4] is the highest and is greater than significance level
X_opt = X[:, [0  ,3 ,5]]
regressor_OLS = sm.OLS(endog= y, exog= X_opt).fit()
regressor_OLS.summary()

        # The P index of variable 3 ie. X[5] is the highest and is greater than significance level
X_opt = X[:, [0  ,3 ]]
regressor_OLS = sm.OLS(endog= y, exog= X_opt).fit()
regressor_OLS.summary()

# Prediction Using the optimal Solution
optRegressor = LinearRegression()
optRegressor.fit(X_opt, y_train)
y_pred2 = optRegressor.predict(X_test)


