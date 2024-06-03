# file src/blib2to3/pgen2/tokenize.py:243-257
# lines [243, 244, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255, 256, 257]
# branches ['244->245', '244->257', '245->246', '245->248', '254->244', '254->255']

import pytest
from blib2to3.pgen2.tokenize import Untokenizer, TokenInfo, NEWLINE, NL
from typing import Tuple, Text

@pytest.fixture
def untokenizer():
    return Untokenizer()

def test_untokenize_with_two_element_tuple(untokenizer):
    # Mock the compat method to ensure it gets called
    untokenizer.compat = lambda x, y: None
    untokenizer.tokens = []
    untokenizer.prev_row = 0
    untokenizer.prev_col = 0

    # Create a two-element tuple token
    token = (1, 'token')
    iterable = [token]

    result = untokenizer.untokenize(iterable)

    assert result == ""
    assert untokenizer.tokens == []

def test_untokenize_with_full_token(untokenizer):
    untokenizer.add_whitespace = lambda x: None
    untokenizer.tokens = []
    untokenizer.prev_row = 0
    untokenizer.prev_col = 0

    # Create a full token
    token = (1, 'token', (0, 0), (0, 5), 'line')
    iterable = [token]

    result = untokenizer.untokenize(iterable)

    assert result == "token"
    assert untokenizer.tokens == ['token']
    assert untokenizer.prev_row == 0
    assert untokenizer.prev_col == 5

def test_untokenize_with_newline_token(untokenizer):
    untokenizer.add_whitespace = lambda x: None
    untokenizer.tokens = []
    untokenizer.prev_row = 0
    untokenizer.prev_col = 0

    # Create a NEWLINE token
    token = (NEWLINE, 'token', (0, 0), (0, 5), 'line')
    iterable = [token]

    result = untokenizer.untokenize(iterable)

    assert result == "token"
    assert untokenizer.tokens == ['token']
    assert untokenizer.prev_row == 1
    assert untokenizer.prev_col == 0

def test_untokenize_with_nl_token(untokenizer):
    untokenizer.add_whitespace = lambda x: None
    untokenizer.tokens = []
    untokenizer.prev_row = 0
    untokenizer.prev_col = 0

    # Create a NL token
    token = (NL, 'token', (0, 0), (0, 5), 'line')
    iterable = [token]

    result = untokenizer.untokenize(iterable)

    assert result == "token"
    assert untokenizer.tokens == ['token']
    assert untokenizer.prev_row == 1
    assert untokenizer.prev_col == 0
