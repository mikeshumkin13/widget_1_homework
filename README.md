# Widget_for_bank

## Описание:

Widget_for_bank - Это виджет, который показывает несколько последних
успешных банковских операций клиента.  Этот проект на бэкенде будет 
готовить данные для отображения в новом виджете.

## Состав:
* пакет SRC содержит следующие модули:
    * mascs.py
    * processing.py
    * widget.py
    * external_api.py 
    * utils.py 
    * generators.py 
    * __init__.py
* пакет tests содержит модули с тестами к пакету src:
    * conftest.py
    * test_masks.py
    * test_processing.py
    * test_widget.py
    * test_external_api.py
    * test_generators.py
    * test_utils.py

## Установка:

1. Клонируйте репозиторий:
```
https://github.com/mikeshumkin13/widget_1_homework.git
```
## Установка зависимостей

для корректной работы программы установите зависимости:
-[tool.poetry]
name = "widget-1"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"
python-dotenv = "^1.0.1"
requests = "^2.32.3"


[tool.poetry.group.lint.dependencies]
flake8 = "^7.1.0"
black = "^24.4.2"
isort = "^5.13.2"
mypy = "^1.10.0"
pytest = "^8.2.2"


[tool.poetry.group.dev.dependencies]
pytest-cov = "^5.0.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.black]
line-length = 119

[tool.isort]
line_length = 119

[tool.mypy]
ignore_missing_imports = true
disallow_untyped_defs = true
warn_return_any = true

установка:
```
poetry install
```

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



# Модуль  external_api.py содержит функцию: def get_exchange_rate(currency: str) -> float:
которая получает текущий курс валюты по отношению к рублю.

# Модуль Utils.py содержит функцию: def load_operations(file_path: str = "data/operations.json") -> List[Dict]:
 которая загружает список транзакций из JSON-файла.
 
 
## Информация о тестировании:
для тестирования модулей содержащих функции, создан пакет "tests", который содержит модули с тестами.
для запуска тестирования выполните команду pytest.
информация о покрытии программы тестами содержится в файле "htmlcov".


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
