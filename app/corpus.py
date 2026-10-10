"""Synthetic enterprise knowledge corpus and reproducible benchmark."""
from dataclasses import dataclass
@dataclass(frozen=True)
class Passage:
 id:str
 text:str
 source:str
CORPUS=[Passage("p1","MCP tools expose typed operations with JSON-schema inputs.","guide/mcp"),Passage("p2","RAG answers should cite retrieved passages, not unsupported model claims.","guide/rag"),Passage("p3","Reranking reorders retrieved candidates according to query relevance.","guide/search"),Passage("p4","Response evaluation measures groundedness and answer usefulness.","guide/evaluation")]
BENCHMARK=[{"query":"How should RAG answers cite evidence?","relevant":["p2"]},{"query":"What is reranking?","relevant":["p3"]}]
