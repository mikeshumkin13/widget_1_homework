import logging
from src.logger_config import logger


# Настройка логгера для модуля
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая возвращает маску номера карты по правилу XXXX XX** **** XXXX"""
    logger.debug(f"Получен номер карты для маскировки: {card_number}")

    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info(f"Замаскированный номер карты: {masked_card}")

    return masked_card


def get_mask_account(account_number: str) -> str:
    """Функция, которая возвращает маску номера счёта по правилу **XXXX"""
    logger.debug(f"Получен номер счёта для маскировки: {account_number}")

    masked_account = "*" * 2 + account_number[-4:]
    logger.info(f"Замаскированный номер счёта: {masked_account}")

    return masked_account