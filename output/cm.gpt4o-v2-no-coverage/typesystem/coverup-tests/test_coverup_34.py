# file: typesystem/fields.py:736-742
# asked: {"lines": [736, 737, 741, 742], "branches": []}
# gained: {"lines": [736, 737, 741, 742], "branches": []}

import pytest
from typesystem.fields import Any

def test_any_validate():
    any_field = Any()
    
    # Test with a simple value
    value = 123
    assert any_field.validate(value) == value
    
    # Test with a string
    value = "test"
    assert any_field.validate(value) == value
    
    # Test with a list
    value = [1, 2, 3]
    assert any_field.validate(value) == value
    
    # Test with a dictionary
    value = {"key": "value"}
    assert any_field.validate(value) == value
    
    # Test with strict=True
    value = 123
    assert any_field.validate(value, strict=True) == value
