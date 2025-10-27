"""
Модуль search_engine
Содержит классы и функции для работы с поисковым движком.
"""
from dataclasses import dataclass


@dataclass
class Doc:
    """
    Типизированная стркутра представления документа.

    Attributes:
        id (str): Идентификатор документа
        text (str): Текстовая содержимое документа
    """
    id: str
    text: str


def search(docs: list[Doc], word: str) -> list[str]:
    """
    Поиск документов по точному совпадению.
    Проверяется наличие слова в тексте документа.

    Args:
        docs (list[Doc]): Документы над которыми производится поиск.
        word (str): Запрос на поиск документов.

    Returns:
        list[str].

    Examples:
        >>> search([Doc("1", "foo bar")], "foo")
        ["1"]
        >>> search([Doc("1", "foo bars")], "bar")
        []
    """
    word = word.replace(" ", "").lower()
    if word == "":
        return []

    return [
        doc.id
        for doc in docs
        if word in doc.text.lower().split(" ")
    ]
