import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

data = '../data/agricultural_raw_material.csv'
df = pd.read_csv(data)

df.isnull().sum()

# Replacing %, "," and "-"
df = df.replace('%', '', regex=True)
df = df.replace(',', '', regex=True)
df = df.replace('-', '', regex=True)
df = df.replace('', np.nan)
df = df.replace('MAY90', np.nan)
# Dropping rows with NaN values
df = df.dropna()
# Check to see if all NaN values are resolved
df.isnull().sum()
# Converting data type to float
lst = ["Coarse wool Price", "Coarse wool price % Change", "Copra Price", "Copra price % Change", "Cotton price % Change", "Fine wool Price", "Fine wool price % Change", "Hard log price % Change",
       "Hard sawnwood price % Change", "Hide price % change", "Plywood price % Change", "Rubber price % Change", "Softlog price % Change", "Soft sawnwood price % Change", "Wood pulp price % Change"]
df[lst] = df[lst].astype("float")
df.dtypes

df.Month = pd.to_datetime(df.Month.str.upper(), format='%b%y', yearfirst=False)
# Indexing month
df = df.set_index('Month')

df.head()

print(df.head())

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

# raw-materials list
raw_data = ['Coarse wool Price',  'Copra Price', 'Cotton Price', 'Fine wool Price',  'Hard log Price', 'Hard sawnwood Price',
            'Hide Price', 'Plywood Price', 'Rubber Price', 'Softlog Price', 'Soft sawnwood Price', 'Wood pulp Price']
# getting the correlation matrix
corrmat = df[raw_data].corr()
# setting the size of plot
fig = plt.figure(figsize=(12, 9))
# masking the upper traingle part since matrix is symmetric(repetitive)
mask = np.triu(np.ones_like(corrmat, dtype=bool))
cmap = 'mako_r'  # Você pode substituir 'coolwarm' por qualquer outra paleta de cores
sns.heatmap(corrmat, vmax=1, mask=mask, square=True, annot=True, cmap=cmap)
plt.show()
