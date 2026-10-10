from app.rerank import rerank,diagnose
def test_reranking_retains_citation():
 results=rerank("citation", [{"id":"p2","source":"guide/rag","text":"citation evidence","retrieval_score":1}])
 assert results[0]["id"]=="p2" and diagnose(results)["candidates"]==1
