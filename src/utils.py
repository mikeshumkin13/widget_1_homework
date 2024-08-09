import json
from typing import Dict, List

def load_operations(file_path: str = "data/operations.json") -> List[Dict]:
    """
    Загружает список транзакций из JSON-файла.

    :param file_path: Путь к JSON-файлу. По умолчанию используется "data/operations.json".
    :return: Список словарей с транзакциями, если файл существует и корректен, иначе пустой список.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    return []
