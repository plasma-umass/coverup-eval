# file: src/blib2to3/pgen2/pgen.py:366-372
# asked: {"lines": [370, 371], "branches": []}
# gained: {"lines": [370, 371], "branches": []}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator

def test_raise_error_with_args(monkeypatch):
    def mock_init(self, filename, stream=None):
        self.filename = "testfile"
        self.end = (1, 2)
        self.line = "test line"

    monkeypatch.setattr(ParserGenerator, "__init__", mock_init)
    pg = ParserGenerator("dummy")

    with pytest.raises(SyntaxError) as excinfo:
        pg.raise_error("Error: %s", "details")
    assert "Error: details" in str(excinfo.value)

def test_raise_error_formatting_fails(monkeypatch):
    def mock_init(self, filename, stream=None):
        self.filename = "testfile"
        self.end = (1, 2)
        self.line = "test line"

    monkeypatch.setattr(ParserGenerator, "__init__", mock_init)
    pg = ParserGenerator("dummy")

    with pytest.raises(SyntaxError) as excinfo:
        pg.raise_error("Error: %d", "not a number")
    assert "Error: %d not a number" in str(excinfo.value)
