# file: typesystem/fields.py:736-742
# asked: {"lines": [736, 737, 741, 742], "branches": []}
# gained: {"lines": [736, 737, 741, 742], "branches": []}

import pytest
from typesystem.fields import Any

def test_any_validate():
    any_field = Any()
    value = "test_value"
    
    # Test validate method
    assert any_field.validate(value) == value
    assert any_field.validate(value, strict=True) == value
