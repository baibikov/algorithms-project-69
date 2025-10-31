import re

from .types import Document, TokenizedDocument


def _tokenize_documents(docs: list[Document]) -> list[TokenizedDocument]:
    return [_tokenize_document(doc) for doc in docs]


def _tokenize_document(doc: Document) -> TokenizedDocument:
    return TokenizedDocument(doc.id, _tokenize_text(doc.text))


def _tokenize_text(text: str) -> list[str]:
    return [w.lower() for w in re.findall(r'\w+', text)]
