from .types import InvertedIndex, TokenizedDocument


def _find_tokenized_documents(
        inverted_index: InvertedIndex,
        query_tokens: list[str]) -> list[TokenizedDocument]:
    """
    Find tokenized documents that contain any of the query tokens.
    """
    doc_set: set[str] = set()
    return [
        doc
        for token in query_tokens
        for doc in inverted_index.index.get(token, {})
        if doc.id not in doc_set
    ]
