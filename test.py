import pandas as pd
import numpy as np


# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(a + b)       #it add the column of A+b
# print(a * b)        #it multiply the column of a*b
# print(np.dot(a, b))    #np.dot is the module to find product of a mean using c. a to * c, b
# print(np.mean(a))  #np.mean is the module to find mean in a data set 1+2+3/3 =2
# print(np.mean(b))     #np.mean is the module to find mean in a data set 4+5+6/3 = 5
# s = pd.Series([10, 20, 40, 50]) 
# print(s)

phd = pd.DataFrame({
    "Name": ["Alice", "Alayo", "Abimbola"],
    "Age": [20, 30, np.nan],
    "Country": ["USA", "UK", np.nan]
})
print(f"Missing value\n: {phd.isnull()}")