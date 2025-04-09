# file: pymonet/either.py:88-95
# asked: {"lines": [95], "branches": []}
# gained: {"lines": [95], "branches": []}

import pytest
from pymonet.either import Left, Either

def test_left_map():
    left_instance = Left("error")
    mapped_instance = left_instance.map(lambda x: x + " mapped")
    
    assert isinstance(mapped_instance, Left)
    assert mapped_instance.value == "error"

