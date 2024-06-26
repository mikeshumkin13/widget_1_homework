from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Возвращает маску номера карты или счёта"""

    if "счёт" in card_info.lower():
        account_info_split = card_info.split(" ")
        return f"{account_info_split[0]} {get_mask_account(account_info_split[1])}"
    else:
        card_info_split = card_info.split(" ")
        return f"{' '.join(card_info_split[:-1])} {get_mask_card_number(card_info_split[-1])}"


def get_data(date_string: str) -> str:
    """Возвращает дату из строки"""

    cut_date = date_string[:10].split("-")
    return ".".join(cut_date[::-1])
