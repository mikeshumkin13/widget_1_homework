import pytest

from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number("9876543210987654") == "9876 54** **** 7654"


@pytest.mark.parametrize("account, expected", [
    ("73654108430135874305", "**4305"),
    ("72954141430135305679", "**5679"),
    ("98765432109876543210", "**3210")
])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected
