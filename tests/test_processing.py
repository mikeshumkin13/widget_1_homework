from datetime import datetime

import pytest

from src.processing import filter_by_state, sort_by_date


# Тест функции filter_by_state
def test_filter_by_state(sample_data):
    executed_operations = filter_by_state(sample_data)
    assert len(executed_operations) == 3
    assert all(op["state"] == "EXECUTED" for op in executed_operations)

    pending_operations = filter_by_state(sample_data, state="PENDING")
    assert len(pending_operations) == 1
    assert pending_operations[0]["state"] == "PENDING"


# Тест функции sort_by_date
def test_sort_by_date(sample_data):
    sorted_operations = sort_by_date(sample_data)
    dates = [datetime.strptime(op["date"], "%Y-%m-%dT%H:%M:%S.%f") for op in sorted_operations]
    assert dates == sorted(dates, reverse=True)

    sorted_operations_asc = sort_by_date(sample_data, is_sort_reverse=False)
    dates_asc = [datetime.strptime(op["date"], "%Y-%m-%dT%H:%M:%S.%f") for op in sorted_operations_asc]
    assert dates_asc == sorted(dates_asc)
