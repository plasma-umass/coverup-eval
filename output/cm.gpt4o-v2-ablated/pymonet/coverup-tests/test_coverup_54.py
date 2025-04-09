# file: pymonet/either.py:88-95
# asked: {"lines": [88, 95], "branches": []}
# gained: {"lines": [88, 95], "branches": []}

import pytest
from pymonet.either import Either, Left

def test_left_map():
    left_instance = Left(10)
    new_left_instance = left_instance.map(lambda x: x + 1)
    
    assert isinstance(new_left_instance, Left)
    assert new_left_instance.value == 10
    assert new_left_instance is not left_instance
