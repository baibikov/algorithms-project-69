### Hexlet tests and linter status:
[![Actions Status](https://github.com/baibikov/algorithms-project-69/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/baibikov/algorithms-project-69/actions)

# Search Engine Project

Проект представляет собой поисковый движок, реализованный на Python.
Вся основная логика находится в папке `search_engine`.

---

## Структура проекта

```
algorithms-project-69/
│
├── search_engine/       # Основная логика поискового движка
├── requirements.txt     # Зависимости проекта
├── README.md
└── ...
```

---

## Установка локального окружения

Рекомендуется использовать Python 3.14+ и виртуальное окружение для изоляции зависимостей.

### 1. Клонировать репозиторий

```
git https://github.com/baibikov/algorithms-project-69.git
cd algorithms-project-69
```

### 2. Создать и активировать виртуальное окружение

**Linux / macOS**

```
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```
python -m venv venv
venv\Scripts\activate
```

### 3. Установить зависимости

```
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Запуск линтера

Для проверки качества кода используется `pylint`:

```
pylint search_engine
```

---

## Запуск тестов

Для тестирования проекта используется `pytest`:

```
pytest .
```

---

## Использование

Пример использования поискового движка:

```
from search_engine.search import search, Doc

docs = [
    Doc("1", "Привет я первый документ"),
    Doc("2", "Привет я второй документ")
]
query = "первый"
results = search(docs, query)
print(results) # ["1"]
```

---

## Контрибьюция

1. Форкните репозиторий
2. Создайте ветку `feature/имя_фичи`
3. Внесите изменения
4. Создайте Pull Request

---

