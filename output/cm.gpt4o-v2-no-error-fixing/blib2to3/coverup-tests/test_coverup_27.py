# file: src/blib2to3/pgen2/pgen.py:428-430
# asked: {"lines": [428, 429, 430], "branches": []}
# gained: {"lines": [428, 429, 430], "branches": []}

import pytest
from blib2to3.pgen2.pgen import generate_grammar, ParserGenerator
from pathlib import Path

def test_generate_grammar(monkeypatch):
    # Mock the ParserGenerator class
    class MockParserGenerator:
        def __init__(self, filename):
            self.filename = filename

        def make_grammar(self):
            return "mock_grammar"

    # Apply the monkeypatch for ParserGenerator
    monkeypatch.setattr("blib2to3.pgen2.pgen.ParserGenerator", MockParserGenerator)

    # Call the function and check the result
    result = generate_grammar("mock_filename")
    assert result == "mock_grammar"
