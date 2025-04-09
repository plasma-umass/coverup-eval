# file: pymonet/utils.py:25-34
# asked: {"lines": [25, 34], "branches": []}
# gained: {"lines": [25, 34], "branches": []}

import pytest
from pymonet.utils import identity

def test_identity_with_int():
    result = identity(5)
    assert result == 5

def test_identity_with_string():
    result = identity("test")
    assert result == "test"

def test_identity_with_list():
    result = identity([1, 2, 3])
    assert result == [1, 2, 3]

def test_identity_with_dict():
    result = identity({"key": "value"})
    assert result == {"key": "value"}

def test_identity_with_none():
    result = identity(None)
    assert result is None
