# file: pymonet/either.py:120-125
# asked: {"lines": [120, 125], "branches": []}
# gained: {"lines": [120, 125], "branches": []}

import pytest
from pymonet.either import Left

class TestLeft:
    def test_is_right(self):
        left_instance = Left("error")
        assert not left_instance.is_right()
