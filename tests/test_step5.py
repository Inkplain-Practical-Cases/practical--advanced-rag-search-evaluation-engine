from app.evaluation import answer,evaluate
def test_grounded_answer_has_real_citation():
 r=answer("RAG answers cite evidence")
 assert r["grounded"] and r["citations"] and r["answer"]
def test_missing_evidence_abstains():
 assert not answer("unknownunlistedtoken")["grounded"]
