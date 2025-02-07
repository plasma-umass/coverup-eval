# file: thonny/jedi_utils.py:46-49
# asked: {"lines": [46, 47, 49], "branches": []}
# gained: {"lines": [46, 47, 49], "branches": []}

import pytest
import importlib

def test_parse_source(monkeypatch):
    parso_mock = pytest.importorskip("parso")

    class MockParso:
        @staticmethod
        def parse(source):
            return f"Parsed: {source}"
    
    monkeypatch.setattr(parso_mock, "parse", MockParso.parse)
    
    from thonny.jedi_utils import parse_source
    source_code = "print('Hello, world!')"
    result = parse_source(source_code)
    
    assert result == f"Parsed: {source_code}"
