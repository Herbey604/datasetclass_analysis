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

print(a + b)       #it add the column of A+b
print(a * b)        #it multiply the column of a*b
print(np.dot(a, b))    #np.dot is the module to find product of a mean using c. a to * c, b
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

#filtering of data 
filtering_data = df[df['Age'] > 27]
print(df)
print(f'Data filtered: {filtering_data}')
#it will print the seconf column in the dataframe

#to modify a particular data set in a frame
df['Age'] = df['Age'] + 1
print(df)
#it will add +1 to the age in the dataframe above

#Add custom column to the dataframe
df['country'] = ['Nigeria', 'Nigeria', 'Nigeria']
#this will add to the column in the dataframe

#grouping is use to group a two column to one coulumn and tp find average of the data
data = {
    "Employee": ["Alice", "James", "John", "Samson", "lekan"],
    "Department": ["HR", "IT", "Finance", "HR", "IT"],
    "Salary": [50000, 60000, 55000, 52000, 65000]
}
df = pd.DataFrame(data)

print(f"Data grouping frame: {df}")
data_grouping = df.groupby('Department')['Salary'].mean()
print(data_grouping)

#merging a data
df1 = pd.DataFrame({
    "Employee": ["John", "Alice","James"],
    "Department": ["HR", "IT", "Finance"],
})

df2 = pd.DataFrame({
    "Employee": ["John", "Alice", "James"],
    "Salary": [55000, 50000, 60000]
})
merged = pd.merge(df1, df2, on='Employee')
print(f"Data Merged:\n {merged}")

#handling missing value
hdf = pd.DataFrame({
    "Name": ['Adesoji', 'Adebola', 'Adewumi', 'Juwon'],
    "Age": [26, np.nan, 32, np.nan],
    "City": ['lagos', 'Kano', 'Abuja', 'Osogbo'],
    "Country": ['Nigeria', np.nan, 'Nigeria', np.nan]
})
#isnull is the use of cleaning/checking the missing value
print(f"Missing value detected\n: {hdf.isnull()}")

print(f"Handling data frame:\n {hdf}")

#dropna is for dropping the missing value with the help of dropna function
drop = hdf.dropna()
print(f"New data frame:\n {drop}")

replace_nan = hdf.fillna({'Age': hdf["Age"].mean(), "Country": "unknown"})
print(f"Replace missing value: \n {replace_nan}")
