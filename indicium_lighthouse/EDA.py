import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

dupp = data.duplicated().sum() #Checando duplicatas
dupp_string = "Não há linhas duplicadas" if dupp == 0 else f"Há {dupp} linhas duplicadas"
print(dupp_string)

data_price_bairro = data.groupby('bairro_group')['price'].agg(
    media='mean',
    desvio_padrao='std',
    preco_minimo='min',
    preco_maximo='max'
).reset_index()
print("Descrição estatística focado no preço por bairro")
print(data_price_bairro)

limites = [0, 100, 200, 300, 400, 500, 600, 700]
data['intervalo_numero_de_reviews'] = pd.cut(data['numero_de_reviews'], bins=limites, right=True)
data_reviews_total = data.groupby('intervalo_numero_de_reviews', observed=True)['price'].agg(
    media='mean',
    desvio_padrao='std',
    preco_minimo='min',
    preco_maximo='max'
).reset_index()
print("Descrição estatística focado no preço agrupado por numero de reviews.")
print(data_reviews_total)

relacao = data.corr(method='spearman', numeric_only=True)
relacao = relacao.drop([
    'id', 'host_id', 'latitude', 'longitude', 'minimo_noites', 'numero_de_reviews',
    'reviews_por_mes', 'calculado_host_listings_count', 'disponibilidade_365'
],axis=0)
relacao = relacao.drop(['id', 'host_id', 'price', 'latitude', 'longitude',],axis=1)
print("Matriz de correlação")
print(relacao)
