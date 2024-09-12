# file: typesystem/composites.py:23-54
# asked: {"lines": [23, 24, 31, 32, 33, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54], "branches": [[44, 45], [44, 50], [46, 44], [46, 47], [50, 51], [50, 52], [52, 53], [52, 54]]}
# gained: {"lines": [23, 24, 31, 32, 33, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54], "branches": [[44, 45], [44, 50], [46, 44], [46, 47], [50, 51], [50, 52], [52, 53], [52, 54]]}

import pytest
from typesystem.composites import OneOf
from typesystem.fields import Field, ValidationError

class MockField(Field):
    def __init__(self, should_validate, **kwargs):
        super().__init__(**kwargs)
        self.should_validate = should_validate

    def validate_or_error(self, value, strict=False):
        if self.should_validate:
            return value, None
        return None, "error"

def test_one_of_no_match():
    field = OneOf(one_of=[MockField(False), MockField(False)])
    with pytest.raises(ValidationError) as excinfo:
        field.validate("test")
    assert str(excinfo.value) == "Did not match any valid type."

def test_one_of_single_match():
    field = OneOf(one_of=[MockField(True), MockField(False)])
    result = field.validate("test")
    assert result == "test"

def test_one_of_multiple_matches():
    field = OneOf(one_of=[MockField(True), MockField(True)])
    with pytest.raises(ValidationError) as excinfo:
        field.validate("test")
    assert str(excinfo.value) == "Matched more than one type."
