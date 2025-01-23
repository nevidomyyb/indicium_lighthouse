import pandas as pd

data = pd.read_csv('./indicium_lighthouse/teste_indicium_precificacao.csv')

df_nan = data[data.isna().any(axis=1)]
nan_counts = df_nan.isna().sum()
df_nan_counts = pd.DataFrame({'coluna': nan_counts.index, "quantidade": nan_counts.values})

data = data.fillna(value={
    'nome': 'Não informado',
    'host_name': 'Não informado',
    'ultima_review': pd.NaT,
    'reviews_por_mes': 0
})
