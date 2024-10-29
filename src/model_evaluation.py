import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Wczytanie przetworzonych danych
df = pd.read_csv(r'C:\Users\wikto\PycharmProjects\Lab3\data\processed_data_with_dummies.csv')

X = df.drop('score', axis=1)
y = df['score']

# Podział danych na zestaw testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Wczytanie modelu
model = joblib.load(r'C:\Users\wikto\PycharmProjects\Lab3\data\trained_model.joblib')

# Predykcje
y_pred = model.predict(X_test)

# Ocena modelu
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MSE: {mse}')
print(f'R²: {r2}')

# Wizualizacja wyników
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Actual Score")
plt.ylabel("Predicted Score")
plt.title("Actual vs Predicted Score")
plt.savefig(r'C:\Users\wikto\PycharmProjects\Lab3\data\actual_vs_predicted.png')
plt.close()
