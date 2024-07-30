# Widget_for_bank

## Описание:

Widget_for_bank - Это виджет, который показывает несколько последних
успешных банковских операций клиента.  Этот проект на бэкенде будет 
готовить данные для отображения в новом виджете.

## Состав:
* пакет SRC содержит следующие модули:
    *mascs.py
    *processing.py
    *widget.py
    *__init__.py
* пакет tests содержит модули с тестами к пакету src:
    *conftest.py
    *test_masks.py
    *test_processing.py
    *test_widget.py

## Установка:

1. Клонируйте репозиторий:
```
https://github.com/mikeshumkin13/widget_1_homework.git
```
##Установка зависимостей

для корректной работы программы установите зависимости:
-python = "^3.12"
-flake8 = "^7.1.0"
-black = "^24.4.2"
-isort = "^5.13.2"
-mypy = "^1.10.0"

установка:
```
poetry install
```

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

# Модуль Generators

## Обзор

Этот модуль предоставляет различные генераторные функции для фильтрации и обработки данных транзакций, а также для генерации форматированных номеров карт.

## Функции

### `filter_by_currency`

**Описание**: Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданному коду валюты.

**Использование**:
```python
transactions = [
    {
        "id": 1,
        "operationAmount": {"amount": "100.00", "currency": {"code": "USD"}},
        "description": "Транзакция 1"
    },
    {
        "id": 2,
        "operationAmount": {"amount": "200.00", "currency": {"code": "EUR"}},
        "description": "Транзакция 2"
    }
]
usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)




## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован и создан по заказу SKYPRO. 
https://sky.pro/main-new?utm_
source=yandex&utm_medium=cpc&utm_campaign=n_brand_search_main_ru_yandex_
93946323%7Cpl_search%7Cpr_171%7Cta_cold%7Cfu_main_landing%7Cma_academtraff%7Cown_b2c%7Cchg
_performance&utm_content=ai_14894857226%7Cagi_5270901781%7Cci_93946323%7Cpi_46704583444%7Cse_
none&utm_term=search%7Ckwd_скайпро=&roistat=direct1_search_14894857226_скайпро&roistat_
referrer=none&roistat_pos=premium_1&etext=&yclid=3939331037279551487#giftpopup
