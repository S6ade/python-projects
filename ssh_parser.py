# Проект: Парсер логов SSH
# Цель: Проанализировать auth.log и найти подозрительную активность
# Использование: python3 ssh_parser.py auth.log

import sys  # для аргументов командной строки


# Проверяем, что пользователь передал путь к файлу
if len(sys.argv) < 2:
    print("Введите путь к файлу логов")
else:
    # Получаем путь из аргументов
    path = sys.argv[1]

    # Открываем файл и читаем все строки
    log_file = open(path, 'r', encoding='utf-8')
    read_log = log_file.readlines()

    # Словарь для подсчёта IP с неудачными попытками
    ip_count: dict[str, int] = {}

    # Счётчик успешных входов
    accepted_count = 0

    # Перебираем строки лога
    for line in read_log:
        # Если строка содержит Failed — это неудачная попытка
        if "Failed" in line:
            parts = line.split()
            ip = parts[10]  # IP находится на 11-й позиции (индекс 10)
            ip_count[ip] = ip_count.get(ip, 0) + 1

        # Если строка содержит Accepted — это успешный вход
        if "Accepted" in line:
            accepted_count += 1

    # Выводим отчёт
    print(f"Общее количество попыток: {len(read_log)}")
    print(
        f"Топ-5 IP с неудачными попытками: {sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:5]}")
    print(f"Количество успешных входов: {accepted_count}")
    print(f"Количество неудачных попыток: {sum(ip_count.values())}")
