import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# limites = [0, 100, 200, 300, 400, 500, 600, 700]
# data['intervalo_numero_de_reviews'] = pd.cut(data['numero_de_reviews'], bins=limites, right=True, include_lowest=True)
# data_reviews_total = data.groupby('intervalo_numero_de_reviews', observed=True)['price'].agg(
#     media='mean',
#     desvio_padrao='std',
#     preco_minimo='min',
#     preco_maximo='msax',
#     quantidade='count'
# ).reset_index()
# print("Descrição estatística focado no preço agrupado por numero de reviews.")
# print(data_reviews_total)
# print('-'*20)
