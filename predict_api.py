from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Ładowanie modelu
model = joblib.load('trained_model.joblib')

# Inicjalizacja aplikacji FastAPI
app = FastAPI()

# Definicja klasy danych wejściowych
class PredictionInput(BaseModel):
    gender: str
    ethnicity: str
    fcollege: str
    mcollege: str
    home: str
    urban: str
    unemp: float
    wage: float
    distance: float
    tuition: float
    education: float
    income: str
    region: str

@app.post("/predict")
async def predict(input_data: PredictionInput):
    # Konwersja danych wejściowych do formatu DataFrame
    data = pd.DataFrame([input_data.dict()])

    # Konwersja zmiennych kategorycznych na dummies
    data = pd.get_dummies(data, drop_first=True)

    # Wyrównanie kolumn względem trenowanego modelu
    model_columns = joblib.load('model_columns.joblib')
    data = data.reindex(columns=model_columns, fill_value=0)

    # Przewidywanie wyniku
    try:
        prediction = model.predict(data)
        return {"predicted_score": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
