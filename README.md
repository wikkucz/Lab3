# Lab4-Analizator Wyników

Aplikacja do przewidywania zmiennej `score` na podstawie dostarczonych danych. Model jest oparty na algorytmie Random Forest i został uruchomiony w kontenerze Docker. 

## Opis projektu
Projekt służy do przewidywania zmiennej `score` na podstawie danych zawartych w zestawie. Model został wytrenowany na danych wejściowych takich jak: płeć, etniczność, status edukacji i inne cechy demograficzne.

Model jest zaimplementowany w Pythonie z użyciem FastAPI dla API oraz Docker do uruchomienia aplikacji w kontenerze.

## Wymagania
- Python 3.11
- Docker
- Docker Hub konto (dla publikacji obrazu)
- FastAPI
- scikit-learn (do implementacji modelu)
- pandas
- numpy

Wszystkie zależności są zawarte w pliku `requirements.txt`.

## Instalacja lokalna

1. **Sklonuj repozytorium**:
    ```bash
    git clone https://github.com/wikkucz/Lab3.git
    cd Lab3
    ```

2. **Zainstaluj wymagane pakiety**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Uruchom aplikację lokalnie**:
    Aplikację można uruchomić lokalnie za pomocą FastAPI. W terminalu wpisz:
    ```bash
    uvicorn main:app --reload
    ```
    Domyślnie aplikacja będzie dostępna pod adresem `http://127.0.0.1:8000`.

## Uruchamianie aplikacji

### Lokalnie
1. Upewnij się, że masz zainstalowane wszystkie zależności:
    ```bash
    pip install -r requirements.txt
    ```

2. Uruchom aplikację przy pomocy `uvicorn`:
    ```bash
    uvicorn main:app --reload
    ```

### Z wykorzystaniem Dockera

1. **Zbuduj obraz Docker**:
    W katalogu, gdzie znajduje się plik `Dockerfile`, uruchom polecenie:
    ```bash
    docker build -t lab4-analyzer .
    ```

2. **Uruchom kontener Docker**:
    Aby uruchomić aplikację w kontenerze Docker, użyj polecenia:
    ```bash
    docker run -p 8000:8000 lab4-analyzer
    ```

Aplikacja będzie dostępna pod adresem `http://localhost:8000`.

## Publikacja obrazu na Docker Hub

1. **Zaloguj się do Docker Hub**:
    Jeśli nie masz jeszcze konta na Docker Hub, załóż je. Następnie zaloguj się z terminala:
    ```bash
    docker login
    ```

2. **Oznacz obraz**:
    Zanim opublikujesz obraz na Docker Hub, oznacz go w odpowiedni sposób:
    ```bash
    docker tag lab4-analyzer wikkucz/lab4-analyzer:latest
    ```

3. **Prześlij obraz na Docker Hub**:
    Aby opublikować obraz na Docker Hub, użyj polecenia:
    ```bash
    docker push wikkucz/lab4-analyzer:latest
    ```

## Korzystanie z obrazu Docker z Docker Hub

1. **Pobierz obraz z Docker Hub**:
    Aby pobrać obraz, użyj następującego polecenia:
    ```bash
    docker pull wikkucz/lab4-analyzer:latest
    ```

2. **Uruchom pobrany obraz**:
    Uruchom obraz na swoim komputerze:
    ```bash
    docker run -p 8000:8000 wikucz/lab4-analyzer
    ```

Aplikacja będzie dostępna pod adresem `http://localhost:8000`.
Wejdź do interaktywnej dokumentacji API pod adresem: http://127.0.0.1:8000/docs
