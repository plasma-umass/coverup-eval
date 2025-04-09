# file: pymonet/either.py:175-180
# asked: {"lines": [175, 180], "branches": []}
# gained: {"lines": [175, 180], "branches": []}

import pytest
from pymonet.either import Right

class TestEither:
    def test_right_is_right(self):
        right_instance = Right("test_value")
        assert right_instance.is_right() == True
