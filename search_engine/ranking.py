import math

from .types import TokenizedDocument, RankedDocument


def _tf(term: str, document_tokens: list[str]) -> float:
    return sum(1 for token in document_tokens if token == term) / len(document_tokens)


def _idf(term: str, documents: list[TokenizedDocument]) -> float:
    term_freq = sum(1 for doc in documents if term in doc.tokens)
    return math.log(len(documents) / (term_freq + 1))


def _tf_idf(term: str, document_tokens: list[str], documents: list[TokenizedDocument]) -> float:
    return _tf(term, document_tokens) * _idf(term, documents)


def _cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    """
    Compute cosine similarity between two vectors.

    Parameters
    ----------
    vec1 : list[float] - first vector
    vec2 : list[float] - second vector

    Returns
    -------
    float - cosine similarity in range [0, 1]
    """
    dot_product = sum(a * b for a, b in zip(vec1, vec2))

    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot_product / (norm1 * norm2)


def _sorted_rank_tokenize_documents(query_tokens: list[str],
                                    documents: list[TokenizedDocument]) -> list[RankedDocument]:
    query_vector = [_idf(t, documents) for t in query_tokens]

    doc_vectors = {
        doc.id: [_tf_idf(t, doc.tokens, documents) for t in query_tokens]
        for doc in documents
    }

    return sorted(
        [
            RankedDocument(doc_id, _cosine_similarity(query_vector, vec))
            for doc_id, vec in doc_vectors.items()
        ],
        key=lambda x: x.score,
        reverse=True
    )
