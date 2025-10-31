from pathlib import Path

from search_engine import Document, search


def test_search_empty_documents():
    docs = []
    assert search(docs, "foo") == []


def test_search_empty_query():
    docs = [
        Document("id_1", "foo")
    ]
    assert search(docs, "") == []
    assert search(docs, "    ") == []


def test_search_full_empty():
    docs = []
    assert search(docs, "") == []


def test_search_one_document():
    docs = [
        Document("id_1", "foo")
    ]
    assert search(docs, "foo") == ["id_1"]


def test_search_two_documents_with_one_token():
    docs = [
        Document("id_1", "foo"),
        Document("id_2", "foo"),
        Document("id_3", "some bar"),
        Document("id_4", "mix vals"),
        Document("id_5", "check"),
    ]
    assert search(docs, "foo") == ["id_1", "id_2"]
    assert search(docs, "bar") == ["id_3"]
    assert search(docs, "mix") == ["id_4"]


def test_search_normalized():
    docs = [
        Document("id_1", "foo"),
        Document("id_2", "Foo"),
        Document("id_3", "FOO"),
        Document("id_4", "!FOO"),
        Document("id_5", "FOO!"),
        Document("id_6", "!FOO! bar"),
    ]
    assert search(docs, "foo") == ["id_1", "id_2",
                                   "id_3", "id_4", "id_5", "id_6"]


def test_search_sort_by_score():
    docs = [
        Document("id_1", "cat sleeps on the couch"),
        Document("id_2", "cat and dog love each other"),
        Document("id_3", "cat plays with a yarn ball"),
    ]
    assert search(docs, "cat plays") == ["id_3", "id_1", "id_2"]

    docs = [
        Document("id_5", "dog plays with the ball"),
        Document("id_6", "cat and dog love each other"),
        Document("id_7", "cat plays with a yarn ball"),
    ]
    assert search(docs, "dog ball") == ["id_5", "id_6", "id_7"]


def test_search_untyped_docs():
    docs = [
        {"id": "1", "text": "foo"},
    ]
    assert search(docs, "foo") == ["1"]


def test_search_short_strings():
    docs = [
        {"id": 'doc1',
         "text": "I can't shoot straight unless I've had a pint!"},
        {"id": 'doc2', "text": "Don't shoot shoot shoot that thing at me."},
        {"id": 'doc3', "text": "I'm your shooter."},
    ]
    assert search(docs, "shoot at me, nerd") == ["doc2", "doc1"]


def test_simple_search():
    docs = [
        {"id": "garbage_patch_NG", "text": _fixture("garbage_patch_NG")},
        {"id": "garbage_patch_ocean_clean",
         "text": _fixture("garbage_patch_ocean_clean")},
        {"id": "garbage_patch_wiki", "text": _fixture("garbage_patch_wiki")},
    ]
    want = [
        "garbage_patch_NG",
        "garbage_patch_ocean_clean",
        "garbage_patch_wiki"
    ]
    assert search(docs, "trash island") == want


def test_search_with_spam():
    docs = [
        {"id": "garbage_patch_NG", "text": _fixture("garbage_patch_NG")},
        {"id": "garbage_patch_ocean_clean",
         "text": _fixture("garbage_patch_ocean_clean")},
        {"id": "garbage_patch_wiki", "text": _fixture("garbage_patch_wiki")},
        {"id": "garbage_patch_spam", "text": _fixture("garbage_patch_spam")},
    ]
    want = [
        "garbage_patch_NG",
        "garbage_patch_ocean_clean",
        "garbage_patch_wiki",
        "garbage_patch_spam"
    ]
    assert search(docs, "the trash island is a") == want


def _fixture(filename: str) -> str:
    return Path("./tests/fixtures/" + filename).read_text()
