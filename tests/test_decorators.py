import pytest
from src.decorators import log

@log()
def divide(a: int, b: int) -> int:
    return a // b

def test_divide_success(capsys):
    divide(10, 2)
    captured = capsys.readouterr()
    assert "Function divide started." in captured.out
    assert "Function divide completed successfully. Result: 5" in captured.out

def test_divide_zero_division(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    captured = capsys.readouterr()
    assert "Function divide started." in captured.out
    assert "Function divide failed with error: integer division or modulo by zero. Inputs: (10, 0), {}" in captured.out
