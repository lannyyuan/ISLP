#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 15:41:50 2018
@author: arpanganguli
"""

# import statistical tools
from __future__ import print_function
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
import scipy.stats as stats

# import data visualisation tools
import matplotlib.pyplot as plt
from matplotlib import pylab
import plotly.plotly as py
import plotly.graph_objs as go
import seaborn as sns

# import and view first 10 items of file
url = "/Users/arpanganguli/Documents/Finance/ISLR/Datasets/Carseats.csv"
CarSeats = pd.read_csv(url)
print(CarSeats.head())
print(list(CarSeats))
print(CarSeats.info())

# 10.a. Multiple regression
reg = ols(formula = 'Sales ~ Price + C(Urban) + C(US)', data = CarSeats).fit() # C prepares categorical data for regression
print(reg.summary())

"""
10.b. For a unit increase of price ceterus paribus, the sales decrease by 0.0545 units. Likewise, for a unit increase in an urban setting
ceterus paribus the sales decrease by 0.219 units. Likewise, for a location in the US a unit increase of another store ceterus paribus
increases the sales by 1.2006 units.

10.c. Sales = 13.0435 - 0.0545*Price - 0.0219 + 1.2006 => Sales = 14.8305 - 0.0545*Price
"""

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
RESULTS (NOT PART OF CODE)

runfile('/Users/arpanganguli/Desktop/untitled0.py', wdir='/Users/arpanganguli/Desktop')
   SlNo  Sales  CompPrice  Income ...   Age  Education  Urban   US
0     1   9.50        138      73 ...    42         17    Yes  Yes
1     2  11.22        111      48 ...    65         10    Yes  Yes
2     3  10.06        113      35 ...    59         12    Yes  Yes
3     4   7.40        117     100 ...    55         14    Yes  Yes
4     5   4.15        141      64 ...    38         13    Yes   No

[5 rows x 12 columns]
['SlNo', 'Sales', 'CompPrice', 'Income', 'Advertising', 'Population', 'Price', 'ShelveLoc', 'Age', 'Education', 'Urban', 'US']
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 400 entries, 0 to 399
Data columns (total 12 columns):
SlNo           400 non-null int64
Sales          400 non-null float64
CompPrice      400 non-null int64
Income         400 non-null int64
Advertising    400 non-null int64
Population     400 non-null int64
Price          400 non-null int64
ShelveLoc      400 non-null object
Age            400 non-null int64
Education      400 non-null int64
Urban          400 non-null object
US             400 non-null object
dtypes: float64(1), int64(8), object(3)
memory usage: 37.6+ KB
None
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  Sales   R-squared:                       0.239
Model:                            OLS   Adj. R-squared:                  0.234
Method:                 Least Squares   F-statistic:                     41.52
Date:                Thu, 03 Jan 2019   Prob (F-statistic):           2.39e-23
Time:                        20:45:10   Log-Likelihood:                -927.66
No. Observations:                 400   AIC:                             1863.
Df Residuals:                     396   BIC:                             1879.
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
Intercept          13.0435      0.651     20.036      0.000      11.764      14.323
C(Urban)[T.Yes]    -0.0219      0.272     -0.081      0.936      -0.556       0.512
C(US)[T.Yes]        1.2006      0.259      4.635      0.000       0.691       1.710
Price              -0.0545      0.005    -10.389      0.000      -0.065      -0.044
==============================================================================
Omnibus:                        0.676   Durbin-Watson:                   1.912
Prob(Omnibus):                  0.713   Jarque-Bera (JB):                0.758
Skew:                           0.093   Prob(JB):                        0.684
Kurtosis:                       2.897   Cond. No.                         628.
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
