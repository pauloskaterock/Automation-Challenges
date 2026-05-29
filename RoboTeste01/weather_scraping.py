import requests     # Importa a biblioteca 'requests' para fazer requisições HTTP
import csv          # Importa a biblioteca 'csv' para trabalhar com arquivos CSV

URL = "https://wttr.in/Sao+Paulo?format=j1" # acessando url
CSV_FILE = "weather_scraping.csv" # salva as informaç~es em um csv



# funcao para obter os dados
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

# funcao para slavar os dados
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
