# file: pymonet/either.py:182-187
# asked: {"lines": [187], "branches": []}
# gained: {"lines": [187], "branches": []}

import pytest
from pymonet.either import Right

def test_right_is_left():
    right_instance = Right("test_value")
    assert right_instance.is_left() is False
