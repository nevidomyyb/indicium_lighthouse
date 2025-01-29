from indicium_lighthouse.EDA.limpeza_dados import get_dados
from sklearn.feature_extraction.text import CountVectorizer
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import LatentDirichletAllocation
import textwrap

def wrap_labels(labels, width= 20):
    return [textwrap.fill(label, width=width) for label in labels]

data, _ = get_dados()
data = data[(data['disponibilidade_365'] != 0) & (data['price'] != 0)]
fig, (ax, ax1) = plt.subplots(2,1)

vectorizer = CountVectorizer(stop_words='english', max_features=20)
media = data['price'].mean()
top_words = vectorizer.fit_transform(data[data['price'] >= media*1.5]['nome'])
words = vectorizer.get_feature_names_out()
word_counts = pd.DataFrame(
    data=top_words.toarray(), columns=words,
).sum().sort_values(ascending=False)

words = word_counts.index
y_pos = np.arange(len(words))
quantities = word_counts.values

ax.barh(y_pos, quantities, align='center')
ax.set_yticks(y_pos, words)
ax.invert_yaxis()
ax.set_xlabel('Quantidade')
ax.set_title("Palavras usadas em imóveis de alto valor")

lda = LatentDirichletAllocation(n_components=6, random_state=42)
lda.fit(top_words)

topics = lda.transform(top_words)
top_imoveis = data[data['price'] >= media * 1.5]
top_imoveis['topico'] = topics.argmax(axis=1)
topic_counts = top_imoveis['topico'].value_counts()
ax1.bar(topic_counts.index, topic_counts.values, color='skyblue')
ax1.set_title("Distribuição de tópicos em imóveis de alto valor")
ax1.set_ylabel('Contagem de Imóveis')
ax1.set_xlabel('Tópico')
ax1.set_xticks(topic_counts.index)


n_top_words = 10 
topics_labels = []
for topic_idx, topic in enumerate(lda.components_):
    top_indices = topic.argsort()[-n_top_words:][::-1]
    topic_words = [words[i] for i in top_indices]
    topics_labels.append(', '.join(topic_words))
wrapped = wrap_labels(topics_labels)
ax1.set_xticklabels(wrapped, rotation=0, ha='center')
plt.tight_layout()

plt.show()
