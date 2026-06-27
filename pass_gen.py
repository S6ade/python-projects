# Проект: Генератор паролей
# Цель: Генерация случайного пароля заданной длины и уровня сложности
# Использование: python3 pass_gen.py [длина] [уровень]
#   длина  — число (по умолчанию 12)
#   уровень — easy / medium / hard (по умолчанию easy)

# Импортируем модули
import sys        # для работы с аргументами командной строки
import random     # для случайного выбора символов
import string     # для наборов символов (буквы, цифры, знаки)


# --- 1. Получаем длину пароля ---
# Если аргумент не передан — используем 12 по умолчанию
if len(sys.argv) < 2:
    print("Размер пароля по умолчанию (12)")
    length = 12
else:
    # Преобразуем строку в число
    length = int(sys.argv[1])


# --- 2. Получаем уровень сложности ---
# Если второй аргумент не передан — easy
if len(sys.argv) < 3:
    level = "easy"
else:
    level = sys.argv[2]


# --- 3. Формируем набор символов в зависимости от уровня ---
if level == "easy":
    # Только строчные буквы
    chars = string.ascii_lowercase
elif level == "medium":
    # Строчные буквы + цифры
    chars = string.ascii_lowercase + string.digits
else:
    # Буквы (строчные + заглавные) + цифры + спецсимволы
    chars = string.ascii_letters + string.digits + string.punctuation


# --- 4. Генерация пароля ---
password = ""  # пустая строка-аккумулятор

# Собираем пароль по одному случайному символу из chars
for _ in range(length):
    password += random.choice(chars)

# Выводим результат
print(password)
