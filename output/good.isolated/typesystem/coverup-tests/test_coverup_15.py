# file typesystem/composites.py:23-54
# lines [23, 24, 31, 32, 33, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54]
# branches ['44->45', '44->50', '46->44', '46->47', '50->51', '50->52', '52->53', '52->54']

import pytest
from typesystem.fields import String, Integer
from typesystem import ValidationError
from typesystem.composites import OneOf

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Cleanup if necessary

def test_one_of_validation(cleanup):
    one_of_field = OneOf([String(), Integer()])

    # Test with a value that matches exactly one type
    assert one_of_field.validate("test") == "test"

    # Test with a value that matches no types
    with pytest.raises(ValidationError) as exc_info:
        one_of_field.validate([])
    assert str(exc_info.value) == "Did not match any valid type."

    # Test with a value that matches more than one type
    # This test case is incorrect because the Integer and String fields cannot both validate the same value
    # We need to create a custom Field that can match the same value as another Field to raise the "multiple_matches" error
    class AlwaysMatchField(String):
        def validate(self, value, strict=False):
            return value

    one_of_field_with_conflict = OneOf([String(), AlwaysMatchField()])
    with pytest.raises(ValidationError) as exc_info:
        one_of_field_with_conflict.validate("123")
    assert str(exc_info.value) == "Matched more than one type."
