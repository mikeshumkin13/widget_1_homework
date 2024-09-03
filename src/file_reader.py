import os
import pandas as pd
from typing import List, Dict, Any


os.chdir('/Users/a12345/Documents/projects_for_skypro/widget_1')


# Путь к CSV и Excel файлам в папке data
csv_file_path = "data/transactions.csv"
xls_file_path = "data/transactions_excel.xlsx"


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """Чтение финансовых операций из CSV-файла."""
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    """Чтение финансовых операций из Excel-файла."""
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")



transactions_from_csv = read_transactions_from_csv(csv_file_path)
transactions_from_excel = read_transactions_from_excel(xls_file_path)

print("Транзакции из CSV:")
print(transactions_from_csv)

print("Транзакции из Excel:")
print(transactions_from_excel)