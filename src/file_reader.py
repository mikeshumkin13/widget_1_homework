import os
import json
import pandas as pd
from typing import List, Dict, Any

# Определите базовую директорию, где находится этот файл
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Путь к CSV и Excel файлам в папке data
csv_file_path = os.path.join(BASE_DIR, "../data/transactions.csv")
xls_file_path = os.path.join(BASE_DIR, "../data/transactions_excel.xlsx")
json_file_path = os.path.join(BASE_DIR, "../data/operations.json")


def read_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """Чтение финансовых операций из JSON-файла."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """Чтение финансовых операций из CSV-файла."""
    df = pd.read_csv(file_path, delimiter=";")
    return df.to_dict(orient="records")


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    """Чтение финансовых операций из Excel-файла."""
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")


# Примеры использования
if __name__ == "__main__":
    transactions_from_json = read_transactions_from_json(json_file_path)
    transactions_from_csv = read_transactions_from_csv(csv_file_path)
    transactions_from_excel = read_transactions_from_excel(xls_file_path)

    print("Транзакции из JSON:")
    print(transactions_from_json)

    print("Транзакции из CSV:")
    print(transactions_from_csv)

    print("Транзакции из Excel:")
    print(transactions_from_excel)
