# Widjet_for_bank

## Описание:

Widjet_for_bank - Это виджет, который показывает несколько последних успешных банковских операций клиента.
этот проект на бэкенде будет готовить данные для отображения в новом виджете.

## Установка:

1. Клонируйте репозиторий:
```
[git clone https://github.com/username/project-x.git](https://github.com/mikeshumkin13/widget_1_homework.git)
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:
src/mascs.py
Функция 
get_mask_card_number
 принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате 
XXXX XX** **** XXXX
, где 
X
 — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами. Пример работы функции:
7000792289606361     # входной аргумент
7000 79** **** 6361  # выход функции
Функция 
get_mask_account
 принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате 
**XXXX
, где 
X
 — это цифра номера. То есть видны только последние 4 цифры номера, а перед ними — две звездочки. Пример работы функции:
73654108430135874305  # входной аргумент
**4305  # выход функции

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован https://my.sky.pro/
