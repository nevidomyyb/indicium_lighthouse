import pickle
import pandas as pd

with open('./random_forest_model.pkl', 'rb') as file:
    model_dict_retreino_sem_randomsearch = pickle.load(file)

with open('./random_forest_model_v2_randomized_search.pkl', 'rb') as file:
    model_dict_randomsearch = pickle.load(file)

model_re = model_dict_retreino_sem_randomsearch["model"]
feature_names_re = model_dict_retreino_sem_randomsearch["feature_names"]

model_randomsearch = model_dict_randomsearch["model"]
feature_names_randomsearch = model_dict_randomsearch["feature_names"]
data = {
    'id': 2595,
    'nome': 'Skylit Midtown Castle',
    'host_id': 2845,
    'host_name': 'Jennifer',
    'bairro_group': 'Manhattan',
    'bairro': 'Midtown',
    'latitude': 40.75362,
    'longitude': -73.98377,
    'room_type': 'Entire home/apt',
    'minimo_noites': 1,
    'numero_de_reviews': 45,
    'ultima_review': '2019-05-21',
    'reviews_por_mes': 0.38,
    'calculado_host_listings_count': 2,
    'disponibilidade_365': 355
}
input_df = pd.DataFrame([data])
input_df = pd.get_dummies(input_df, drop_first=True)
input_df = input_df.reindex(columns=feature_names_re, fill_value=0)
prediction = model_re.predict(input_df)
print(f"Predicted price with retrained model without reandomsearch: {prediction[0]:.2f}")

input_df = pd.DataFrame([data])
input_df = pd.get_dummies(input_df, drop_first=True)
input_df = input_df.reindex(columns=feature_names_randomsearch, fill_value=0)
prediction = model_randomsearch.predict(input_df)
print(f"Predicted price with model with reandomsearch: {prediction[0]:.2f}")