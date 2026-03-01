from google.colab import files
files.upload()
import pandas as pd
df = pd.read_csv("Car_Purchasing_Data.csv", encoding='latin1')
df.head()
