# file: src/blib2to3/pgen2/tokenize.py:243-257
# asked: {"lines": [243, 244, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255, 256, 257], "branches": [[244, 245], [244, 257], [245, 246], [245, 248], [254, 244], [254, 255]]}
# gained: {"lines": [243, 244, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255, 256, 257], "branches": [[244, 245], [244, 257], [245, 246], [245, 248], [254, 244], [254, 255]]}

import pytest
from blib2to3.pgen2.tokenize import Untokenizer, TokenInfo

def test_untokenize_with_two_element_tuple(monkeypatch):
    def mock_compat(self, token, iterable):
        self.tokens.append("mocked")

    monkeypatch.setattr(Untokenizer, "compat", mock_compat)
    
    ut = Untokenizer()
    ut.tokens = []
    ut.prev_row = 0
    ut.prev_col = 0

    iterable = [(1, "token")]
    result = ut.untokenize(iterable)
    
    assert result == "mocked"
    assert ut.tokens == ["mocked"]

def test_untokenize_with_full_token_info(monkeypatch):
    ut = Untokenizer()
    ut.tokens = []
    ut.prev_row = 0
    ut.prev_col = 0

    iterable = [(1, "token", (0, 0), (0, 5), "line")]
    result = ut.untokenize(iterable)
    
    assert result == "token"
    assert ut.tokens == ["token"]
    assert ut.prev_row == 0
    assert ut.prev_col == 5

def test_untokenize_with_newline_token(monkeypatch):
    ut = Untokenizer()
    ut.tokens = []
    ut.prev_row = 0
    ut.prev_col = 0

    NEWLINE = 4
    iterable = [(NEWLINE, "token", (0, 0), (0, 5), "line")]
    result = ut.untokenize(iterable)
    
    assert result == "token"
    assert ut.tokens == ["token"]
    assert ut.prev_row == 1
    assert ut.prev_col == 0
