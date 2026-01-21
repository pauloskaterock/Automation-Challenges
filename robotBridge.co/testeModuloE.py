# tentativa de desenvolver o modulo E em python
import requests
import json
import pandas as pd
import time
from datetime import datetime
import sys
import os
from retrying import retry
import logging


logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "module": "E", "message": "%(message)s"}',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class CoinGeckoExtractor:   # verificar class e metodos errados
    def __init__(self):
        self.api_url = "https://api.coingecko.com/api/v3/coins/markets"
        self.params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 5,
            "page": 1
        }
        self.execution_id = datetime.now().strftime("%Y%m%d%H")
        self.headers = {
            "Accept": "application/json",
            "User-Agent": "BridgeRPA/1.0"
        }

    def retry_if_connection_error(self, exception):
        """Condição para retry"""
        return isinstance(exception, (requests.ConnectionError, requests.Timeout))

    @retry(stop_max_attempt_number=3,
      wait_exponential_multiplier=1000,
      wait_exponential_max=10000,
      # retry_on_exception=self.retry_if_connection_error)
    )
    def fetch_data(self):
        """Busca dados da API com retry"""
        start_time = time.time()

        try:
            response = requests.get(
                self.api_url,
                params=self.params,
                headers=self.headers,
                timeout=30
            )

            elapsed_time = time.time() - start_time

            if response.status_code == 200:
                data = response.json()

                if len(data) != 5:
                    raise ValueError(f"API retornou {len(data)} itens, esperado 5")

                return {
                    "success": True,
                    "data": data,
                    "response_time": round(elapsed_time, 3),
                    "records_count": len(data),
                    "status_code": response.status_code
                }
            else:
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}",
                    "response_time": round(elapsed_time, 3),
                    "status_code": response.status_code
                }

        except requests.exceptions.RequestException as e:
            elapsed_time = time.time() - start_time
            return {
                "success": False,
                "error": str(e),
                "response_time": round(elapsed_time, 3),
                "status_code": None
            }

    def process_coins(self, api_data):
        """Processa os dados das moedas"""
        coins = []

        for item in api_data:
            coin = {
                "id": item.get("id", ""),
                "symbol": item.get("symbol", "").upper(),
                "name": item.get("name", ""),
                "current_price": item.get("current_price", 0),
                "market_cap": item.get("market_cap", 0),
                "total_volume": item.get("total_volume", 0),
                "execution_id": self.execution_id,
                "extraction_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            coins.append(coin)

        return coins

    def save_to_csv(self, coins):
        """Salva dados em CSV"""
        if not coins:
            return None

        df = pd.DataFrame(coins)

        #tentar manter apens coluas cvs
        csv_columns = ["id", "symbol", "name", "current_price", "market_cap", "total_volume"]
        df_csv = df[csv_columns].copy()
        df_csv["extraction_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        filename = f"coins_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df_csv.to_csv(filename, index=False, encoding='utf-8')

        return filename

    def save_to_json(self, coins):
        """Salva dados em JSON (para queue simulation)"""
        if not coins:
            return None

        filename = f"coins_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        output = {
            "execution_id": self.execution_id,
            "extraction_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "records_count": len(coins),
            "coins": coins
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        return filename

    def check_idempotence(self):
        """Verifica se já foi processado (simulação)"""
        # verificar orquestrator
        check_file = f"processed_{self.execution_id}.check"

        if os.path.exists(check_file):
            logger.warning(f"Execution {self.execution_id} already processed")
            return True

        # processado
        with open(check_file, 'w') as f:
            f.write(datetime.now().isoformat())

        return False

    def run(self):
        """Executa o fluxo completo"""

        logger.info(f"Starting execution {self.execution_id}")

        # 1. idempotência
        if self.check_idempotence():
            return {
                "success": False,
                "error": "Already processed",
                "execution_id": self.execution_id
            }

        # 2. Buscar dados da API
        logger.info("Fetching data from CoinGecko API...")
        api_result = self.fetch_data()

        if not api_result["success"]:
            logger.error(f"API error: {api_result.get('error', 'Unknown error')}")
            return api_result

        # 3. Processar dados
        logger.info(f"API response time: {api_result['response_time']}s")
        coins = self.process_coins(api_result["data"])

        # 4. Salvar e um csv
        csv_file = self.save_to_csv(coins)
        if csv_file:
            logger.info(f"Data saved to CSV: {csv_file}")


        json_file = self.save_to_json(coins)
        if json_file:
            logger.info(f"Data saved to JSON: {json_file}")

        # 6. Logar métricas finais
        metrics = {
            "success": True,
            "execution_id": self.execution_id,
            "response_time": api_result["response_time"],
            "records_count": api_result["records_count"],
            "status_code": api_result["status_code"],
            "csv_file": csv_file,
            "json_file": json_file,
            "timestamp": datetime.now().isoformat()
        }

        logger.info(f"Metrics: {json.dumps(metrics)}")

        return metrics

def main():
    """Função principal"""
    try:
        extractor = CoinGeckoExtractor()
        result = extractor.run()

        # Imprimir resultado final para captura
        print(f"BRIDGE_RPA_RESULT:{json.dumps(result)}")

        return 0 if result.get("success", False) else 1

    except Exception as e:
        logger.error(f"Critical error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
