def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    # Получаем выбор пользователя
    choice = input("Пожалуйста, введите номер пункта меню (1, 2 или 3): ")

    # Обработка выбора
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        # Здесь мы будем загружать и обрабатывать JSON-файл
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        # Здесь мы будем загружать и обрабатывать CSV-файл
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        # Здесь мы будем загружать и обрабатывать XLSX-файл
    else:
        print("Некорректный выбор. Попробуйте снова.")

    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    status = input("Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ").upper()

    while status not in available_statuses:
        print(f'Статус операции "{status}" недоступен.')
        status = input("Введите корректный статус: ").upper()

    print(f'Операции отфильтрованы по статусу "{status}".')

    # Шаг 3: Запрос на сортировку
    sort_by_date = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()

    if sort_by_date == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        if sort_order == "по возрастанию":
            print("Операции отсортированы по возрастанию.")
            # Здесь будет логика сортировки по возрастанию
        elif sort_order == "по убыванию":
            print("Операции отсортированы по убыванию.")
            # Здесь будет логика сортировки по убыванию
        else:
            print("Некорректный выбор сортировки. Пропускаем сортировку.")

    # Шаг 4: Фильтр по валюте
    ruble_transactions_only = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if ruble_transactions_only == "да":
        print("Будут выведены только рублевые транзакции.")
        # Здесь будет логика фильтрации только рублевых транзакций


if __name__ == "__main__":
    main()

