# file: pymonet/utils.py:25-34
# asked: {"lines": [25, 34], "branches": []}
# gained: {"lines": [25, 34], "branches": []}

import pytest
from pymonet.utils import identity

def test_identity_with_int():
    assert identity(5) == 5

def test_identity_with_string():
    assert identity("test") == "test"

def test_identity_with_list():
    assert identity([1, 2, 3]) == [1, 2, 3]

def test_identity_with_dict():
    assert identity({"key": "value"}) == {"key": "value"}

def test_identity_with_none():
    assert identity(None) == None
