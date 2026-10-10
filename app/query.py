"""Conservative query preparation preserving the user's meaning."""
import re
SYNONYMS={"citations":"cite","citation":"cite","ranking":"reranking","evaluate":"evaluation"}
def normalize_query(query:str)->list[str]:
 if not query.strip():raise ValueError("Empty query")
 tokens=re.findall(r"[a-z0-9]+",query.lower())
 return [SYNONYMS.get(t,t) for t in tokens]
def prepare_query(query:str)->dict:
 tokens=normalize_query(query)
 return {"original":query,"tokens":tokens,"expansion_applied":any(x in query.lower() for x in SYNONYMS)}
