# file: pymonet/either.py:97-104
# asked: {"lines": [97, 104], "branches": []}
# gained: {"lines": [97, 104], "branches": []}

import pytest
from pymonet.either import Left, Either

class TestLeft:
    def test_bind(self):
        left_instance = Left("error")
        result = left_instance.bind(lambda x: x)
        assert result is left_instance
