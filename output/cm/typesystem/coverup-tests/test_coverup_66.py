# file typesystem/fields.py:301-302
# lines [301, 302]
# branches []

import pytest
from typesystem import Integer

def test_integer_field():
    integer_field = Integer()
    assert integer_field.numeric_type == int

    # Test validation with correct type
    validated_value, error = integer_field.validate_or_error(123)
    assert validated_value == 123
    assert error is None

    # Test validation with incorrect type
    _, error = integer_field.validate_or_error("not an integer")
    assert error is not None
