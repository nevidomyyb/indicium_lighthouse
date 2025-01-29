import pickle
import pandas as pd

with open('./random_forest_v7.pkl', 'rb') as file:
    MODEL = pickle.load(file)


model_re = MODEL["model"]
feature_names_re = MODEL["feature_names"]

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
