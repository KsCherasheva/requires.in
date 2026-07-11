# reqres-api-tests

Учебный проект API-автотестов для https://reqres.in

## Стек

- Python 3.11
- pytest — раннер тестов
- requests — HTTP-запросы к API

## Структура проекта

```
reqres-api-tests/
├── README.md
├── requirements.txt
├── pytest.ini
└── tests/
    └── test_users.py       # тесты на reqres.in
```

## Установка

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt --break-system-packages
```

## Запуск тестов

```bash
# все тесты
pytest -v

# один файл
pytest tests/test_users.py -v
```

## О проекте

Учебный проект для практики API-тестирования на reqres.in — простом
REST API с предсказуемыми ответами (GET/POST/PUT/DELETE на users,
register, login). Используется для отработки проверки статус-кодов
и структуры JSON-ответа без лишних сложностей UI-автоматизации.

## Что дальше

- Покрыть тестами основные эндпоинты: GET /users, GET /users/{id},
  POST /users, PUT /users/{id}, DELETE /users/{id}, POST /register,
  POST /login
- Добавить негативные кейсы (несуществующий id, регистрация без пароля)
- Когда тестов станет много — сгруппировать по файлам
  (test_users.py, test_auth.py)