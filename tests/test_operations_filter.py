import pytest
from src.operations_filter import filter_operations_by_description


def test_filter_operations_by_description():
    operations = [
        {"id": 1, "description": "Оплата услуг", "amount": 1000},
        {"id": 2, "description": "Перевод на счет", "amount": 5000},
        {"id": 3, "description": "Оплата мобильной связи", "amount": 200},
        {"id": 4, "description": "Покупка продуктов", "amount": 1500},
    ]

    result = filter_operations_by_description(operations, "оплата")
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3

    result = filter_operations_by_description(operations, "перевод")
    assert len(result) == 1
    assert result[0]["id"] == 2

    result = filter_operations_by_description(operations, "страховка")
    assert len(result) == 0
