"""Deterministic lexical candidate retrieval with preserved passage provenance."""
import re
from app.corpus import CORPUS
def retrieve(query_tokens:list[str],k:int=4):
 if k<1:raise ValueError("k must be positive")
 scored=[]
 for passage in CORPUS:
  terms=set(re.findall(r"[a-z0-9]+",passage.text.lower()))
  score=len(terms.intersection(set(query_tokens)))
  if score:scored.append({"id":passage.id,"source":passage.source,"text":passage.text,"retrieval_score":score})
 return sorted(scored,key=lambda r:(-r["retrieval_score"],r["id"]))[:k]
