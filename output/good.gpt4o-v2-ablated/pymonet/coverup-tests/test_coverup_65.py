# file: pymonet/either.py:17-20
# asked: {"lines": [18, 19, 20], "branches": []}
# gained: {"lines": [18, 19, 20], "branches": []}

import pytest
from pymonet.either import Either

class TestEither:
    def test_either_eq_same_type_same_value(self):
        either1 = Either(10)
        either2 = Either(10)
        assert either1 == either2

    def test_either_eq_same_type_different_value(self):
        either1 = Either(10)
        either2 = Either(20)
        assert either1 != either2

    def test_either_eq_different_type(self):
        either1 = Either(10)
        other = 10
        assert either1 != other

    def test_either_eq_same_type_different_is_right(self, monkeypatch):
        either1 = Either(10)
        either2 = Either(10)

        monkeypatch.setattr(either1, 'is_right', lambda: True)
        monkeypatch.setattr(either2, 'is_right', lambda: False)

        assert either1 != either2
