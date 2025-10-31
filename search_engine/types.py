from dataclasses import dataclass


@dataclass(frozen=True)
class Document:
    """
    Represents an immutable text document used by the search engine.

    Each document has a unique identifier and raw text content.
    Documents are the primary data units that are tokenized, normalized,
    and indexed during the indexing stage.

    Attributes
    ----------
    id : str
        Unique document identifier (e.g., UUID or filename).
    text : str
        Raw textual content of the document.
    """
    id: str
    text: str

    def __post_init__(self):
        """
        Validate the fields of the Document after initialization.

        This method is automatically called by the dataclass mechanism
        immediately after the object is created. It ensures that both
        the document ID and text fields are non-empty and contain
        meaningful (non-whitespace) content.
        """
        if not self.id or not self.id.strip():
            raise ValueError("Document 'id' cannot be empty.")

        if not self.text or not self.text.strip():
            raise ValueError("Document 'text' cannot be empty.")


@dataclass(frozen=True)
class TokenizedDocument:
    """
      Represents a document after tokenization.

      This dataclass stores a document identifier along with the list of tokens
      produced by a tokenizer. It serves as an intermediate representation
      between the raw `Document` (containing text) and further processing stages
      such as normalization, indexing, or term frequency analysis.

      Attributes
      ----------
      id : str
          Unique identifier of the original document.
      tokens : list[str]
          Sequence of tokens extracted from the document text.
    """
    id: str
    tokens: list[str]


@dataclass(frozen=True)
class InvertedIndex:
    """
    Represents an inverted index mapping tokens to document IDs.

    Attributes
    ----------
    index : dict[str, list[TokenizedDocument]]
        Mapping from token (term) to list of tokenized documents containing it.
    """
    index: dict[str, list[TokenizedDocument]]


@dataclass(frozen=True)
class RankedDocument:
    """
    Represents a document after ranking.

    Attributes
    ----------
    id : str
        ID of the original document.
    score : float
        Relevance score of the document for a given query.
    """
    id: str
    score: float
