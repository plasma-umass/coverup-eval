# file: typesystem/fields.py:736-742
# asked: {"lines": [736, 737, 741, 742], "branches": []}
# gained: {"lines": [736, 737, 741, 742], "branches": []}

import pytest
from typesystem.fields import Any

def test_any_field_validate():
    any_field = Any()
    value = "test_value"
    assert any_field.validate(value) == value
    assert any_field.validate(123) == 123
    assert any_field.validate(None) is None
    assert any_field.validate([1, 2, 3]) == [1, 2, 3]
