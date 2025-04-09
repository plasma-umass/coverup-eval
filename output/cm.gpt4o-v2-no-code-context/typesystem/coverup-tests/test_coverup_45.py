# file: typesystem/fields.py:305-306
# asked: {"lines": [305, 306], "branches": []}
# gained: {"lines": [305, 306], "branches": []}

import pytest
from typesystem.fields import Number
from typesystem import ValidationError

def test_float_class():
    class Float(Number):
        numeric_type = float

    # Verify that the numeric_type is indeed float
    assert Float.numeric_type is float

    # Verify that an instance of Float can be created and used as expected
    float_instance = Float()
    assert isinstance(float_instance, Float)
    assert float_instance.numeric_type is float

    # Verify that the Float class can handle float values correctly
    assert float_instance.validate(3.14) == 3.14

    # Verify that the Float class raises an error for non-float values
    with pytest.raises(ValidationError):
        float_instance.validate("not a float")
