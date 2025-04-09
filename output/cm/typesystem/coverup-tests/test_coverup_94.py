# file typesystem/composites.py:97-122
# lines [111, 112, 113, 114, 115, 118, 119, 120, 122]
# branches ['119->120', '119->122']

import pytest
from typesystem.composites import IfThenElse
from typesystem.fields import Field, Any
from typesystem import ValidationError

class MockField(Field):
    def validate(self, value, strict=False):
        if value == "trigger_error":
            raise ValidationError(text="Error triggered")
        return value

    def validate_or_error(self, value, strict=False):
        try:
            return self.validate(value, strict=strict), None
        except ValidationError as error:
            return None, error

@pytest.fixture
def mock_field():
    return MockField()

def test_if_then_else_validation(mock_field):
    if_clause = mock_field
    then_clause = mock_field
    else_clause = mock_field

    # Test the 'then' clause
    if_then_else = IfThenElse(if_clause=if_clause, then_clause=then_clause)
    assert if_then_else.validate("valid_value") == "valid_value"

    # Test the 'else' clause
    if_then_else = IfThenElse(if_clause=if_clause, else_clause=else_clause)
    assert if_then_else.validate("valid_value") == "valid_value"

    # Test assertion for 'allow_null' in kwargs
    with pytest.raises(AssertionError):
        IfThenElse(if_clause=if_clause, allow_null=True)

    # Test default Any() clause for 'then' and 'else'
    if_then_else = IfThenElse(if_clause=if_clause)
    assert if_then_else.validate("valid_value") == "valid_value"
    assert if_then_else.validate("trigger_error") == "trigger_error"
