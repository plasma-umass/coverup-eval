# file: pymonet/either.py:17-20
# asked: {"lines": [17, 18, 19, 20], "branches": []}
# gained: {"lines": [17, 18, 19, 20], "branches": []}

import pytest
from pymonet.either import Either

class TestEither:
    def test_eq_with_same_value_and_type(self):
        either1 = Either(10)
        either2 = Either(10)
        assert either1 == either2

    def test_eq_with_different_value(self):
        either1 = Either(10)
        either2 = Either(20)
        assert either1 != either2

    def test_eq_with_different_type(self):
        either1 = Either(10)
        either2 = "Not an Either"
        assert either1 != either2

    def test_eq_with_different_is_right(self, mocker):
        either1 = Either(10)
        either2 = Either(10)
        
        mocker.patch.object(either1, 'is_right', return_value=True)
        mocker.patch.object(either2, 'is_right', return_value=False)
        
        assert either1 != either2
