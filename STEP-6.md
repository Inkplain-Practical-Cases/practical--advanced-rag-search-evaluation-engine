# STEP-6 — Run end to end RAG regression suite

This cumulative branch includes real Python source and deterministic regression tests. Run `python -m pip install -r requirements.txt` followed by `python -m pytest -q`. It illustrates a local lexical retrieval and reranking system, not a hosted LLM or semantic vector database.

## Database (Entity) Relations
SQLite persists RAG HTTP request/outcome audit; corpus stays a static fixture. See STEP-6.erd and STEP-6-ERD.
