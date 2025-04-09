# file typesystem/composites.py:76-94
# lines [86, 87, 88, 91, 92, 93, 94]
# branches ['92->93', '92->94']

import pytest
from typesystem import Field, ValidationError
from typesystem.composites import Not

class DummyField(Field):
    def validate(self, value, strict=False):
        if value == "invalid":
            raise ValidationError(text="Invalid value.")
        return value

@pytest.fixture
def dummy_field():
    return DummyField()

def test_not_field_validation_passes(dummy_field):
    not_field = Not(negated=dummy_field)
    assert not_field.validate("invalid") == "invalid"

def test_not_field_validation_fails(dummy_field):
    not_field = Not(negated=dummy_field)
    with pytest.raises(ValidationError) as exc_info:
        not_field.validate("valid")
    assert str(exc_info.value) == "Must not match."

def test_not_field_with_allow_null_raises_assertion_error(dummy_field):
    with pytest.raises(AssertionError):
        Not(negated=dummy_field, allow_null=True)
