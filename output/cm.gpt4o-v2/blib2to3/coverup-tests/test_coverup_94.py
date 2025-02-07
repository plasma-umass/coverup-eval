# file: src/blib2to3/pgen2/pgen.py:241-255
# asked: {"lines": [248], "branches": [[247, 248]]}
# gained: {"lines": [248], "branches": [[247, 248]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator, NFAState
from pathlib import Path
from io import StringIO

@pytest.fixture
def setup_nfa_states():
    start = NFAState()
    middle = NFAState()
    finish = NFAState()
    
    start.addarc(middle, 'a')
    middle.addarc(finish, 'b')
    middle.addarc(start, 'c')  # This creates a loop to ensure the 'if next in todo' branch is taken
    
    return start, finish

@pytest.fixture
def mock_parser_generator(monkeypatch):
    def mock_init(self, filename, stream=None):
        self.filename = filename
        self.stream = StringIO("")
        self.generator = iter([])
        self.dfas = {}
        self.startsymbol = None
        self.first = {}
    
    monkeypatch.setattr(ParserGenerator, "__init__", mock_init)
    return ParserGenerator("dummy_path")

def test_dump_nfa(capsys, setup_nfa_states, mock_parser_generator):
    start, finish = setup_nfa_states
    pg = mock_parser_generator
    
    # Run the method
    pg.dump_nfa("test_nfa", start, finish)
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Check the output
    assert "Dump of NFA for test_nfa" in captured.out
    assert "  State 0 " in captured.out
    assert "  State 1 " in captured.out
    assert "  State 2 (final)" in captured.out
    assert "    a -> 1" in captured.out
    assert "    b -> 2" in captured.out
    assert "    c -> 0" in captured.out
