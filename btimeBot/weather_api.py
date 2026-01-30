import requests
import csv

API_URL = "https://api.open-meteo.com/v1/forecast"
CSV_FILE = "weather_api.csv"

def get_weather():
    params = {
        "latitude": -23.55,
        "longitude": -46.63,
        "current_weather": True
    }

    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()["current_weather"]

    return {
        "city": "São Paulo",
        "temperature": data["temperature"],
        "condition": "N/A",
        "source": "api"
    }

def save_to_csv(data):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["city", "temperature", "condition", "source"]
        )
        writer.writeheader()
        writer.writerow(data)

if __name__ == "__main__":
    try:
        weather = get_weather()
        save_to_csv(weather)
        print("✅ Dados coletados via API com sucesso")
    except Exception as error:
        print(f"❌ Erro na API: {error}")
