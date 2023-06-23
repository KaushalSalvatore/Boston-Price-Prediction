## Boston Price Prediction Using machine learning algorithm

This is machine learning web app that use to predict Boston house price accroding to given paramenter in data set.

#### Data set
```bash
    from sklearn.datasets import load_boston
```

#### Data Set Characteristics:
- Number of Instances: 506 
- Number of Attributes: 13 numeric/categorical predictive.

#### Data Attribute Information
    - **CRIM:** per capita crime rate by town
    - **ZN:** proportion of residential land zoned for lots over 25,000 sq.ft.
    - INDUS    proportion of non-retail business acres per town
    - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
    - NOX      nitric oxides concentration (parts per 10 million)
    - RM       average number of rooms per dwelling
    - AGE      proportion of owner-occupied units built prior to 1940
    - DIS      weighted distances to five Boston employment centres
    - RAD      index of accessibility to radial highways
    - TAX      full-value property-tax rate per $10,000
    - PTRATIO  pupil-teacher ratio by town
    - B        1000(Bk - 0.63)^2 where Bk is the proportion of black people by town
    - LSTAT    % lower status of the population

#### 1. Create a new enviroment  
```bash
    conda create -p boston_env python==3.8 -y
```

1.1 activate enviroment
```bash
    conda activate boston_env/
```