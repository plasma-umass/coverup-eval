# file: thonny/roughparse.py:805-854
# asked: {"lines": [812, 815, 821, 822, 828, 829, 830, 831, 832, 833, 834, 840, 841, 842, 846, 847, 851, 852, 854], "branches": [[821, 822], [821, 828], [828, 829], [828, 842], [829, 830], [829, 831], [831, 832], [831, 833], [833, 834], [833, 840], [840, 841], [840, 851], [842, 846], [842, 851], [846, 847], [846, 851], [851, 852], [851, 854]]}
# gained: {"lines": [812, 815, 821, 822, 828, 829, 830, 831, 832, 833, 834, 840, 842, 846, 847, 851, 852, 854], "branches": [[821, 822], [821, 828], [828, 829], [828, 842], [829, 830], [829, 831], [831, 832], [831, 833], [833, 834], [833, 840], [840, 851], [842, 846], [846, 847], [846, 851], [851, 852], [851, 854]]}

import pytest
from thonny.roughparse import HyperParser

# Mocking necessary components
_IS_ASCII_ID_CHAR = [False] * 128
for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_":
    _IS_ASCII_ID_CHAR[ord(c)] = True

_IS_ASCII_ID_FIRST_CHAR = [False] * 128
for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_":
    _IS_ASCII_ID_FIRST_CHAR[ord(c)] = True

def iskeyword(s):
    return s in {"False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"}

class TestHyperParser:
    @pytest.fixture(autouse=True)
    def setup(self, monkeypatch):
        monkeypatch.setattr("thonny.roughparse._IS_ASCII_ID_CHAR", _IS_ASCII_ID_CHAR)
        monkeypatch.setattr("thonny.roughparse._IS_ASCII_ID_FIRST_CHAR", _IS_ASCII_ID_FIRST_CHAR)
        monkeypatch.setattr("thonny.roughparse.iskeyword", iskeyword)
        monkeypatch.setattr(HyperParser, "_ID_KEYWORDS", {"True", "False", "None"})

    def test_eat_identifier_ascii(self):
        s = "test_identifier"
        pos = len(s)
        limit = 0
        result = HyperParser._eat_identifier(s, limit, pos)
        assert result == len(s)

    def test_eat_identifier_non_ascii(self):
        s = "test_идентификатор"
        pos = len(s)
        limit = 0
        result = HyperParser._eat_identifier(s, limit, pos)
        assert result == len("test_идентификатор")

    def test_eat_identifier_keyword(self):
        s = "class"
        pos = len(s)
        limit = 0
        result = HyperParser._eat_identifier(s, limit, pos)
        assert result == 0

    def test_eat_identifier_non_keyword(self):
        s = "klass"
        pos = len(s)
        limit = 0
        result = HyperParser._eat_identifier(s, limit, pos)
        assert result == len(s)

    def test_eat_identifier_invalid_first_char(self):
        s = "1invalid"
        pos = len(s)
        limit = 0
        result = HyperParser._eat_identifier(s, limit, pos)
        assert result == 0

    def test_eat_identifier_partial_non_ascii(self):
        s = "test_идентификатор"
        pos = len(s)
        limit = 5
        result = HyperParser._eat_identifier(s, limit, pos)
        assert result == len("идентификатор")
