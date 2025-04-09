# file: typesystem/composites.py:76-94
# asked: {"lines": [76, 77, 83, 85, 86, 87, 88, 90, 91, 92, 93, 94], "branches": [[92, 93], [92, 94]]}
# gained: {"lines": [76, 77, 83, 85, 86, 87, 88, 90, 91, 92, 93, 94], "branches": [[92, 93], [92, 94]]}

import pytest
from typesystem.fields import Field, ValidationError
from typesystem.composites import Not

class MockField(Field):
    def __init__(self, should_error=False, **kwargs):
        super().__init__(**kwargs)
        self.should_error = should_error

    def validate_or_error(self, value, strict=False):
        if self.should_error:
            return value, "error"
        return value, None

    def validation_error(self, code):
        return ValidationError(text=self.get_error_text(code), code=code)

def test_not_field_initialization():
    negated_field = MockField()
    not_field = Not(negated=negated_field)
    assert not_field.negated == negated_field

def test_not_field_validate_success():
    negated_field = MockField(should_error=True)
    not_field = Not(negated=negated_field)
    value = "test_value"
    assert not_field.validate(value) == value

def test_not_field_validate_failure():
    negated_field = MockField(should_error=False)
    not_field = Not(negated=negated_field)
    with pytest.raises(ValidationError) as exc_info:
        not_field.validate("test_value")
    assert str(exc_info.value) == "Must not match."

def test_not_field_allow_null_assertion():
    negated_field = MockField()
    with pytest.raises(AssertionError):
        Not(negated=negated_field, allow_null=True)
