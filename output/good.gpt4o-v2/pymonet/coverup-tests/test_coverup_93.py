# file: pymonet/either.py:88-95
# asked: {"lines": [88, 95], "branches": []}
# gained: {"lines": [88, 95], "branches": []}

import pytest
from pymonet.either import Left

def test_left_map():
    left_instance = Left("error")
    mapped_instance = left_instance.map(lambda x: x)
    
    assert isinstance(mapped_instance, Left)
    assert mapped_instance.value == "error"
