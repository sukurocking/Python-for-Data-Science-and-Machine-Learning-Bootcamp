import pandas as pd
import seaborn as sns
salaries = pd.read_csv("Salaries.csv")
# print(salaries.head())

# salaries.dropna()

# salaries.duplicated()
# salaries.columns

# salaries["Id"].
# sns.scatterplot()
# sns.lineplot()
# salaries.agg()
print(salaries.isna().sum())