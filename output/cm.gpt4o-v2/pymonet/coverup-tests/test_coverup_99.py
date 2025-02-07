# file: pymonet/either.py:113-118
# asked: {"lines": [113, 118], "branches": []}
# gained: {"lines": [113, 118], "branches": []}

import pytest
from pymonet.either import Left

def test_left_is_left():
    left_instance = Left("error")
    assert left_instance.is_left() is True

def test_left_is_not_right():
    left_instance = Left("error")
    assert left_instance.is_right() is False
