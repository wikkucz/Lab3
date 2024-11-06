from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Inicjalizacja aplikacji FastAPI
app = FastAPI()

# Załaduj model predykcyjny
model = joblib.load('trained_model.joblib')  # Ścieżka do modelu


# Przykład danych, które mogą być użyte w API
class InputData(BaseModel):
    ethnicity: str
    fcollege: str
    gender: str
    home: str
    income: float
    score: float = None  # Zmienna 'score' jest opcjonalna, tylko do obliczeń


# Endpoint do przewidywania wartości 'score'
@app.post("/predict/")
def predict(input_data: InputData):
    # Przekształcenie danych wejściowych na wektor cech
    data = np.array([[input_data.ethnicity, input_data.fcollege, input_data.gender,
                      input_data.home, input_data.income]])

    # Dokonanie predykcji
    prediction = model.predict(data)

    # Zwrócenie wyniku
    return {"predicted_score": prediction[0]}


# Endpoint do sprawdzenia działania API
@app.get("/")
def read_root():
    return {"message": "Hello World"}

