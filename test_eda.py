import pandas as pd
df = pd.read_csv('dataset_clustering_project/bank_transactions_data_edited.csv')
print(df.dtypes)
print(df.nunique())
