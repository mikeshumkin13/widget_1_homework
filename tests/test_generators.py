import pytest


from src.generators import filter_by_currency, transaction_descriptions



# Пример данных транзакций
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 484579136,
        "state": "EXECUTED",
        "date": "2020-01-15T12:34:56.789123",
        "operationAmount": {
            "amount": "5000.00",
            "currency": {
                "name": "EUR",
                "code": "EUR"
            }
        },
        "description": "Оплата услуг",
        "from": "Счет 12345678901234567890",
        "to": "Счет 98765432109876543210"
    }
]


def test_filter_by_currency_usd():
    usd_transactions = filter_by_currency(transactions, "USD")
    result = list(usd_transactions)

    assert len(result) == 2
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"
    assert result[1]["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_eur():
    eur_transactions = filter_by_currency(transactions, "EUR")
    result = list(eur_transactions)

    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "EUR"


def test_filter_by_currency_no_transactions():
    jpy_transactions = filter_by_currency(transactions, "JPY")
    result = list(jpy_transactions)

    assert len(result) == 0


def test_filter_by_currency_stop_iteration():
    usd_transactions = filter_by_currency(transactions, "USD")
    try:
        for _ in range(3):  # Попробуем получить 3 транзакции, хотя их всего 2
            print(next(usd_transactions))
    except StopIteration:
        print("No more USD transactions available.")
    except Exception as e:
        pytest.fail(f"Unexpected exception {e}")


# Пример данных транзакций
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 484579136,
        "state": "EXECUTED",
        "date": "2020-01-15T12:34:56.789123",
        "operationAmount": {
            "amount": "5000.00",
            "currency": {
                "name": "EUR",
                "code": "EUR"
            }
        },
        "description": "Оплата услуг",
        "from": "Счет 12345678901234567890",
        "to": "Счет 98765432109876543210"
    }
]


def test_transaction_descriptions():
    descriptions = transaction_descriptions(transactions)
    result = list(descriptions)

    assert len(result) == 3
    assert result[0] == "Перевод организации"
    assert result[1] == "Перевод со счета на счет"
    assert result[2] == "Оплата услуг"


def test_transaction_descriptions_exhaustion():
    descriptions = transaction_descriptions(transactions)

    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Оплата услуг"

    # Попробуем получить еще одно описание после того, как генератор исчерпан
    try:
        next(descriptions)
        assert False, "Генератор должен был быть исчерпан"
    except StopIteration:
        pass