from typing import List, Dict, Generator



def filter_by_currency(transactions: list[dict], currency: str) -> Generator[Dict, None, None]:
    """
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.
    """
    return (
        transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency
    )


def transaction_descriptions(transactions: List[dict]) -> Generator[str, None, None]:
    """
    Возвращает генератор, который поочередно выдает описание каждой операции.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        card_number = f"{number:016d}"  # Преобразуем число в строку длиной 16 символов с ведущими нулями
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number