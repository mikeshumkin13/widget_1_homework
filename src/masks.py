import logging
from src.logger_config import logger

print("Начало выполнения masks.py")
logger.debug("Тестовый лог: начало выполнения скрипта masks.py")

# Настройка логгера для модуля
module_logger = logger.getChild('masks')

def get_mask_card_number(card_number: str) -> str:
    """Функция, которая возвращает маску номера карты по правилу XXXX XX** **** XXXX"""
    module_logger.debug(f"Получен номер карты для маскировки: {card_number}")

    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    module_logger.info(f"Замаскированный номер карты: {masked_card}")

    return masked_card

def get_mask_account(account_number: str) -> str:
    """Функция, которая возвращает маску номера счёта по правилу **XXXX"""
    module_logger.debug(f"Получен номер счёта для маскировки: {account_number}")

    masked_account = "*" * 2 + account_number[-4:]
    module_logger.info(f"Замаскированный номер счёта: {masked_account}")

    return masked_account
