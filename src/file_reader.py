import pandas as pd
from typing import List, Dict, Any


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """Чтение финансовых операций из CSV-файла."""
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    """Чтение финансовых операций из Excel-файла."""
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')
