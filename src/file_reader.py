import pandas as pd
from typing import List, Dict, Any

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
