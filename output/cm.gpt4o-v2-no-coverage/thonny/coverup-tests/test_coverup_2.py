# file: thonny/jedi_utils.py:46-49
# asked: {"lines": [46, 47, 49], "branches": []}
# gained: {"lines": [46, 47, 49], "branches": []}

import pytest
import parso
from thonny.jedi_utils import parse_source

def test_parse_source(monkeypatch):
    source_code = "def foo():\n    return 42"
    
    # Mock parso.parse to ensure it is called correctly
    def mock_parse(code, **kwargs):
        assert code == source_code
        return "parsed_code"
    
    monkeypatch.setattr(parso, "parse", mock_parse)
    
    result = parse_source(source_code)
    
    assert result == "parsed_code"
