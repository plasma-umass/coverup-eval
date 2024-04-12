# file src/blib2to3/pgen2/tokenize.py:184-189
# lines [185, 186, 187, 188]
# branches []

import pytest
from blib2to3.pgen2 import tokenize
from blib2to3.pgen2.token import tok_name

@pytest.fixture
def mock_print(mocker):
    return mocker.patch('builtins.print')

def test_printtoken(mock_print):
    type = 1  # Assuming 1 is a valid token type for this test
    token = 'test_token'
    start = (1, 0)
    end = (1, 10)
    line = 'test_token_line'
    
    tokenize.printtoken(type, token, start, end, line)
    
    mock_print.assert_called_once_with(
        "%d,%d-%d,%d:\t%s\t%s" % (start[0], start[1], end[0], end[1], tok_name[type], repr(token))
    )
