import json
from typing import List, Dict

def load_transactions(file_path: str) -> List[Dict]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):  # Проверяем, что данные - это список
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):  # Обрабатываем ошибку, если файл не найден или пуст
        return []

# Пример использования функции
if __name__ == "__main__":
    transactions = load_transactions('data/operations.json')
    print(transactions)
