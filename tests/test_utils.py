from src.utils import load_operations


def test_load_operations(tmp_path):
    # Создание временного JSON-файла для теста
    file_path = tmp_path / "operations.json"
    file_path.write_text('[{"id": 1, "amount": 100.0, "date": "2023-08-09", "description": "Payment"}]')

    # Вызов функции с передачей пути к файлу
    result = load_operations(str(file_path))

    # Проверка корректности результата
    assert len(result) == 1
    assert result[0]['id'] == 1

    # Тест на пустой файл
    empty_file_path = tmp_path / "empty_operations.json"
    empty_file_path.write_text('')

    result = load_operations(str(empty_file_path))
    assert result == []
