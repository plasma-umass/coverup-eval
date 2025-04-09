# file: pymonet/monad_try.py:14-17
# asked: {"lines": [14, 15, 16, 17], "branches": []}
# gained: {"lines": [14, 15, 16, 17], "branches": []}

import pytest
from pymonet.monad_try import Try

class TestTry:
    def test_eq_same_instance(self):
        instance1 = Try(10, True)
        instance2 = Try(10, True)
        assert instance1 == instance2

    def test_eq_different_instance(self):
        instance1 = Try(10, True)
        instance2 = Try(20, True)
        assert instance1 != instance2

    def test_eq_different_type(self):
        instance1 = Try(10, True)
        instance2 = "Not a Try instance"
        assert instance1 != instance2

    def test_eq_different_success(self):
        instance1 = Try(10, True)
        instance2 = Try(10, False)
        assert instance1 != instance2
