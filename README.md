# My First Site — учебный интернет-магазин

Мини-сайт с каталогом товаров, созданный **в учебных целях** для отработки
разных видов автоматизированного тестирования: white-box и black-box.

## 📌 О проекте

Простой интернет-магазин на Django с авторизацией, каталогом товаров и БД
(PostgreSQL / SQLite для локальной разработки). При написании кода
использовались принципы **OOP, DRY, KISS**.

На проекте отрабатываются:
- **White-box тесты** — модульные тесты моделей, форм, схем (Pydantic),
  запросов к БД;
- **Black-box тесты** — UI-тесты через Playwright (авторизация, каталог)
  и API-тесты;
- **Нагрузочное тестирование** — через Locust;
- **Покрытие кода** — отчёты coverage (`htmlcov/`).

## 🛠 Стек

- **Backend:** Django, Pydantic (схемы/валидация)
- **БД:** PostgreSQL (прод) / SQLite (локально)
- **Тестирование:** pytest, Playwright, Locust, coverage

## 📁 Структура проекта

```
my_first_site/
├── catalog/                    # Основное приложение (каталог товаров)
│   ├── migrations/              # Миграции БД
│   ├── templates/catalog/       # HTML-шаблоны (base, home, login, register)
│   ├── tests/                   # Все тесты приложения
│   │   ├── api_test/             # White-box: тесты моделей, логики, форм
│   │   ├── SQL_test/             # White-box: тесты запросов/данных в БД
│   │   ├── UI_tests/             # Black-box: UI-тесты (Playwright)
│   │   └── load_tests/           # Нагрузочные тесты (Locust)
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── schemas.py               # Pydantic-схемы
│   ├── urls.py
│   └── views.py
├── config/                     # Настройки Django-проекта
├── htmlcov/                    # HTML-отчёт покрытия кода (генерируется)
├── manage.py
├── pytest.ini
├── requirements.txt
├── db.sqlite3                  # Локальная БД для разработки
├── .env                        # Переменные окружения (не в репозитории)
└── README.md
```

## 🚀 Запуск локально

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

## ✅ Тестирование

```bash
# все тесты
pytest

# только white-box (модели, API, БД)
pytest catalog/tests/api_test catalog/tests/SQL_test

# только black-box (UI через Playwright)
pytest catalog/tests/UI_tests

# отчёт покрытия
coverage run -m pytest
coverage html   # результат в htmlcov/
```

### Нагрузочное тестирование

```bash
locust -f catalog/tests/load_tests/locustfile.py
```

## 📌 Заметки

- Проект учебный — фокус на структуре тестов, а не на продакшн-готовности кода.
- `.env`, `db.sqlite3`, `venv/`, `htmlcov/`, `.pytest_cache/` — не хранятся в
  репозитории (см. `.gitignore`).