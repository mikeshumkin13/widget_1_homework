from unittest.mock import patch
from src.external_api import convert_to_rub

def test_convert_to_rub():
    # Замена реального вызова API фиктивными данными
    with patch('src.external_api.get_exchange_rate', return_value=75.0):
        transaction = {"amount": 100.0, "currency": "USD"}
        result = convert_to_rub(transaction)
        assert result == 7500.0


