# file typesystem/fields.py:736-742
# lines [736, 737, 741, 742]
# branches []

import pytest
from typesystem.fields import Any

def test_any_field_validate():
    any_field = Any()
    test_value = "test_value"
    assert any_field.validate(test_value) == test_value, "The Any field should return the input value unmodified."

    test_value = 12345
    assert any_field.validate(test_value) == test_value, "The Any field should return the input value unmodified."

    test_value = None
    assert any_field.validate(test_value) == test_value, "The Any field should return the input value unmodified."

    test_value = {"key": "value"}
    assert any_field.validate(test_value) == test_value, "The Any field should return the input value unmodified."

    test_value = [1, 2, 3]
    assert any_field.validate(test_value) == test_value, "The Any field should return the input value unmodified."
