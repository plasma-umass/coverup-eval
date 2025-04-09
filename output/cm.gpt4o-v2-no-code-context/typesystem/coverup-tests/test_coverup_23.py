# file: typesystem/composites.py:76-94
# asked: {"lines": [76, 77, 83, 85, 86, 87, 88, 90, 91, 92, 93, 94], "branches": [[92, 93], [92, 94]]}
# gained: {"lines": [76, 77, 83, 85, 86, 87, 88, 90, 91, 92, 93, 94], "branches": [[92, 93], [92, 94]]}

import pytest
from typesystem.composites import Not
from typesystem.fields import Field
from typesystem import ValidationError

class MockField(Field):
    def validate_or_error(self, value, strict=False):
        if value == "invalid":
            return None, "error"
        return value, None

def test_not_field_initialization():
    negated_field = MockField()
    not_field = Not(negated=negated_field)
    assert not_field.negated == negated_field

def test_not_field_validation_success():
    negated_field = MockField()
    not_field = Not(negated=negated_field)
    result = not_field.validate("invalid")
    assert result == "invalid"

def test_not_field_validation_failure():
    negated_field = MockField()
    not_field = Not(negated=negated_field)
    with pytest.raises(ValidationError) as excinfo:
        not_field.validate("valid")
    assert str(excinfo.value) == "Must not match."

def test_not_field_allow_null_assertion():
    negated_field = MockField()
    with pytest.raises(AssertionError):
        Not(negated=negated_field, allow_null=True)
