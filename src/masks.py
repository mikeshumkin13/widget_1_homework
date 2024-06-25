def get_mask_card_number(card_number: str) -> str:
    """функция, которая возвращает маску номера карты по правилу XXXX XX** **** XXXX"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """функция, которая возвращает маску номера счёта по правилу **XXXX"""

    masked_account = "*" * 2 + account_number[-4:]
    return masked_account
