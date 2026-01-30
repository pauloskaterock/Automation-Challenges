import requests
import csv

URL = "https://wttr.in/Sao+Paulo?format=j1"
CSV_FILE = "weather_scraping.csv"

def get_weather():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    data = response.json()

    temperature = data["current_condition"][0]["temp_C"]
    condition = data["current_condition"][0]["weatherDesc"][0]["value"]

    return {
        "city": "São Paulo",
        "temperature": temperature,
        "condition": condition,
        "source": "scraping"
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
        print("✅ Dados coletados via scraping com sucesso")
    except Exception as error:
        print(f"❌ Erro no scraping: {error}")
