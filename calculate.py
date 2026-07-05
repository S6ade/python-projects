# Проект: Калькулятор расходов
# Цель: Учёт трат с сохранением в файл. Можно добавлять, просматривать,
#        удалять записи и считать общую сумму расходов.
# Формат хранения в файле: дата|товар|сумма

from datetime import datetime


# --- Меню ---
def show_menu():
    """Отображает главное меню с доступными действиями"""
    print("======МЕНЮ======")
    print("1. Добавить")
    print("2. Показать")
    print("3. Удалить")
    print("4. Сумма")
    print("5. Выйти")


# Список для хранения расходов (каждый элемент — словарь с датой, товаром и ценой)
expense: list[dict[str, object]] = []


def menu():
    """Основная функция: загружает данные из файла и управляет меню"""

    # --- Загрузка данных из файла при запуске ---
    # Если файла ещё нет — просто начинаем с пустым списком
    try:
        with open('expenses.txt', 'r') as f:
            for line in f:
                line = line.strip()          # убираем пробелы и перевод строки
                if line:                     # пропускаем пустые строки
                    date, article, price = line.split(
                        '|')   # разбиваем по разделителю
                    expense.append({
                        "date": date,
                        "article": article,
                        # цену храним как число для подсчёта
                        "price": int(price)
                    })
    except FileNotFoundError:
        pass  # файла ещё нет при первом запуске

    # --- Основной цикл ---
    while True:
        show_menu()
        choice = input("Выбери: ")

        # 1. Добавление расхода
        if choice == "1":
            user_article = input("Введите название товара: ")
            user_price = input("Введите сумму товара: ")

            # Создаём запись с текущей датой
            log_entry = {
                "date": datetime.now().isoformat(),
                "article": user_article,
                "price": int(user_price)
            }
            expense.append(log_entry)        # добавляем в список

            # Дописываем одну строку в файл (режим 'a' — append)
            with open('expenses.txt', 'a') as f:
                f.write(
                    f"{log_entry['date']}|{log_entry['article']}|{log_entry['price']}\n")

        # 2. Просмотр всех расходов
        elif choice == "2":
            print("Ваш список расходов")
            if not expense:
                print("Ваш список пуст")
            else:
                print("Твой список:")
                for i, item in enumerate(expense, 1):
                    print(f"{i}. {item}")

        # 3. Удаление расхода по номеру
        elif choice == "3":
            print("Твой список")
            for i, item in enumerate(expense, 1):
                print(f"{i}. {item}")

            removed_task = input("Какую задачу удаляем? ")
            # пользователь вводит номер, а индекс с 0
            index = int(removed_task) - 1

            if 0 <= index < len(expense):
                expense.pop(index)           # удаляем из списка

                # Полностью перезаписываем файл (режим 'w' — write)
                with open('expenses.txt', 'w') as f:
                    for item in expense:
                        f.write(
                            f"{item['date']}|{item['article']}|{item['price']}\n")
            else:
                print("Выбранное число за пределами списка задач")

        # 4. Подсчёт общей суммы
        elif choice == "4":
            total = 0
            for item in expense:
                total += item["price"]
            print(f"Общая сумма расходов: {total}")

        # 5. Выход
        else:
            print("До свидания")
            break


# Точка входа
if __name__ == "__main__":
    menu()
