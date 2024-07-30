def filter_by_currency(transactions, currency):
    """
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.
    """
    return (
        transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency
    )


def transaction_descriptions(transactions):
    """
    Возвращает генератор, который поочередно выдает описание каждой операции.
    """
    for transaction in transactions:
        yield transaction["description"]
