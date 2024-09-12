# Widget_for_bank

# Banking Transactions Processor

## Описание проекта

Программа предназначена для работы с банковскими транзакциями, включая их загрузку, фильтрацию и сортировку. Поддерживаются форматы JSON, CSV и XLSX. Программа позволяет фильтровать транзакции по статусу, дате, валюте и описанию.

## Функции программы

- Загрузка транзакций из файлов форматов JSON, CSV, и XLSX.
- Фильтрация транзакций по статусу (`EXECUTED`, `CANCELED`, `PENDING`).
- Дополнительная фильтрация по описанию (по ключевым словам).
- Сортировка транзакций по дате (по возрастанию или убыванию).
- Возможность отображать только рублевые транзакции.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://your-repo-url.git
    ```

2. Установите зависимости с помощью [Poetry](https://python-poetry.org/):

    ```bash
    cd widget_1
    poetry install
    ```

3. Убедитесь, что необходимые файлы с транзакциями (`operations.json`, `transactions.csv`, `transactions_excel.xlsx`) находятся в папке `data`.

## Запуск

Для запуска программы выполните следующую команду:

```bash
poetry run python src/main.py


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
    * logger_config.py
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

## Логирование в проекте

В данном проекте используется библиотека logging для создания и настройки логгирования. Логи записываются в файл и выводятся в консоль, что позволяет отслеживать важные события и ошибки в процессе выполнения программы.

Конфигурация логирования
В проекте создан общий конфигурационный файл для логгирования logger_config.py, расположенный в директории src/. Этот файл настраивает логирование для всех модулей проекта.

Файл src/logger_config.py:
import logging
import os

# Определение директории для хранения логов
log_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
os.makedirs(log_directory, exist_ok=True)

# Путь к файлу лога
log_file_path = os.path.join(log_directory, 'project.log')

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path, mode='w'),
        logging.StreamHandler()  # Также выводим логи в консоль
    ]
)

# Создание логгера для всего проекта
logger = logging.getLogger('widget_1')


Использование логгера в модулях
В каждом модуле проекта необходимо импортировать общий логгер из logger_config.py и использовать его для записи логов.

Пример в src/masks.py:
import logging
from src.logger_config import logger

def get_mask_card_number(card_number: str) -> str:
    logger.debug(f"Получен номер карты для маскировки: {card_number}")
    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info(f"Замаскированный номер карты: {masked_card}")
    return masked_card

def get_mask_account(account_number: str) -> str:
    logger.debug(f"Получен номер счёта для маскировки: {account_number}")
    masked_account = "*" * 2 + account_number[-4:]
    logger.info(f"Замаскированный номер счёта: {masked_account}")
    return masked_account


# Логи
Все логи записываются в файл logs/project.log и также выводятся в консоль. Файл лога перезаписывается при каждом запуске приложения.

Формат записи логов:
%(asctime)s - %(name)s - %(levelname)s - %(message)s

%(asctime)s: Время записи лога
%(name)s: Имя логгера
%(levelname)s: Уровень серьезности сообщения (DEBUG, INFO, WARNING, ERROR, CRITICAL)
%(message)s: Сообщение лога


## Работа с файлами форматов CSV и XLSX

В проект добавлена поддержка работы с файлами форматов CSV и XLSX, из которых можно считывать данные о финансовых транзакциях.

### Новый модуль: `file_reader.py`

В папке `src` создан модуль `file_reader.py`, содержащий функции для работы с файлами:

- `read_transactions_from_csv(filepath: str) -> List[Dict[str, Any]]`
  - Функция принимает путь к CSV-файлу и возвращает список словарей, представляющих собой транзакции.
  
- `read_transactions_from_excel(filepath: str) -> List[Dict[str, Any]]`
  - Функция принимает путь к XLSX-файлу и возвращает список словарей с транзакциями.

### Тестирование новых функций

Для новых функций были написаны тесты, которые находятся в файле `test_file_reader.py` в папке `tests`.

Тесты используют `pytest` и `unittest.mock` для имитации работы с файлами и проверки корректности возвращаемых данных.

### Типизация

Для всех новых функций добавлена типизация, что делает код более понятным и безопасным. Типы данных проверяются с помощью инструмента `mypy`, чтобы избежать ошибок на этапе написания кода.

### Зависимости

Для работы с файлами форматов CSV и XLSX используется библиотека `pandas`. Убедитесь, что она добавлена в зависимости проекта (`pyproject.toml`):

```toml
[tool.poetry.dependencies]
pandas = "^1.5"

##Структура проекта:

.
├── README.md
├── data
│   ├── operations.json
│   ├── transactions.csv
│   └── transactions_excel.xlsx
├── htmlcov
│   ├── class_index.html
│   ├── coverage_html_cb_6fb7b396.js
│   ├── favicon_32_cb_58284776.png
│   ├── function_index.html
│   ├── index.html
│   ├── keybd_closed_cb_ce680311.png
│   ├── status.json
│   ├── style_cb_8e611ae1.css
│   ├── z_145eef247bfb46b6___init___py.html
│   ├── z_145eef247bfb46b6_masks_py.html
│   ├── z_145eef247bfb46b6_processing_py.html
│   └── z_145eef247bfb46b6_widget_py.html
├── logs
│   └── project.log
├── poetry.lock
├── pyproject.toml
├── src
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── decorators.cpython-312.pyc
│   │   ├── external_api.cpython-312.pyc
│   │   ├── file_reader.cpython-312.pyc
│   │   ├── generators.cpython-312.pyc
│   │   ├── logger_config.cpython-312.pyc
│   │   ├── masks.cpython-312.pyc
│   │   ├── operations_filter.cpython-312.pyc
│   │   ├── processing.cpython-312.pyc
│   │   ├── utils.cpython-312.pyc
│   │   └── widget.cpython-312.pyc
│   ├── external_api.py
│   ├── file_reader.py
│   ├── generators.py
│   ├── logger_config.py
│   ├── main.py
│   ├── masks.py
│   ├── operations_filter.py
│   ├── processing.py
│   ├── utils.py
│   └── widget.py
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-312.pyc
    │   ├── conftest.cpython-312-pytest-8.2.2.pyc
    │   ├── test_decorators.cpython-312-pytest-8.2.2.pyc
    │   ├── test_external_api.cpython-312-pytest-8.2.2.pyc
    │   ├── test_external_api.cpython-312.pyc
    │   ├── test_file_reader.cpython-312-pytest-8.2.2.pyc
    │   ├── test_generators.cpython-312-pytest-8.2.2.pyc
    │   ├── test_masks.cpython-312-pytest-8.2.2.pyc
    │   ├── test_operations_filter.cpython-312-pytest-8.2.2.pyc
    │   ├── test_processing.cpython-312-pytest-8.2.2.pyc
    │   ├── test_utils.cpython-312-pytest-8.2.2.pyc
    │   └── test_widget.cpython-312-pytest-8.2.2.pyc
    ├── conftest.py
    ├── test_external_api.py
    ├── test_file_reader.py
    ├── test_generators.py
    ├── test_masks.py
    ├── test_operations_filter.py
    ├── test_processing.py
    ├── test_utils.py
    └── test_widget.py


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
