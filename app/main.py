"""Final FastAPI evaluation service. Local source-backed evaluation only."""
from fastapi import FastAPI
from pydantic import BaseModel,Field
from app.evaluation import answer,evaluate
from app.corpus import BENCHMARK
app=FastAPI(title="Advanced RAG Search & Evaluation")
class Query(BaseModel):
 query:str=Field(min_length=1,max_length=1500)
@app.post("/rag/answer")
def rag_answer(request:Query):
 return answer(request.query)
@app.get("/rag/benchmark")
def benchmark():
 return {"results":[{"query":x["query"],**evaluate(x["query"],x["relevant"])} for x in BENCHMARK]}
