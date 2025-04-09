# file: pymonet/either.py:120-125
# asked: {"lines": [120, 125], "branches": []}
# gained: {"lines": [120, 125], "branches": []}

import pytest
from pymonet.either import Left

def test_left_is_right():
    left_instance = Left("error")
    assert not left_instance.is_right()
