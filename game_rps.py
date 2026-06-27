# Проект по игре камень ножницы бумага
# Цель проекта Реализовать игру с подсчетом количества раундов и в конце выявить кто победил

import random


print("Приветствую в игру камень ножницы бумага!!!")

# 1. Добавляем элементы для игры и добавляем словарь c информацией об игре
items = ["камень", "ножницы", "бумага"]
rules = {"камень": "ножницы", "ножницы": "бумага", "бумага": "камень"}

# 2. Добавляем начальный счет
user_score = 0
computer_score = 0

# 3. Выносим в цикл колличесвто раундов и проверку на корректный ввод игрока
while True:
    ask_total_raund = input("Сколько раундов будем играть: ")
    if ask_total_raund.isdigit():
        num = int(ask_total_raund)
        print(f"количество раундов: {ask_total_raund} ")
        break
    else:
        print("Вы не ввели количество раундов")

# 4. Сохраняем общее количество раундов
rounds_total = int(ask_total_raund)


# 5. Прописываем логику игры. Реализуем цикл где идет подсчет побед в раунде и вывод результата
while user_score < rounds_total and computer_score < rounds_total:
    computer_ask = random.choice(items)
    user_ask = input("Сделай свой выбор: ")
    if user_ask == computer_ask:
        print("Ничья")
    elif user_ask not in rules:
        print("Ты не правильно выбрал")
    elif rules[user_ask] == computer_ask:
        print("Ты победил")
        user_score += 1
    else:
        print("Ты проиграл")
        computer_score += 1
    print(f"Твой выбор: {user_ask}")
    print(f"Компьютер выбрал: {computer_ask}")
    print(f"Счет:{user_score} : {computer_score} ")


# 6. Выводим победителя матча
if user_score > computer_score:
    print(f"Ты победил со счетом {user_score} : {computer_score}")
else:
    print(f"Ты проиграл со счетом {user_score} : {computer_score}")
