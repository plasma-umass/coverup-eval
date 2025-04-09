# file typesystem/fields.py:697-733
# lines [725, 732]
# branches ['722->714', '729->732']

import pytest
from typesystem.fields import Union, Field
from typesystem import ValidationError

class MockField(Field):
    errors = {"type": "Invalid input."}

    def validate(self, value, strict=False):
        if value == "valid":
            return value
        raise self.validation_error("type")

class MockFieldWithIndexError(Field):
    errors = {"type": "Invalid input."}

    def validate(self, value, strict=False):
        if value == "valid":
            return value
        error = self.validation_error("type")
        error.messages()[0].index = 1  # Simulate an error with an index
        raise error

@pytest.fixture
def mock_field():
    return MockField()

@pytest.fixture
def mock_field_with_index_error():
    return MockFieldWithIndexError()

def test_union_field_validation_error_with_index(mock_field, mock_field_with_index_error):
    union_field = Union(any_of=[mock_field, mock_field_with_index_error])

    # Test that a ValidationError is raised with a message that has an index
    with pytest.raises(ValidationError) as exc_info:
        union_field.validate("invalid")
    assert exc_info.value.messages()[0].index == 1

    # Test that a ValidationError is raised for the union error
    with pytest.raises(ValidationError) as exc_info:
        union_field.validate(None)
    assert str(exc_info.value) == "May not be null."

    # Test that a ValidationError is raised for the union error with multiple candidate errors
    union_field_with_multiple_errors = Union(any_of=[mock_field_with_index_error, mock_field_with_index_error])
    with pytest.raises(ValidationError) as exc_info:
        union_field_with_multiple_errors.validate("invalid")
    assert str(exc_info.value) == "Did not match any valid type."
