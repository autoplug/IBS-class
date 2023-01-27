import numpy as np
import pandas as pd

distr_table = pd.DataFrame({
    'X': [0, 0, 1, 1],
    'Y': [1, 2, 1, 2],
    'pr': [0.3, 0.25, 0.15, 0.3]
})

EX = distr_table['X'].dot(distr_table['pr'])
EY = distr_table['Y'].dot(distr_table['pr'])

distr_table['dev_product'] = (distr_table['X'] - EX) * (distr_table['Y'] - EY)

cov = distr_table['pr'].dot(distr_table['dev_product'])


# Calculate standard deviation of X
x_mean = distr_table['X'].dot(distr_table['pr'])
x_std = np.sqrt(((distr_table['X'] - x_mean) ** 2).dot(distr_table['pr']))

# Calculate standard deviation of Y
y_mean = distr_table['Y'].dot(distr_table['pr'])
y_std = np.sqrt(((distr_table['Y'] - y_mean) ** 2).dot(distr_table['pr']))

correlation = cov / (x_std * y_std)

print(f"Std of X: {x_std}")
print(f"Std of Y: {y_std}")
print(correlation)




print(cov)