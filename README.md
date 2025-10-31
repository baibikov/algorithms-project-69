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
├── tests/               # Тесты к публичному интерфейсу
├── uv.lock              # Зависимости проекта
├── README.md
└── ...
```

---

## Установка локального окружения

### 1. Клонировать репозиторий

```
git https://github.com/baibikov/algorithms-project-69.git
cd algorithms-project-69
```

### 2. Установить uv менеджером пакетов

**Linux / macOS**

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Установить зависимости

```
make install 
```

---

## Запуск линтера

Для проверки качества кода используется `ruff`:

```
make lint
```

---

## Запуск тестов

Для тестирования проекта используется `pytest`:

```
make test
```

---

## Использование

Пример использования поискового движка:

```
from search_engine import search, Document

docs = [
    Document("1", "Привет я первый документ"),
    Document("2", "Привет я второй документ")
]
results = search(docs, "первый")
assert results == ["1"]
```

---

## Контрибьюция

1. Форкните репозиторий
2. Создайте ветку `feature/имя_фичи`
3. Внесите изменения
4. Создайте Pull Request

---

