import math

from .types import RankedDocument, TokenizedDocument


def _tf(term: str, document_tokens: list[str]) -> float:
    term_count = sum(1 for token in document_tokens if token == term)
    return term_count / len(document_tokens)


def _idf(term: str, documents: list[TokenizedDocument]) -> float:
    term_count = sum(1 for doc in documents if term in doc.tokens)
    return math.log2(1 + (len(documents) / (term_count + 0.5)))


def _tf_idf(term: str,
            document_tokens: list[str],
            documents: list[TokenizedDocument]) -> float:
    return _tf(term, document_tokens) * _idf(term, documents)


def _sorted_rank_tokenize_documents(
        query_tokens: list[str],
        documents: list[TokenizedDocument]) -> list[RankedDocument]:
    doc_vectors = {
        doc.id: [_tf_idf(t, doc.tokens, documents) for t in query_tokens]
        for doc in documents
    }

    return sorted(
        [
            RankedDocument(doc_id, sum(vec))
            for doc_id, vec in doc_vectors.items()
        ],
        key=lambda x: x.score,
        reverse=True
    )
