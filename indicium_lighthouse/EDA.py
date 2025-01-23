import pandas as pd

data = pd.read_csv('./indicium_lighthouse/teste_indicium_precificacao.csv')

df_nan = data[data.isna().any(axis=1)]
nan_counts = df_nan.isna().sum()
df_nan_counts = pd.DataFrame({'coluna': nan_counts.index, "quantidade": nan_counts.values})
print(df_nan_counts)