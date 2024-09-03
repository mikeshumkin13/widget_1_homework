import json
import logging
from typing import Dict, List
from src.logger_config import logger

# Настройка логгера для модуля
module_logger = logger.getChild("utils")


def load_operations(file_path: str = "data/operations.json") -> List[Dict]:
    """
    Загружает список транзакций из JSON-файла.

    :param file_path: Путь к JSON-файлу. По умолчанию используется "data/operations.json".
    :return: Список словарей с транзакциями, если файл существует и корректен, иначе пустой список.
    """
    try:
        module_logger.debug(f"Загрузка операций из файла: {file_path}")
        with open(file_path, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                module_logger.info(f"Успешная загрузка {len(data)} операций")
                return data
    except FileNotFoundError:
        module_logger.error(f"Файл не найден: {file_path}")
    except json.JSONDecodeError:
        module_logger.error(f"Ошибка декодирования JSON в файле: {file_path}")

    module_logger.warning("Возвращен пустой список операций")
    return []
