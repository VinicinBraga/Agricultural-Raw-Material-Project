import pandas as pd
data = '../data/agricultural_raw_material.csv'
df=pd.read_csv(data)

print(df.head())