import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Wczytanie przetworzonych danych
df = pd.read_csv(r'C:\Users\wikto\PycharmProjects\Lab3\data\processed_data_with_dummies.csv')

X = df.drop('score', axis=1)
y = df['score']

# Podział danych na zestaw treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Wybór modelu
model = RandomForestRegressor(random_state=42)

# Trenowanie modelu
model.fit(X_train, y_train)

# Zapis modelu
joblib.dump(model, r'C:\Users\wikto\PycharmProjects\Lab3\data\trained_model.joblib')

print("Model training completed and saved to 'data/trained_model.joblib'")
