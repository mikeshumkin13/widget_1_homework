import re
from typing import List, Dict, Any


def filter_operations_by_description(operations: List[Dict[str, Any]], search_term: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список операций, возвращая те, у которых в описании содержится поисковая строка.

    :param operations: Список операций (словари), каждый из которых содержит данные об операции.
    :param search_term: Строка поиска, которая будет искаться в описании операции.
    :return: Список операций, описание которых содержит строку поиска.
    """
    filtered_operations = []

    for operation in operations:
        description = operation.get("description", "")

        # Поиск строки поиска в описании с игнорированием регистра
        if re.search(search_term, description, re.IGNORECASE):
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

