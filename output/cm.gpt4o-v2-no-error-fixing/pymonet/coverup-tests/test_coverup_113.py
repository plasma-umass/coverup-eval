# file: pymonet/either.py:182-187
# asked: {"lines": [187], "branches": []}
# gained: {"lines": [187], "branches": []}

import pytest
from pymonet.either import Right

def test_right_is_left():
    right_instance = Right(10)
    assert not right_instance.is_left()
