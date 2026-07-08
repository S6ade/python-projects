from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Привет! Это API портволио s6ade"}


@app.get("/projects")
def get_projects():
    projects = [
        {"id": 1, "name": "Парсер логов", "skills": "sys.argv, словари, sorted"},
        {"id": 2, "name": "Генератор паролей",
            "skills": "random, string, аргументы"},
        {"id": 3, "name": "To-do в терминале",
            "skills": "while True, списки, enumerate"},
        {"id": 4, "name": "Камень-ножницы-бумага",
            "skills": "словарь правил, isdigit()"},
        {"id": 5, "name": "Калькулятор расходов",
            "skills": "datetime, файл, split()"},
    ]
    return {"projects": projects}


@app.get("/projects/{project_id}")
def get_project(project_id: int):
    """Возвращает один проект по его ID."""
    projects = {
        1: {"name": "Парсер логов", "skills": "sys.argv, словари, sorted", "description": "Анализирует access.log Nginx и выводит отчёт: топ IP, URL, статусы, ошибки 404 и 500."},
        2: {"name": "Генератор паролей", "skills": "random, string, аргументы", "description": "Генерирует пароль заданной длины и сложности (easy/medium/hard)."},
        3: {"name": "To-Do в терминале", "skills": "while True, списки, enumerate", "description": "Менеджер задач в терминале: добавление, просмотр, удаление."},
        4: {"name": "Камень-ножницы-бумага", "skills": "словарь правил, .isdigit()", "description": "Игра с раундами и подсчётом очков до N побед."},
        5: {"name": "Калькулятор расходов", "skills": "datetime, файлы, split()", "description": "Учёт трат с сохранением в файл и подсчётом общей суммы."},
    }

    if project_id in projects:
        return {"project": projects[project_id]}
    else:
        return {"error": "Проект не найден"}
