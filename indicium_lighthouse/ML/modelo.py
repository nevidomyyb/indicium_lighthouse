import pandas as pd
import pickle
from indicium_lighthouse.EDA.limpeza_dados import get_dados
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

def model():
    df, _ = get_dados()
    
    X = df.drop(columns=['price'])
    y = df['price']
    
    X = pd.get_dummies(X, drop_first=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # param_dist = {
    #     'n_estimators': randint(50, 100),
    #     'max_depth': [None, 10, 20],
    #     'min_samples_split': randint(5, 10),
    #     'min_samples_leaf': randint(2, 5),
    #     'max_features': ['sqrt', 'log2', None]
    # }
    
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=None, 
        random_state=42,
        n_jobs=-1,
        verbose=2
    )
    
    # model = RandomizedSearchCV(
    #     model, param_distributions=param_dist, n_iter=10, cv=None,
    #     scoring='neg_mean_absolute_error', random_state=42, n_jobs=3,
    #     verbose=2
    # )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f'MAE: {mae:.2f}')
    print(f'MSE: {mse:.2f}')
    print(f'R²: {r2:.2f}')


    feature_importances = pd.DataFrame({
        'Feature': X.columns,
        #'Importance': model.best_estimator_.feature_importances_  Se usar random search.
        'Importance': model.feature_importances_
    }).sort_values(by='Importance', ascending=False)

    print(feature_importances.head(10))
    
    model_dict = {
        "model": model,
        "feature_names": X.columns.tolist()
    }
    
    with open('random_forest_model.pkl', 'wb') as f:
        pickle.dump(model_dict, f)
    
if __name__ == "__main__":
    model()