# file: src/blib2to3/pgen2/tokenize.py:243-257
# asked: {"lines": [243, 244, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255, 256, 257], "branches": [[244, 245], [244, 257], [245, 246], [245, 248], [254, 244], [254, 255]]}
# gained: {"lines": [243, 244, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255, 256, 257], "branches": [[244, 245], [244, 257], [245, 246], [245, 248], [254, 244], [254, 255]]}

import pytest
from blib2to3.pgen2.tokenize import TokenInfo, Untokenizer
from blib2to3.pgen2.token import NEWLINE, NL
from typing import Tuple, Text

@pytest.fixture
def untokenizer():
    return Untokenizer()

def test_untokenize_with_two_element_tuple(monkeypatch, untokenizer):
    def mock_compat(token: Tuple[int, Text], iterable):
        assert token == (1, 'token')
        assert list(iterable) == [(1, 'token')]

    monkeypatch.setattr(untokenizer, 'compat', mock_compat)
    iterable = [(1, 'token')]
    result = untokenizer.untokenize(iterable)
    assert result == ''

def test_untokenize_with_full_token_info(monkeypatch, untokenizer):
    def mock_add_whitespace(start):
        assert start == (1, 0)

    monkeypatch.setattr(untokenizer, 'add_whitespace', mock_add_whitespace)
    iterable = [(1, 'token', (1, 0), (1, 5), 'line')]
    result = untokenizer.untokenize(iterable)
    assert result == 'token'
    assert untokenizer.prev_row == 1
    assert untokenizer.prev_col == 5

def test_untokenize_with_newline_token(monkeypatch, untokenizer):
    def mock_add_whitespace(start):
        assert start == (1, 0)

    monkeypatch.setattr(untokenizer, 'add_whitespace', mock_add_whitespace)
    iterable = [(NEWLINE, 'token', (1, 0), (1, 5), 'line')]
    result = untokenizer.untokenize(iterable)
    assert result == 'token'
    assert untokenizer.prev_row == 2
    assert untokenizer.prev_col == 0

def test_untokenize_with_nl_token(monkeypatch, untokenizer):
    def mock_add_whitespace(start):
        assert start == (1, 0)

    monkeypatch.setattr(untokenizer, 'add_whitespace', mock_add_whitespace)
    iterable = [(NL, 'token', (1, 0), (1, 5), 'line')]
    result = untokenizer.untokenize(iterable)
    assert result == 'token'
    assert untokenizer.prev_row == 2
    assert untokenizer.prev_col == 0
