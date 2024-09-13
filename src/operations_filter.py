import re
from typing import List, Dict, Any


def filter_operations_by_status(operations: List[Dict[str, Any]], status: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по статусу.

    :param operations: Список операций (словари), каждый из которых содержит данные об операции.
    :param status: Статус для фильтрации.
    :return: Список операций, которые соответствуют заданному статусу.
    """
    return [operation for operation in operations if operation.get("state", "").upper() == status]



def filter_operations_by_description(operations: List[Dict[str, Any]], search_term: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список операций, возвращая те, у которых в описании содержится поисковая строка.

    :param operations: Список операций (словари), каждый из которых содержит данные об операции.
    :param search_term: Строка поиска, которая будет искаться в описании операции.
    :return: Список операций, описание которых содержит строку поиска.
    """
    search_term = search_term.lower()
    filtered_operations = []

    for operation in operations:
        description = operation.get("description", "")

        # Проверяем, что description является строкой
        if isinstance(description, str) and search_term in description.lower():
            filtered_operations.append(operation)

    return filtered_operations


def count_operations_by_category(operations: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций для каждой категории на основе описания.

    :param operations: Список операций (словари).
    :param categories: Список категорий для поиска в описаниях.
    :return: Словарь, где ключ — категория, а значение — количество операций.
    """
    category_count = {category: 0 for category in categories}

    for operation in operations:
        description = operation.get("description", "").lower()

        for category in categories:
            if category.lower() in description:
                category_count[category] += 1

    return category_count
