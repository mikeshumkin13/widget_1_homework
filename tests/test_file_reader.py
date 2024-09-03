import pytest
from unittest.mock import patch, MagicMock
from src.file_reader import read_transactions_from_csv, read_transactions_from_excel


@patch('src.file_reader.pd.read_csv')
def test_read_transactions_from_csv(mock_read_csv):
    """
    Тест проверяет, корректно ли функция read_transactions_from_csv
    считывает данные из CSV-файла и возвращает список словарей с транзакциями.
    """
    mock_data = MagicMock()
    mock_read_csv.return_value = mock_data
    mock_data.to_dict.return_value = [{'id': 1, 'amount': 100}]

    result = read_transactions_from_csv('dummy_path.csv')

    assert result == [{'id': 1, 'amount': 100}]
    mock_read_csv.assert_called_once_with('dummy_path.csv')


@patch('src.file_reader.pd.read_excel')
def test_read_transactions_from_excel(mock_read_excel):
    """
    Тест проверяет, корректно ли функция read_transactions_from_excel
    считывает данные из Excel-файла и возвращает список словарей с транзакциями.
    """
    mock_data = MagicMock()
    mock_read_excel.return_value = mock_data
    mock_data.to_dict.return_value = [{'id': 1, 'amount': 100}]

    result = read_transactions_from_excel('dummy_path.xlsx')

    assert result == [{'id': 1, 'amount': 100}]
    mock_read_excel.assert_called_once_with('dummy_path.xlsx')
