# Data pre-process - Steve Mendis
import pandas as pd

# creating a data frame
df = pd.read_csv('/Users/stevemendis/Desktop/crop_data_analysis/data_preprocess/data/data.csv')
print(df.head())

df = df.drop('Crop_Year', axis=1)
newdf=df.groupby(['State','Crop','Season','District ']).mean()

print(df.groupby(['State','Crop','Season','District ']).mean().head())
import random


rainfall_mm = [random.uniform(0, 100) for _ in range(34631)]
years = [random.randint(2000, 2021) for _ in range(34631)]
percentage = [random.uniform(-100, 100) for _ in range(34631)]

newdf["Rainfall"] = rainfall_mm
newdf["Profit"] = percentage
newdf["Year"] = years
# print(newdf)

# newdf = df.apply(lambda x: x.astype(str).str.lower())
# newdf["District "] = newdf["District "].apply(lambda x: x.replace('"', ''))

newdf = newdf.dropna()
newdf.to_csv('crop_data_app/finaldata.csv', sep=',')

print(len(df.index))