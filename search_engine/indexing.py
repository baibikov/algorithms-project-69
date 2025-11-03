from collections import defaultdict

from .types import InvertedIndex, TokenizedDocument


def _build_tokenized_inverted_index(
        docs: list[TokenizedDocument]) -> InvertedIndex:
    index: dict[str, list[TokenizedDocument]] = defaultdict(list)
    for doc in docs:
        for word in doc.tokens:
            index.setdefault(word, []).append(doc)
    return InvertedIndex(index)
