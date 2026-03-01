import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    'Name' : ['A', 'B', 'C'],
    'Age'  :[11, 12, 14],
    'Deparment' : ['civil', 'cse', 'electrical'],
    'marks' : [23, 40, 36]
}
df = pd.DataFrame(data)
print("Head of the dataset : \n" , df.head())
print("Summary Satistics : \n" , df.describe())
print("\n Missing Values : \n", df.isnull().sum())
print(" \n Average marks by department \n ", df.groupby('Deparment')['marks'].mean())
plt.figure(figsize=(5, 5))
plt.hist(df['marks'] , bins=5,  edgecolor='black')
plt.title('Distribution of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
