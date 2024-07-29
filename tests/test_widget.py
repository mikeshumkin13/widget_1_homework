import pytest

from src.widget import get_data, mask_account_card


def test_mask_account_card_account(mock_get_mask_account):
    result = mask_account_card("счёт 12345678901234567890")
    assert result == "счёт **7890"
    mock_get_mask_account.assert_called_once_with("12345678901234567890")


def test_get_data():
    result = get_data("2023-07-29T12:34:56.789")
    assert result == "29.07.2023"
