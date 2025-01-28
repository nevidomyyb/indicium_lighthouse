from indicium_lighthouse.EDA.limpeza_dados import get_dados
from indicium_lighthouse.EDA.utils import criar_tabela
import matplotlib.pyplot as plt


def eda_correlacao():

    data, _ = get_dados()   
    

    relacao = data.corr(method='spearman', numeric_only=True)
    relacao = relacao.drop([
        'id', 'host_id', 'latitude', 'longitude', 'minimo_noites', 'numero_de_reviews',
        'reviews_por_mes', 'calculado_host_listings_count', 'disponibilidade_365'
    ],axis=0)
    relacao = relacao.drop(['id', 'host_id', 'price', 'latitude', 'longitude',],axis=1)
    print(relacao)
    fig, ax = plt.subplots(1,1 )
    criar_tabela(ax, relacao, "Relação")
    plt.show()
    
if __name__ == "__main__":
    eda_correlacao()