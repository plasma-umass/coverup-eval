# file: typesystem/fields.py:62-63
# asked: {"lines": [62, 63], "branches": []}
# gained: {"lines": [62, 63], "branches": []}

import pytest
import typing
from typesystem.fields import Field

def test_field_serialize():
    field = Field()
    
    # Test with a string
    obj = "test_string"
    assert field.serialize(obj) == obj
    
    # Test with an integer
    obj = 123
    assert field.serialize(obj) == obj
    
    # Test with a list
    obj = [1, 2, 3]
    assert field.serialize(obj) == obj
    
    # Test with a dictionary
    obj = {"key": "value"}
    assert field.serialize(obj) == obj
    
    # Test with None
    obj = None
    assert field.serialize(obj) == obj
