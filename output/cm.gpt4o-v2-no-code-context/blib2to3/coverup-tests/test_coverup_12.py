# file: src/blib2to3/pgen2/parse.py:205-217
# asked: {"lines": [205, 209, 210, 211, 212, 213, 214, 215, 216, 217], "branches": [[214, 215], [214, 217]]}
# gained: {"lines": [205, 209, 210, 211, 212, 213, 214, 215, 216, 217], "branches": [[214, 215], [214, 217]]}

import pytest
from blib2to3.pgen2.parse import Parser

class MockGrammar:
    pass

class MockContext:
    pass

@pytest.fixture
def parser():
    p = Parser(MockGrammar())
    p.stack = [(None, None, [[]])]
    return p

def test_shift_with_newnode(parser, mocker):
    mock_convert = mocker.patch.object(parser, 'convert', return_value='newnode')
    parser.shift(1, 'value', 2, MockContext())
    assert parser.stack[-1] == (None, 2, [['newnode']])
    mock_convert.assert_called_once()

def test_shift_without_newnode(parser, mocker):
    mock_convert = mocker.patch.object(parser, 'convert', return_value=None)
    parser.shift(1, 'value', 2, MockContext())
    assert parser.stack[-1] == (None, 2, [[]])
    mock_convert.assert_called_once()
