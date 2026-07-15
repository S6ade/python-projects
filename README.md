# Python Projects

Учебные проекты на Python, выполненные в рамках самостоятельного обучения.

## Проекты

| #   | Проект                | Навыки                                                           |
| --- | --------------------- | ---------------------------------------------------------------- |
| 1   | Парсер логов Nginx    | `sys.argv`, `.split()`, словари, `sorted`, `lambda`              |
| 2   | Генератор паролей     | `random`, `string`, аргументы командной строки, уровни сложности |
| 3   | To-Do в терминале     | `while True`, списки, `enumerate`, функции, меню                 |
| 4   | Камень-ножницы-бумага | Словарь правил, `.isdigit()`, игра до N побед, подсчёт очков     |
| 5   | Калькулятор расходов  | `datetime`, чтение/запись файлов, `split()`, словари             |
| 6   | FastAPI для портфолио | FastAPI, uvicorn, JSON, REST API, Swagger                        |
| 7   | Калькулятор IP-подсетей | `ipaddress`, `sys.argv`, `IPv4Network`                         |
| 8   | Парсер логов SSH      | `sys.argv`, словари, `sorted`, `lambda`, парсинг логов           |

## Технологии

- Python 3.14
- Стандартные библиотеки: `sys`, `random`, `string`, `datetime`
- Docker
- FastAPI + Uvicorn
- Swagger (автодокументация)
- 
## Структура репозитория
```
├── .github/
│   └── workflows/
│       └── test.yml       # CI/CD: автотесты и линтер
├── log_parser.py          # Парсер логов Nginx
├── pass_gen.py            # Генератор паролей
├── todo.py                # To-Do в терминале
├── game_rps.py            # Игра камень-ножницы-бумага
├── calculate.py           # Калькулятор расходов
├── subnet_calc.py         # Калькулятор IP-подсетей
├── ssh_parser.py          # Парсер логов SSH
├── api.py                 # FastAPI для портфолио
├── Dockerfile             # Docker-образ для FastAPI
├── requirements.txt       # Зависимости (будет позже)
└── README.md
```
## Автор

s6ade
