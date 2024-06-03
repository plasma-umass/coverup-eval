# file typesystem/fields.py:305-306
# lines [305, 306]
# branches []

import pytest
from typesystem.fields import Number
import decimal
from typesystem.base import ValidationError

class Float(Number):
    numeric_type = float

def test_float_field():
    field = Float()

    # Test that the numeric_type is float
    assert field.numeric_type is float

    # Test that the field can validate a float value
    value = field.validate(3.14)
    assert value == 3.14

    # Test that the field raises a ValidationError for non-float value
    with pytest.raises(ValidationError, match="Must be a number."):
        field.validate("not a float")

    # Test that the field can handle None if it's allowed
    field.allow_null = True
    value = field.validate(None)
    assert value is None

    # Test that the field raises a ValidationError for None if it's not allowed
    field.allow_null = False
    with pytest.raises(ValidationError, match="null"):
        field.validate(None)
