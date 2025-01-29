


# Indicium Lighthouse

Este é um projeto Python gerenciado com [Poetry](https://python-poetry.org/), uma ferramenta de gerenciamento de dependências e empacotamento.

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter instalado:
- Python (versão recomendada: 3.8+)
- Poetry
  
## Instalando as Dependências

Dentro do diretório do projeto, execute:

```sh
poetry install
```

Isso criará um ambiente virtual e instalará todas as dependências listadas no pyproject.toml.Ativando o Ambiente Virtual

## Rodar os arquivos

Para rodar o projeto, gerar os gráficos, treinar o modelo ou ver a predição do modelo use cada arquivo respectivamente ao rodar o comando python:

- EDA dos bairros
```sh
poetry run python indicium_lighthouse/EDA/eda_bairro.py
```
- EDA da disponibilidade ao longo do ano, minimo de noites com relação ao preço
```sh
poetry run python indicium_lighthouse/EDA/eda_disponibilidade_noites.py
```
- EDA correlação entre as variáveis e preço
```sh
poetry run python indicium_lighthouse/EDA/eda_correlacao.py
```
- Gerar o mapa da distribuição dos bairros
```sh
poetry run python indicium_lighthouse/EDA/mapa_bairros_metro.py
```
- Análise do padrão de nomes
```sh
poetry run python indicium_lighthouse/ML/padrao_nomes.py
```
- Treinar o modelo final
```sh
poetry run python indicium_lighthouse/ML/modelo.py
```
- Predizer o preço de algum imóvel
```sh
poetry run python indicium_lighthouse/ML/predicao.py
```





