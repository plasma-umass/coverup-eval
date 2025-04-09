# file: pymonet/either.py:14-15
# asked: {"lines": [14, 15], "branches": []}
# gained: {"lines": [14, 15], "branches": []}

import pytest
from pymonet.either import Either

def test_either_init():
    value = 42
    either = Either(value)
    assert either.value == value
