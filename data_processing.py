import pandas as pd

# Wczytanie danych
df = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/AER/CollegeDistance.csv')

# Imputacja braków
numeric_columns = df.select_dtypes(include=['number']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())

# Zapis przetworzonych danych
df.to_csv("processed_data.csv", index=False)
print("Data processing completed and saved to 'processed_data.csv'")

# Przetwarzanie danych z dummies
df_with_dummies = pd.get_dummies(df, drop_first=True)
df_with_dummies.to_csv('processed_data_with_dummies.csv', index=False)
print("Processed data with dummies saved to 'processed_data_with_dummies.csv'")
