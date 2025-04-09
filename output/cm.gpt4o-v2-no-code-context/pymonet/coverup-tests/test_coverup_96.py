# file: pymonet/either.py:113-118
# asked: {"lines": [113, 118], "branches": []}
# gained: {"lines": [113, 118], "branches": []}

import pytest
from pymonet.either import Left

class TestLeft:
    def test_is_left(self):
        left_instance = Left("error")
        assert left_instance.is_left() is True
