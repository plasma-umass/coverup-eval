# file src/blib2to3/pgen2/tokenize.py:243-257
# lines [243, 244, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255, 256, 257]
# branches ['244->245', '244->257', '245->246', '245->248', '254->244', '254->255']

import pytest
from blib2to3.pgen2.tokenize import Untokenizer, TokenInfo
from typing import Iterable, Tuple, Text
from blib2to3.pgen2 import token

@pytest.fixture
def mock_untokenizer(mocker):
    mocker.patch.object(Untokenizer, 'compat')
    mocker.patch.object(Untokenizer, 'add_whitespace')
    untokenizer = Untokenizer()
    untokenizer.tokens = []
    untokenizer.prev_row = 0
    untokenizer.prev_col = 0
    return untokenizer

def test_untokenizer_with_len_two_token(mock_untokenizer):
    iterable = [(token.NAME, 'example')]
    result = mock_untokenizer.untokenize(iterable)
    mock_untokenizer.compat.assert_called_once_with((token.NAME, 'example'), iterable)
    assert result == "", "The result should be an empty string since compat handles the token."

def test_untokenizer_with_full_token_info(mock_untokenizer):
    tok_type = token.NAME
    token_str = 'example'
    start = (1, 0)
    end = (1, 7)
    line = 'example\n'
    iterable = [(tok_type, token_str, start, end, line)]
    result = mock_untokenizer.untokenize(iterable)
    mock_untokenizer.add_whitespace.assert_called_once_with(start)
    assert mock_untokenizer.tokens == [token_str], "The token string should be added to the tokens list."
    assert mock_untokenizer.prev_row == end[0], "The prev_row should be updated to the end row of the token."
    assert mock_untokenizer.prev_col == end[1], "The prev_col should be updated to the end column of the token."
    assert result == token_str, "The result should be the token string."

def test_untokenizer_with_newline_token(mock_untokenizer):
    tok_type = token.NEWLINE
    token_str = '\n'
    start = (1, 0)
    end = (1, 1)
    line = '\n'
    iterable = [(tok_type, token_str, start, end, line)]
    result = mock_untokenizer.untokenize(iterable)
    mock_untokenizer.add_whitespace.assert_called_once_with(start)
    assert mock_untokenizer.tokens == [token_str], "The newline token should be added to the tokens list."
    assert mock_untokenizer.prev_row == end[0] + 1, "The prev_row should be incremented after a newline token."
    assert mock_untokenizer.prev_col == 0, "The prev_col should be reset to 0 after a newline token."
    assert result == token_str, "The result should be the newline token."
