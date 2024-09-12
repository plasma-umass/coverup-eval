# file: pymonet/either.py:182-187
# asked: {"lines": [182, 187], "branches": []}
# gained: {"lines": [182, 187], "branches": []}

import pytest
from pymonet.either import Right

class TestRight:
    def test_is_left(self):
        right_instance = Right("value")
        assert not right_instance.is_left()
