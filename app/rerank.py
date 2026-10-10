"""Transparent reranker that keeps citations and exposes diagnostics."""
from app.query import normalize_query
def rerank(query:str,candidates:list[dict])->list[dict]:
 tokens=set(normalize_query(query))
 output=[]
 for item in candidates:
  meaningful=set(normalize_query(item["text"]))
  score=2*len(tokens & meaningful)+float(item["retrieval_score"])
  output.append({**item,"rerank_score":score})
 return sorted(output,key=lambda x:(-x["rerank_score"],x["id"]))
def diagnose(ranked:list[dict])->dict:
 return {"candidates":len(ranked),"top_passage_id":ranked[0]["id"] if ranked else None,"score_spread":(ranked[0]["rerank_score"]-ranked[-1]["rerank_score"]) if ranked else 0}
