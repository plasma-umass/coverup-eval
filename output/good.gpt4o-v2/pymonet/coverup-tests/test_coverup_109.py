# file: pymonet/either.py:17-20
# asked: {"lines": [17, 18, 19, 20], "branches": []}
# gained: {"lines": [17, 18, 19, 20], "branches": []}

import pytest
from pymonet.either import Either

class TestEither:
    def test_eq_same_type_and_value(self):
        either1 = Either(10)
        either1.is_right = lambda: True

        either2 = Either(10)
        either2.is_right = lambda: True

        assert either1 == either2

    def test_eq_different_type(self):
        either1 = Either(10)
        either1.is_right = lambda: True

        assert either1 != 10

    def test_eq_different_value(self):
        either1 = Either(10)
        either1.is_right = lambda: True

        either2 = Either(20)
        either2.is_right = lambda: True

        assert either1 != either2

    def test_eq_different_is_right(self):
        either1 = Either(10)
        either1.is_right = lambda: True

        either2 = Either(10)
        either2.is_right = lambda: False

        assert either1 != either2
