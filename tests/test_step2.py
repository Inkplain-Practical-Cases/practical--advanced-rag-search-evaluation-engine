from app.query import prepare_query,normalize_query
import pytest
def test_conservative_normalization():
 assert "cite" in normalize_query("Need citations!")
def test_empty_rejected():
 with pytest.raises(ValueError):prepare_query("  ")
