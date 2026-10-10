from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_benchmark_route():
 assert client.get("/rag/benchmark").status_code==200
def test_answer_route():
 r=client.post("/rag/answer",json={"query":"How to cite RAG evidence?"})
 assert r.status_code==200 and "citations" in r.json()
def test_invalid_query():
 assert client.post("/rag/answer",json={"query":""}).status_code==422
