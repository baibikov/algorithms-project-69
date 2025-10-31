from .find import _find_tokenized_documents
from .indexing import _build_tokenized_inverted_index
from .ranking import _sorted_rank_tokenize_documents
from .tokenize import _tokenize_documents, _tokenize_text
from .types import Document


def search(docs: list[Document], query: str) -> list[str]:
    """
    Search for documents that match the given query and return their IDs sorted by relevance.

    This function performs the full search pipeline:
    1. Tokenizes and normalizes the input documents.
    2. Builds a tokenized inverted index for efficient lookup.
    3. Tokenizes and normalizes the query.
    4. Finds candidate documents containing query tokens.
    5. Ranks the candidate documents using TF-IDF and cosine similarity.
    6. Returns document IDs sorted by descending relevance score.

    Parameters
    ----------
    docs : list[Document]
        List of documents to search in. Each Document must have 'id' and 'text' attributes.
    query : str
        The search query string provided by the user.

    Returns
    -------
    list[str]
        A list of document IDs sorted from most to least relevant to the query.
        Returns an empty list if no documents or query tokens are found.

    Examples
    --------
    >>> documents = [
    ...     Document(id="doc1", text="Python is a programming language"),
    ...     Document(id="doc2", text="Search engines use ranking algorithms"),
    ...     Document(id="doc3", text="Python can be used for search engines")
    ... ]
    >>> search(documents, "python search")
    ['doc3', 'doc1', 'doc2']

    >>> search(documents, "ranking algorithms")
    ['doc2']

    >>> search(documents, "nonexistent term")
    []

    >>> search([], "python")
    []

    >>> search(documents, "")
    []
    """
    if not docs or not query:
        return []

    tokenized_documents = _tokenize_documents(docs)
    if not tokenized_documents:
        return []

    tokenized_inverted_index = _build_tokenized_inverted_index(tokenized_documents)

    tokenized_query = _tokenize_text(query)
    if not tokenized_query:
        return []

    found_tokenized_documents = _find_tokenized_documents(tokenized_inverted_index, tokenized_query)
    if not found_tokenized_documents:
        return []

    sorted_rank_documents = _sorted_rank_tokenize_documents(tokenized_query,
                                                            found_tokenized_documents)

    return [doc.id for doc in sorted_rank_documents]
