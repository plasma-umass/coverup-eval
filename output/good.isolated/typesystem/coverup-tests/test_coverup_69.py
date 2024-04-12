# file typesystem/fields.py:305-306
# lines [305, 306]
# branches []

import pytest
from typesystem.fields import Float
from typesystem import ValidationError

def test_float_field():
    float_field = Float()
    assert float_field.numeric_type == float

    # Test validation with correct type
    validated_value, error = float_field.validate_or_error(123.45)
    assert validated_value == 123.45
    assert error is None

    # Test validation with incorrect type and ensure it raises a validation error
    _, error = float_field.validate_or_error("not a float")
    assert isinstance(error, ValidationError)
    assert 'Must be a number.' in str(error)
