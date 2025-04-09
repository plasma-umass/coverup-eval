# file typesystem/fields.py:95-105
# lines [95, 96, 97, 98, 99, 100, 101, 102, 103]
# branches []

import pytest
from typesystem import ValidationError
from typesystem.fields import String

def test_string_field_errors():
    string_field = String()

    # Test 'type' error
    with pytest.raises(ValidationError) as exc_info:
        string_field.validate(123)
    assert str(exc_info.value) == "Must be a string."

    # Test 'null' error
    with pytest.raises(ValidationError) as exc_info:
        string_field.validate(None)
    assert str(exc_info.value) == "May not be null."

    # Test 'blank' error
    with pytest.raises(ValidationError) as exc_info:
        string_field.validate('')
    assert str(exc_info.value) == "Must not be blank."

    # Test 'max_length' error
    string_field = String(max_length=5)
    with pytest.raises(ValidationError) as exc_info:
        string_field.validate('toolong')
    assert str(exc_info.value) == "Must have no more than 5 characters."

    # Test 'min_length' error
    string_field = String(min_length=3)
    with pytest.raises(ValidationError) as exc_info:
        string_field.validate('a')
    assert str(exc_info.value) == "Must have at least 3 characters."

    # Test 'pattern' error
    string_field = String(pattern=r'^[a-z]+$')
    with pytest.raises(ValidationError) as exc_info:
        string_field.validate('123')
    assert str(exc_info.value) == "Must match the pattern /^[a-z]+$/."

    # The 'format' error is not raised by the String field itself, but by a subclass or a validator.
    # Therefore, we should not test for 'format' error here as it's not part of the String field's
    # responsibility. If there's a specific subclass or validator that handles the 'format' error,
    # the test should be written for that instead.
