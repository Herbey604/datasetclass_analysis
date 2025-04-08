import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr2)

#indexing the array of our numbers: thhis is how we access our number set with numpy
print(arr[0])
print(arr[4])
print(arr[-2])

#index slicing
print(arr[1:])

#filtering out a particular number data
print(arr2[1, 0])

#mathematics operation [sum multiplication product mean]
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * b)
print(np.dot(a, b))    #np.dot is the module to find product of a mean
print(np.mean(a))  #np.mean is the module to find mean in a data set 1+2+3/3 =2
print(np.mean(b))     #np.mean is the module to find mean in a data set 4+5+6/3 = 5

#pandas   operation..........................
ds = pd.Series([10, 20, 40, 50]) 

print(ds) #the function series will list the value in column set and give it index value

#to create a dataframe for pandas
data = {
    "Name": ["Adesoji", "Abimbola", "Alayo"],
    "Age": [20, 30, 32],
    "City": ["lagos", "kano", "Abuja"]
}

df = pd.DataFrame(data)
print(df)

