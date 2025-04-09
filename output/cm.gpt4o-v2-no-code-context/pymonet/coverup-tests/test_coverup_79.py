# file: pymonet/either.py:14-15
# asked: {"lines": [14, 15], "branches": []}
# gained: {"lines": [14, 15], "branches": []}

import pytest
from pymonet.either import Either

def test_either_initialization():
    value = 42
    either_instance = Either(value)
    assert either_instance.value == value

def test_either_initialization_with_string():
    value = "test"
    either_instance = Either(value)
    assert either_instance.value == value

def test_either_initialization_with_none():
    value = None
    either_instance = Either(value)
    assert either_instance.value is None
