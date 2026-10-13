"""Check SQLite RAG request and event foreign-key integrity."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit
def test_rag_audit(tmp_path):
    db=str(tmp_path/"rag.sqlite3")
    rid=provider_record_request_audit("POST","/rag/answer",200,8.8,db)
    with sqlite3.connect(db) as c:
        assert c.execute("SELECT COUNT(*) FROM rag_api_requests WHERE id=?",(rid,)).fetchone()[0]==1
        assert c.execute("SELECT COUNT(*) FROM rag_api_events WHERE request_id=?",(rid,)).fetchone()[0]==1
        assert c.execute("PRAGMA foreign_key_check").fetchall()==[]
