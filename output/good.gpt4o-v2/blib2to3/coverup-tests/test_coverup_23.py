# file: src/blib2to3/pgen2/pgen.py:241-255
# asked: {"lines": [241, 242, 243, 244, 245, 246, 247, 248, 250, 251, 252, 253, 255], "branches": [[244, 0], [244, 245], [246, 244], [246, 247], [247, 248], [247, 250], [252, 253], [252, 255]]}
# gained: {"lines": [241, 242, 243, 244, 245, 246, 247, 250, 251, 252, 253, 255], "branches": [[244, 0], [244, 245], [246, 244], [246, 247], [247, 250], [252, 253], [252, 255]]}

import pytest
from blib2to3.pgen2.pgen import ParserGenerator, NFAState
from io import StringIO

@pytest.fixture
def setup_nfa_states():
    start = NFAState()
    mid = NFAState()
    finish = NFAState()
    start.addarc(mid, 'a')
    mid.addarc(finish, None)
    return start, mid, finish

@pytest.fixture
def parser_generator(mocker):
    mocker.patch('blib2to3.pgen2.pgen.ParserGenerator.parse', return_value=({}, 'start'))
    dummy_file = StringIO("dummy content")
    return ParserGenerator("dummy_filename", dummy_file)

def test_dump_nfa(capsys, setup_nfa_states, parser_generator):
    start, mid, finish = setup_nfa_states
    pg = parser_generator
    pg.dump_nfa("test_nfa", start, finish)
    
    captured = capsys.readouterr()
    assert "Dump of NFA for test_nfa" in captured.out
    assert "  State 0 " in captured.out
    assert "  State 1 " in captured.out
    assert "  State 2 (final)" in captured.out
    assert "    a -> 1" in captured.out
    assert "    -> 2" in captured.out
