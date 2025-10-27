"""
Модуль search_engine
содержит классы и функции для работы с поисковым движком.
"""
import re
from dataclasses import dataclass


@dataclass
class Doc:
    """
    Типизированная структура представления документа.

    Attributes:
        id (str): Идентификатор документа
        text (str): Текстовая содержимое документа
    """
    id: str
    text: str


def search(docs: list[Doc], query: str) -> list[str]:
    """
    Поиск документов по точному совпадению.
    Проверяется наличие слова в тексте документа.

    Args:
        docs (list[Doc]): Документы над которыми производится поиск.
        query (str): Запрос на поиск документов.

    Returns:
        list[str].

    Examples:
        >>> search([Doc("1", "foo bar")], "foo")
        ["1"]
        >>> search([Doc("1", "foo bars")], "bar")
        []
    """

    processed_docs = _preprocessing(docs)
    query_tokens = _preprocessing_text(query)

    return [
        doc.id
        for doc in processed_docs
        if any(x in doc.tokens for x in query_tokens)
    ]


@dataclass
class _ProcessingDoc:
    """
      Типизированная структура представления документа.

      Attributes:
          id (str): Идентификатор документа
          tokens (list[str]): Обработанные токены текстового представления документа
    """
    id: str
    tokens: list[str]


def _preprocessing(docs: list[Doc]) -> list[_ProcessingDoc]:
    res: list[_ProcessingDoc] = []
    for doc in docs:
        res.append(
            _ProcessingDoc(doc.id, _preprocessing_text(doc.text))
        )
    return res


def _preprocessing_text(text: str) -> list[str]:
    res = []
    for word in text.split(" "):
        if word == "":
            continue
        term = re.findall(r'\w+', word)
        res.append(''.join(term).lower())
    return res
