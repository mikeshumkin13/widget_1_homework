import os
import requests
from dotenv import load_dotenv
from typing import Dict, Any

# Загрузка переменных окружения из .env файла
load_dotenv()

def get_exchange_rate(currency: str) -> float:
    """
    Получает текущий курс валюты по отношению к рублю.

    :param currency: Валюта для конвертации (например, 'USD', 'EUR').
    :return: Текущий курс валюты по отношению к рублю.
    """
    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    if not api_key:
        raise ValueError("API key is missing")

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers)
    data: Dict[str, Any] = response.json()

    if response.status_code != 200 or "RUB" not in data.get("rates", {}):
        raise ValueError("Invalid response from exchange rate API")

    return float(data["rates"]["RUB"])


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции.
    :return: Сумма транзакции в рублях.
    """
    amount = float(transaction["amount"])
    currency = transaction.get("currency", "RUB")

    if currency != "RUB":
        exchange_rate = get_exchange_rate(currency)
        amount *= exchange_rate

    return amount
