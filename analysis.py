import pandas as pd

df = pd.read_csv('GRASP.csv')
# print(df.columns)
print(df.groupby(['CONJUNTO', 'AMOSTRAS', 'PORCENTAGEM']).mean())