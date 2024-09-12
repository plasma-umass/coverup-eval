# file: pymonet/either.py:81-82
# asked: {"lines": [82], "branches": []}
# gained: {"lines": [82], "branches": []}

import pytest
from pymonet.either import Either

def test_either_is_right():
    either_instance = Either(value="test_value")
    assert either_instance.is_right() is None
