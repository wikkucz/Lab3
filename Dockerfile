# Wybierz bazowy obraz Pythona
FROM python:3.11-slim

# Ustaw katalog roboczy na /app w kontenerze
WORKDIR /app

# Skopiuj requirements.txt z katalogu głównego projektu do /app w kontenerze
COPY requirements.txt /app/requirements.txt

# Zainstaluj wymagane zależności
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj wszystkie pliki projektu do katalogu roboczego /app w kontenerze
COPY . /app/

# Ustawienie punktu wejścia do uruchamiania serwera FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]



