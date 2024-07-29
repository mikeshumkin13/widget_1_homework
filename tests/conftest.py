import pytest


# Фикстура для предоставления примеров данных
@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-07-29T12:34:56.789"},
        {"id": 2, "state": "PENDING", "date": "2023-07-28T09:34:56.789"},
        {"id": 3, "state": "EXECUTED", "date": "2023-07-27T05:34:56.789"},
        {"id": 4, "state": "CANCELED", "date": "2023-07-26T03:34:56.789"},
        {"id": 5, "state": "EXECUTED", "date": "2023-07-25T01:34:56.789"},
    ]


@pytest.fixture
def mock_get_mask_account(mocker):
    return mocker.patch("src.widget.get_mask_account", return_value="**7890")


@pytest.fixture
def mock_get_mask_card_number(mocker):
    return mocker.patch("src.widget.get_mask_card_number", return_value="**** **** **** 5678")
