# file: pymonet/either.py:88-95
# asked: {"lines": [88, 95], "branches": []}
# gained: {"lines": [88, 95], "branches": []}

import pytest
from pymonet.either import Either, Left

def test_left_map():
    left_instance = Left("error")
    new_left_instance = left_instance.map(lambda x: x + " modified")
    
    assert isinstance(new_left_instance, Left)
    assert new_left_instance.value == "error"
    assert new_left_instance is not left_instance
