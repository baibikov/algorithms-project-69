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

    # подготавливаем документы
    # определяем токены документов
    processed_docs = _preprocessing(docs)
    # подготавливаем запрос
    # определяем токен запроса
    query_tokens = _preprocessing_text(query)
    # ищем релевантные документы
    processed_searched_docs = _preprocessing_search(processed_docs, query_tokens)
    # производим расчет релевантности по алгоритму: TF (Term Frequency)
    ranked_docs = _calculate_rank_by_tf(processed_searched_docs, query_tokens)
    # сортируем рассчитанные документы
    sorted_ranked_docs = _sort_ranked_docs(ranked_docs)

    return [
        doc.id
        for doc in sorted_ranked_docs
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


def _preprocessing_search(
        docs: list[_ProcessingDoc], query_tokens: list[str]) -> list[_ProcessingDoc]:
    return [
        doc
        for doc in docs
        if any(x in doc.tokens for x in query_tokens)
    ]


@dataclass
class _RankedDoc:
    """
     Структура для представления документа с рассчитанным рангом релевантности.

     Используется для хранения результатов этапа ранжирования перед финальной сортировкой.

     Attributes:
         id (str): Уникальный идентификатор документа
         tokens (list[str]): Обработанные токены текстового содержания документа
         rank (float): Расчет релевантности (например, TF, TF-IDF, BM25 score)
     """
    id: str
    tokens: list[str]
    rank: float


def _calculate_rank_by_tf(docs: list[_ProcessingDoc], query_tokens: list[str]) -> list[_RankedDoc]:
    return [
        _RankedDoc(doc.id, doc.tokens, len(list(filter(lambda x: x in query_tokens, doc.tokens))))
        for doc in docs
    ]


def _sort_ranked_docs(docs: list[_RankedDoc]) -> list[_RankedDoc]:
    return sorted(docs, key=lambda doc: doc.rank, reverse=True)
