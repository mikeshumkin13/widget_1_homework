import pytest


# Фикстура для предоставления примеров данных
@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-07-29T12:34:56.789"},
        {"id": 2, "state": "PENDING", "date": "2023-07-28T09:34:56.789"},
        {"id": 3, "state": "EXECUTED", "date": "2023-07-27T05:34:56.789"},
        {"id": 4, "state": "CANCELED", "date": "2023-07-26T03:34:56.789"},
        {"id": 5, "state": "EXECUTED", "date": "2023-07-25T01:34:56.789"},
    ]


@pytest.fixture
def mock_get_mask_account(mocker):
    return mocker.patch("src.widget.get_mask_account", return_value="**7890")


@pytest.fixture
def mock_get_mask_card_number(mocker):
    return mocker.patch("src.widget.get_mask_card_number", return_value="**** **** **** 5678")



# Фикстура для генерации данных о транзакциях
@pytest.fixture
def transactions():
    return [
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

# Параметризация для генератора номеров карт
@pytest.fixture(params=[
    (1, 5, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]),
    (9999999999999995, 9999999999999999, [
        "9999 9999 9999 9995",
        "9999 9999 9999 9996",
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]),
    (1234567890123456, 1234567890123456, ["1234 5678 9012 3456"]),
])
def card_number_params(request):
    return request.param

