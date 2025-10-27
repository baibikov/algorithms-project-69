"""
Тестирование поискового движка
"""
from search_engine.search import Doc, search

def test_search_hello():
    docs = [
        Doc("1", "hello world"),
        Doc("2", "hi there"),
        Doc("3", "world hello"),
    ]
    assert search(docs, "hello") == ["1", "3"]

def test_search_not_found():
    docs = [Doc("1", "foo bar")]
    assert search(docs, "baz") == []


def test_search_exact_word():
    docs = [Doc("1", "cat cats caterpillar")]
    assert search(docs, "cat") == ["1"]


def test_search_empty():
    docs = []
    assert search(docs, "cat") == []


def test_search_full_empty():
    docs = []
    assert search(docs, "") == []


def test_search_with_space():
    docs = [
        Doc("1", "foo bar"),
    ]
    assert search(docs, " ") == []


def test_search_space():
    docs = [
        Doc("1", "      "),
    ]
    assert search(docs, " ") == []
