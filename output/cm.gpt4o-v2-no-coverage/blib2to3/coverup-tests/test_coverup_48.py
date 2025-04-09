# file: src/blib2to3/pgen2/pgen.py:428-430
# asked: {"lines": [428, 429, 430], "branches": []}
# gained: {"lines": [428, 429, 430], "branches": []}

import pytest
from pathlib import Path
from blib2to3.pgen2.pgen import generate_grammar, ParserGenerator, PgenGrammar

def test_generate_grammar(monkeypatch):
    # Mock the ParserGenerator to avoid actual file I/O
    class MockParserGenerator(ParserGenerator):
        def __init__(self, filename: Path, stream=None):
            self.filename = filename
            self.stream = stream
            self.first = {}
            self.dfas = {}
            self.startsymbol = ""
            self.addfirstsets_called = False

        def addfirstsets(self):
            self.addfirstsets_called = True

        def make_grammar(self):
            return PgenGrammar()

    monkeypatch.setattr("blib2to3.pgen2.pgen.ParserGenerator", MockParserGenerator)

    # Test with default filename
    grammar = generate_grammar()
    assert isinstance(grammar, PgenGrammar)

    # Test with custom filename
    custom_filename = Path("CustomGrammar.txt")
    grammar = generate_grammar(custom_filename)
    assert isinstance(grammar, PgenGrammar)
