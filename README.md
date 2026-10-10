# Advanced RAG Search & Evaluation Engine

Junior FDE cumulative six-step learning implementation: synthetic corpus and benchmark, query normalization, provenance-preserving lexical retrieval, transparent reranking, grounded extractive answer and precision@1 evaluation, and FastAPI routes.

This code is **not a production semantic RAG or LLM-powered application**. It uses deterministic lexical retrieval instead of hosted vector databases or large-language-model generation; the engineering concepts and evaluation contracts can be extended without network keys.

## Study
- STEP-1: [Create corpus and benchmark fixtures](https://github.com/Inkplain-Practical-Cases/practical--advanced-rag-search-evaluation-engine/tree/step-01-create-corpus-and-benchmark-fixtures)
- STEP-2: [Normalize and expand queries](https://github.com/Inkplain-Practical-Cases/practical--advanced-rag-search-evaluation-engine/tree/step-02-normalize-and-expand-queries)
- STEP-3: [Retrieve cited document candidates](https://github.com/Inkplain-Practical-Cases/practical--advanced-rag-search-evaluation-engine/tree/step-03-retrieve-cited-document-candidates)
- STEP-4: [Rerank and diagnose ranked results](https://github.com/Inkplain-Practical-Cases/practical--advanced-rag-search-evaluation-engine/tree/step-04-rerank-and-diagnose-ranked-results)
- STEP-5: [Evaluate grounded generated responses](https://github.com/Inkplain-Practical-Cases/practical--advanced-rag-search-evaluation-engine/tree/step-05-evaluate-grounded-generated-responses)
- STEP-6: [Run end to end RAG regression suite](https://github.com/Inkplain-Practical-Cases/practical--advanced-rag-search-evaluation-engine/tree/step-06-run-end-to-end-rag-regression-suite)

Install with `python -m pip install -r requirements.txt`, run `python -m pytest -q`, then `uvicorn app.main:app --reload`. Each branch has STEP-N.crd and STEP-N.md; main has FINAL.crd and INKP simulator added separately.
