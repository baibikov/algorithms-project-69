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
    # создаем обратный индекс для документов
    reverse_index = _make_reverse_index(processed_docs)
    # фильтруем значения по индексу
    filtered_processed_docs = _filter_reverse_index_processing_docs(reverse_index, query_tokens)
    # производим расчет релевантности по алгоритму: TF (Term Frequency)
    ranked_docs = _calculate_rank_by_tf(filtered_processed_docs, query_tokens)
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


@dataclass
class _ReverseIndex:
    """
    Attributes:
         index (dict[str, _ProcessingDoc): Представляет собой обратный индекс,
            где ключом является слово, а значением ссылки на преобразованные документы.
            _ProcessingDoc необходим для дальнейшей работы с документами.
    """
    index: dict[str, list[_ProcessingDoc]]


def _make_reverse_index(docs: list[_ProcessingDoc]) -> _ReverseIndex:
    index: dict[str, list[_ProcessingDoc]] = {}
    for doc in docs:
        for word in doc.tokens:
            index.setdefault(word, []).append(doc)
    return _ReverseIndex(index)


def _filter_reverse_index_processing_docs(reverse_index: _ReverseIndex,
                                          filter_keys: list[str]) -> list[_ProcessingDoc]:
    unique_docs: dict[str, _ProcessingDoc] = {}
    for word in filter_keys:
        for doc in reverse_index.index.get(word, []):
            unique_docs.setdefault(doc.id, doc)
    return list(unique_docs.values())


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
