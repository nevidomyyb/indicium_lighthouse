import pandas as pd
from limpeza_dados import get_dados
import matplotlib.pyplot as plt
import numpy as np

def calc_rentabilidade(series):
    preco_medio = series['preco_medio']
    disponibilidade_media = series['disponibilidade_media']
    return preco_medio * disponibilidade_media

def eda_bairro():
    data, _ = get_dados()
    data_price_bairro = data.groupby('bairro_group')['price'].agg(
        preco_medio='mean',
        desvio_padrao_preco='std',
        preco_minimo='min',
        preco_maximo='max',
        quantidade_imoveis='count',
    ).reset_index()

    disponibilidade_media_bairro = data.groupby('bairro_group')['disponibilidade_365'].agg(
        disponibilidade_media='mean'
    )
    data_price_bairro = data_price_bairro.merge(
        disponibilidade_media_bairro,
        on='bairro_group',
        how='left'
    )
    data_price_bairro['rentabilidade_potencial'] = data_price_bairro.apply(calc_rentabilidade, axis=1)
    fig, (ax, ax1) = plt.subplots(2, 1)
    ax.axis('tight')
    ax.axis('off')
    
    data_price_bairro= data_price_bairro.rename({
        "bairro_group": "Bairro",
        "preco_medio": "Preço Médio",
        "desvio_padrao_preco": "Desvio Padrão do Preço",
        "preco_minimo": "Preço Mínimo",
        "preco_maximo": "Preço Máximo",
        "quantidade_imoveis": "Quantidade de Imóveis",
        "disponibilidade_media": "Disponibilidade Média",
        "rentabilidade_potencial": "Potêncial de Rentabilidade (R$)"
    }, axis=1)
    
    
    table = ax.table(
        cellText=data_price_bairro.values,
        colLabels=data_price_bairro.columns,
        loc='center',
        cellLoc='center', 
        colColours=['#f5f5f5']*data_price_bairro.shape[1]
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    
    ax.set_title("Descrição estatística", fontsize=15)
    
    width = 0.25 
    multiplier = 0
    bairros = data_price_bairro['Bairro'].values
    valores = data_price_bairro[['Preço Médio', 'Potêncial de Rentabilidade (R$)', 'Quantidade de Imóveis']]
    x = np.arange(len(bairros))

    for coluna, valor in valores.items():
        offset = width * multiplier
        rects = ax1.bar(x + offset, valor, width, label=coluna)
        multiplier += 1

    ax1.set_ylabel('Valor')
    ax1.set_title('Preço Médio, Potêncial de Rentabilidade e Quantidade de Imóveis por Bairro')
    ax1.set_xticks(x + width, bairros)
    ax1.set_xticklabels(bairros, rotation=45, ha="right")
    ax1.legend(loc='upper left', ncols=3)
    ax1.set_ylim(0, 25000)

    plt.show()

if __name__ == "__main__":
    eda_bairro()