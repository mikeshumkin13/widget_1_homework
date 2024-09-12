import os
from file_reader import read_transactions_from_csv, read_transactions_from_excel, read_transactions_from_json
from operations_filter import filter_operations_by_status, filter_operations_by_description

def get_file_path(file_name: str) -> str:
    """
    Возвращает полный путь к файлу, основываясь на относительном пути.

    :param file_name: Имя файла.
    :return: Полный путь к файлу.
    """
    return os.path.join(os.path.dirname(__file__), '..', 'data', file_name)

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пожалуйста, введите номер пункта меню (1, 2 или 3): ").strip()

    transactions = []

    if choice == "1":
        file_path = get_file_path("operations.json")
        transactions = read_transactions_from_json(file_path)
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        file_path = get_file_path("transactions.csv")
        transactions = read_transactions_from_csv(file_path)
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        file_path = get_file_path("transactions_excel.xlsx")
        transactions = read_transactions_from_excel(file_path)
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор. Завершение программы.")
        return

    # Выводим информацию о загруженных транзакциях
    print(f"Загруженные транзакции ({len(transactions)}):")
    for tx in transactions:
        print(tx)

    status = (
        input("Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ")
        .strip()
        .upper()
    )
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}

    if status not in valid_statuses:
        print(f'Статус операции "{status}" недоступен.')
        return

    # Добавляем отладочные сообщения перед и после фильтрации по статусу
    print(f"Фильтрация по статусу: {status}")
    transactions = filter_operations_by_status(transactions, status)

    # Выводим информацию о транзакциях после фильтрации
    print(f"Транзакции после фильтрации по статусу ({len(transactions)}):")
    for tx in transactions:
        print(tx)

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    sort_option = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_option == "да":
        ascending = input("Отсортировать по возрастанию или по убыванию? ").strip().lower() == "по возрастанию"
        transactions = sorted(transactions, key=lambda x: x["date"], reverse=not ascending)

    currency_filter = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_filter == "да":
        transactions = [tx for tx in transactions if tx.get("currency_name", "") == "руб"]

    description_filter = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    )
    if description_filter == "да":
        search_term = input("Введите слово для фильтрации в описании: ").strip()
        transactions = filter_operations_by_description(transactions, search_term)

    print("Распечатываю итоговый список транзакций...")

    if transactions:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for tx in transactions:
            date = tx.get("date", "")
            description = tx.get("description", "")
            amount = tx.get("amount", 0)
            currency = tx.get("currency_name", "unknown currency")
            print(f"\nДата: {date}")
            print(f"Описание: {description}")
            print(f"Сумма: {amount} {currency}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

if __name__ == "__main__":
    main()
