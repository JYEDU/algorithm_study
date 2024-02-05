import numpy as np
from sklearn import linear_model

"""
Marketing Costs
link : https://www.testdome.com/questions/python-data-science/marketing-costs/41455

:param marketing_expenditure: (list) A list of integers with the expenditure for each previous campaign.
:param units_sold: (list) A list of integers with the number of units sold for each previous campaign.
:param desired_units_sold: (integer) Target number of units to sell in the new campaign.
:returns: (float) Required amount of money to be invested.
"""

def desired_marketing_expenditure(marketing_expenditure, units_sold, desired_units_sold):

    # data
    trainX=np.array(units_sold).reshape(-1,1)
    trainY=np.array(marketing_expenditure).reshape(-1,1)
    testX=np.array(desired_units_sold).reshape(-1,1)
    
    # model train
    model=linear_model.LinearRegression()
    model.fit(trainX, trainY)
    
    # model test
    predY=model.predict(testX)
    answer=round(float(predY.item()),-4)
    return answer

#For example, with the parameters below, the function should return 250000.0
print(desired_marketing_expenditure(
    [300000, 200000, 400000, 300000, 100000],
    [60000, 50000, 90000, 80000, 30000],
    60000))

def desired_marketing_expenditure2(marketing_expenditure, units_sold, desired_units_sold):

    # data
    trainX=np.array(marketing_expenditure).reshape(-1,1)
    trainY=np.array(units_sold).reshape(-1,1)
    
    # model train
    model=linear_model.LinearRegression()
    model.fit(trainX, trainY)
    
    # model test
    answer=((desired_units_sold-model.intercept_)/model.coef_).item()
    return answer

print(desired_marketing_expenditure2(
    [300000, 200000, 400000, 300000, 100000],
    [60000, 50000, 90000, 80000, 30000],
    60000))