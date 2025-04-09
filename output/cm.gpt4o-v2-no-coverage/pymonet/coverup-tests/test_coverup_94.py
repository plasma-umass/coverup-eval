# file: pymonet/either.py:17-20
# asked: {"lines": [17, 18, 19, 20], "branches": []}
# gained: {"lines": [17, 18, 19, 20], "branches": []}

import pytest
from pymonet.either import Either

class TestEither:
    def test_eq_same_instance(self):
        e1 = Either(10)
        e1.is_right = lambda: True
        assert e1 == e1

    def test_eq_different_instance_same_values(self):
        e1 = Either(10)
        e1.is_right = lambda: True

        e2 = Either(10)
        e2.is_right = lambda: True

        assert e1 == e2

    def test_eq_different_instance_different_values(self):
        e1 = Either(10)
        e1.is_right = lambda: True

        e2 = Either(20)
        e2.is_right = lambda: True

        assert e1 != e2

    def test_eq_different_instance_different_is_right(self):
        e1 = Either(10)
        e1.is_right = lambda: True

        e2 = Either(10)
        e2.is_right = lambda: False

        assert e1 != e2

    def test_eq_different_type(self):
        e1 = Either(10)
        e1.is_right = lambda: True

        assert e1 != 10
