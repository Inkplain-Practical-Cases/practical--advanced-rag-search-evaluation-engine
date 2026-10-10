"""Citation-grounded extractive response and simple inspectable evaluation metrics."""
from app.corpus import BENCHMARK,CORPUS
from app.query import prepare_query
from app.retrieval import retrieve
from app.rerank import rerank
def answer(question:str)->dict:
 prepared=prepare_query(question)
 ranked=rerank(question,retrieve(prepared["tokens"]))
 if not ranked:return {"answer":"Insufficient evidence","citations":[],"grounded":False}
 top=ranked[0]
 return {"answer":top["text"],"citations":[{"id":top["id"],"source":top["source"]}],"grounded":True}
def evaluate(question:str,relevant_ids:list[str])->dict:
 output=answer(question)
 predicted={x["id"] for x in output["citations"]}
 return {"precision_at_1":float(bool(predicted & set(relevant_ids))),"citation_count":len(predicted),"grounded":output["grounded"]}
