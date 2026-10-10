from app.corpus import CORPUS,BENCHMARK
def test_corpus_has_unique_citations():
 assert len({p.id for p in CORPUS})==len(CORPUS)
def test_benchmark_references_real_passages():
 ids={p.id for p in CORPUS}
 assert all(set(item["relevant"]) <= ids for item in BENCHMARK)
