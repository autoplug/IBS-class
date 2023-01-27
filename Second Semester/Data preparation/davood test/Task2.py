import numpy as np
import pandas as pd
#independent variable P(X=x^Y=y)=P(X=x)*P(Y=y)
#P(Y=1)=P(X=0^Y=1)+P(X=1^Y=1)
#PX(0)=PXY(0,0)+PXY(0,1)+PXY(0,2)---> P(X=0)=0.3+0.25=0.55--- P(Y=1)=0.45


distr_table = pd.DataFrame({
    'X': [0, 0, 1, 1],
    'Y': [1, 2, 1, 2],
    'pr': [0.3, 0.25, 0.15, 0.3]
})
# print(distr_table["X"][0])
# exit()

def check_independence(distr_table):#Element1
    
    PX_0 = distr_table.loc[(distr_table["X"])==(distr_table["X"][0])]
    PX_0 = sum(PX_0["pr"])
    
    PY_1 = distr_table.loc[distr_table["Y"]==distr_table["Y"][0]]
    PY_1 = sum(PY_1["pr"])

    PX0_Y1 = distr_table.loc[(distr_table["X"]==distr_table["X"][0]) & (distr_table["Y"]==distr_table["Y"][0])]
    PX0_Y1 = PX0_Y1['pr'][0]
    # print("p x=0",PX_0,"P Y=1",PY_1)
    # print("PX0_Y1",PX0_Y1)
    result = True if PX0_Y1 == PX_0 * PY_1 else False

    return result
def covariance(distr_table):
    # Element 2
    # E[X] = Sum(x * pr) and E[Y] = Sum(y * pr)
    # (X - E[X])(Y - E[Y])    
    EX = distr_table['X'].dot(distr_table['pr'])
    EY = distr_table['Y'].dot(distr_table['pr'])

    distr_table['dev_product'] = (distr_table['X'] - EX) * (distr_table['Y'] - EY)

    cov = distr_table['pr'].dot(distr_table['dev_product'])
    return cov
def correlation(distr_table):

    # Calculate standard deviation of X
    x_mean = distr_table['X'].dot(distr_table['pr'])
    x_std = np.sqrt(((distr_table['X'] - x_mean) ** 2).dot(distr_table['pr']))

    # Calculate standard deviation of Y
    y_mean = distr_table['Y'].dot(distr_table['pr'])
    y_std = np.sqrt(((distr_table['Y'] - y_mean) ** 2).dot(distr_table['pr']))
    cov = covariance(distr_table)
    correlation = cov / (x_std * y_std)

    # print(check_independence(distr_table))
    return correlation

result = {"are_independent": check_independence(distr_table), "cov":covariance(distr_table), "corr":correlation(distr_table) }

print(result)