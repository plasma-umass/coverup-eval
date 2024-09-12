# file: typesystem/composites.py:76-94
# asked: {"lines": [76, 77, 83, 85, 86, 87, 88, 90, 91, 92, 93, 94], "branches": [[92, 93], [92, 94]]}
# gained: {"lines": [76, 77, 83, 85, 86, 87, 88, 90, 91, 92, 93, 94], "branches": [[92, 93], [92, 94]]}

import pytest
import typing
from typesystem.fields import Field
from typesystem.composites import Not

class MockField(Field):
    def validate_or_error(self, value: typing.Any, *, strict: bool=False):
        if value == "error":
            return None, "error"
        return value, None

def test_not_field_with_error():
    negated_field = MockField()
    not_field = Not(negated=negated_field)
    
    # This should pass as the negated field returns an error
    assert not_field.validate("error") == "error"

def test_not_field_without_error():
    negated_field = MockField()
    not_field = Not(negated=negated_field)
    
    # This should raise a validation error as the negated field does not return an error
    with pytest.raises(Exception) as exc_info:
        not_field.validate("no_error")
    
    assert str(exc_info.value) == "Must not match."
