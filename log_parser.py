# Проект: Парсер логов Nginx
# Цель: Анализ access.log и вывод отчёта (топ IP, URL, статусы, ошибки)
# Использование: python3 log_parser.py access.log

import sys


# --- 1. Получаем путь к файлу ---
path = sys.argv[1]

# Проверяем, что путь передан
if len(sys.argv) < 2:
    print("Не передали путь к log-файлу")
    exit(1)


# --- 2. Читаем файл ---
with open(path, 'r') as log:
    log_lines = log.readlines()    # список всех строк

lines = len(log_lines)             # общее количество строк
print(f"Всего строк в логе: {lines}")


# --- 3. Готовим структуры для подсчёта ---
ip_count: dict[str, int] = {}     # словарь: IP → количество запросов
url_count: dict[str, int] = {}     # словарь: URL → количество запросов
status_count: dict[str, int] = {}  # словарь: статус-код → количество

count_404 = 0      # счётчик ошибок 404
count_500 = 0      # счётчик ошибок 500


# --- 4. Основной цикл: разбор каждой строки лога ---
for line in log_lines:
    parts = line.split()  # разбиваем строку по пробелам

    # Извлекаем данные по индексам
    ip = parts[0]                         # IP-адрес (первый элемент)
    # URL (седьмой элемент, после метода GET/POST)
    url = parts[6]
    status = parts[8]                     # HTTP-статус (девятый элемент)

    # Подсчитываем через .get(): если ключа нет — возвращаем 0, затем +1
    ip_count[ip] = ip_count.get(ip, 0) + 1
    url_count[url] = url_count.get(url, 0) + 1
    status_count[status] = status_count.get(status, 0) + 1

    # Отдельно считаем ошибки
    if status == "404":
        count_404 += 1
    elif status == "500":
        count_500 += 1


# --- 5. Сортировка ---
# sorted() с key=lambda x: x[1] сортирует по значению (количеству)
# reverse=True — по убыванию (самые частые сверху)
sorted_ip = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)
top10_ip = sorted_ip[:10]  # первые 10

sorted_url = sorted(url_count.items(), key=lambda x: x[1], reverse=True)
top10_url = sorted_url[:10]

sorted_status = sorted(status_count.items(), key=lambda x: x[1], reverse=True)
top10_status = sorted_status[:10]


# --- 6. Запись отчёта в файл ---
with open('report.txt', 'w') as report:
    report.write("=== Отчёт по логам ===\n")
    report.write(f"Всего запросов: {lines}\n\n")

    report.write("Топ-10 IP:\n")
    for ip, count in top10_ip:
        report.write(f"{ip} — {count} запросов\n")

    report.write("\nТоп-10 URL:\n")
    for url, count in top10_url:
        report.write(f"{url} — {count} запросов\n")

    report.write("\nСтатусы:\n")
    for status, count in top10_status:
        report.write(f"{status} — {count} запросов\n")


# --- 7. Вывод отчёта на экран ---
print("=== Отчёт по логам ===")
print(f"Всего запросов: {lines}")

print(f"\nТоп-10 IP:")
for ip, count in top10_ip:
    print(f"{ip} — {count} запросов")

print(f"\nТоп-10 URL:")
for url, count in top10_url:
    print(f"{url} — {count} запросов")

print(f"\nОшибок 404: {count_404}")
print(f"Ошибок 500: {count_500}")
print(f"Всего запросов: {lines}")

print("\nВсе статусы:")
for status, count in top10_status:
    print(f"{status} — {count} запросов")
