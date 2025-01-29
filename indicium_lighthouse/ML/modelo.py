import pandas as pd
import pickle
from indicium_lighthouse.EDA.limpeza_dados import get_dados
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_squared_log_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint
import numpy as np

def model():
    df, _ = get_dados()
    df = df.drop(columns=['id', 'host_id', 'host_name', 'calculado_host_listings_count'])
    df = df[(df['disponibilidade_365'] != 0) & (df['price'] != 0)]
    X = df.drop(columns=['price', 'nome'])
    y = df['price']
    
    X = pd.get_dummies(X, drop_first=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    param_dist = {
        'n_estimators': randint(50, 100),
        'max_depth': [None, 10, 20],
        'min_samples_split': randint(5, 10),
        'min_samples_leaf': randint(2, 5),
        'max_features': ['sqrt', 'log2', None]
    }
    
    # model = RandomForestRegressor(
    #     n_estimators=100,
    #     max_depth=None, 
    #     random_state=42,
    #     n_jobs=-1,
    #     verbose=2
    # )
    
    model = RandomizedSearchCV(
        RandomForestRegressor(verbose=2, random_state=42), param_distributions=param_dist, n_iter=20, cv=None,
        scoring='neg_mean_absolute_error', random_state=42, n_jobs=2,
        verbose=2
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    msle = mean_squared_log_error(y_test,y_pred)
    
    print(f'MAE: {mae:.2f}')
    print(f"RMSE: {rmse:.2f}")
    print(f"MSLE: {msle:.2f}")
    print(f'R²: {r2:.2f}')

    feature_importances = pd.DataFrame({
        'Feature': X.columns,
        'Importance': model.best_estimator_.feature_importances_  #Se usar random search.
        # 'Importance': model.feature_importances_ #Sem random search
    }).sort_values(by='Importance', ascending=False)

    print(feature_importances.head(10))
    feature_importances = feature_importances.sort_index()
    feature_importances.to_csv('feature_importances.csv', header=True, sep=';')
    model_dict = {
        "model": model,
        "feature_names": X.columns.tolist()
    }
    
    with open('random_forest_v7.pkl', 'wb') as f:
        pickle.dump(model_dict, f)
    
if __name__ == "__main__":
    model()