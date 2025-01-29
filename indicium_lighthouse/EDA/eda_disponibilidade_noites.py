from indicium_lighthouse.EDA.limpeza_dados import get_dados
import matplotlib.pyplot as plt
import pandas as pd
from indicium_lighthouse.EDA.utils import criar_tabela
def eda_disponibilidade_noites():
    data, _ = get_dados()
    data = data[(data['disponibilidade_365'] != 0) & (data['price'] != 0)]
    
    limites = [0, 50, 100, 250, 300, 365]
    data['intervalo_disponibilidade_365'] = pd.cut(data['disponibilidade_365'], bins=limites, right=True, include_lowest=True)
    data_disponibilidade = data.groupby('intervalo_disponibilidade_365', observed=True)['price'].agg(
        media='mean',
        desvio_padrao='std',
        preco_minimo='min',
        preco_maximo='max',
        quantidade='count'
    ).reset_index()
    limites = [0, 50, 100, 250, 300, 365, 1250]
    data['intervalo_minimo_noites'] = pd.cut(data['minimo_noites'], bins=limites, right=True, include_lowest=False)
    data_minimo_noites = data.groupby('intervalo_minimo_noites', observed=True)['price'].agg(
        media='mean',
        desvio_padrao='std',
        preco_minimo='min',
        preco_maximo='max',
        quantidade='count'
    ).reset_index()
    
    fig, (ax, ax1) = plt.subplots(2, 1)
    data_disponibilidade = data_disponibilidade.rename({
        "intervalo_disponibilidade_365": "Intervalo de Disponibilidade",
        "media": "Preço Médio",
        "desvio_padrao": "Desvio Padrão do Preço",
        "preco_minimo": "Preço Mínimo",
        "preco_maximo": "Preço Máximo",
        "quantidade": "Quantidade no Intervalo"
    }, axis=1)
    data_minimo_noites = data_minimo_noites.rename({
        "intervalo_minimo_noites": "Intervalo de Noites Mínimas",
        "media": "Preço Médio",
        "desvio_padrao": "Desvio Padrão do Preço",
        "preco_minimo": "Preço Mínimo",
        "preco_maximo": "Preço Máximo",
        "quantidade": "Quantidade no Intervalo"
    }, axis=1)
    criar_tabela(ax, data_disponibilidade, "Intervalo de Disponibilidades Durante o Ano e Preço")
    criar_tabela(ax1, data_minimo_noites, "Intervalo de Noites Mínimas e Preço")
    plt.show()

if __name__ == "__main__":
    eda_disponibilidade_noites()