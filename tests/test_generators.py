import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тест с использованием фикстуры для данных транзакций
def test_filter_by_currency_usd(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    result = list(usd_transactions)

    assert len(result) == 2
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"
    assert result[1]["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_eur(transactions):
    eur_transactions = filter_by_currency(transactions, "EUR")
    result = list(eur_transactions)

    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "EUR"


def test_filter_by_currency_no_transactions(transactions):
    jpy_transactions = filter_by_currency(transactions, "JPY")
    result = list(jpy_transactions)

    assert len(result) == 0


def test_filter_by_currency_stop_iteration(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    try:
        for _ in range(3):  # Попробуем получить 3 транзакции, хотя их всего 2
            print(next(usd_transactions))
    except StopIteration:
        print("No more USD transactions available.")
    except Exception as e:
        pytest.fail(f"Unexpected exception {e}")


# Тест с использованием фикстуры для данных транзакций
def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    result = list(descriptions)

    assert len(result) == 3
    assert result[0] == "Перевод организации"
    assert result[1] == "Перевод со счета на счет"
    assert result[2] == "Оплата услуг"


def test_transaction_descriptions_exhaustion(transactions):
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


# Тест с параметризацией для генератора номеров карт
@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9999999999999995,
            9999999999999999,
            [
                "9999 9999 9999 9995",
                "9999 9999 9999 9996",
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
        (1234567890123456, 1234567890123456, ["1234 5678 9012 3456"]),
    ],
)
def test_card_number_generator_parametrized(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected
