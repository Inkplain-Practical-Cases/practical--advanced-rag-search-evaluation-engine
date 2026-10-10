from app.retrieval import retrieve
def test_retrieval_preserves_source():
 r=retrieve(["rag","answers","cite"])
 assert r and all("source" in x and "id" in x for x in r)
def test_no_false_match():
 assert retrieve(["unrelatedgibberish"])==[]
