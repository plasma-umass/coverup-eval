# file: typesystem/composites.py:23-54
# asked: {"lines": [37, 38, 39, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54], "branches": [[44, 45], [44, 50], [46, 44], [46, 47], [50, 51], [50, 52], [52, 53], [52, 54]]}
# gained: {"lines": [37, 38, 39, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54], "branches": [[44, 45], [44, 50], [46, 44], [46, 47], [50, 51], [50, 52], [52, 53], [52, 54]]}

import pytest
from typesystem.fields import Field
from typesystem.composites import OneOf

class MockField(Field):
    def __init__(self, should_validate, validated_value=None):
        self.should_validate = should_validate
        self.validated_value = validated_value

    def validate_or_error(self, value, strict=False):
        if self.should_validate:
            return self.validated_value, None
        else:
            return None, "error"

def test_one_of_no_match():
    field = OneOf(one_of=[MockField(False), MockField(False)])
    with pytest.raises(Exception) as excinfo:
        field.validate("test")
    assert str(excinfo.value) == "Did not match any valid type."

def test_one_of_multiple_matches():
    field = OneOf(one_of=[MockField(True, "value1"), MockField(True, "value2")])
    with pytest.raises(Exception) as excinfo:
        field.validate("test")
    assert str(excinfo.value) == "Matched more than one type."

def test_one_of_single_match():
    field = OneOf(one_of=[MockField(True, "value1"), MockField(False)])
    result = field.validate("test")
    assert result == "value1"

def test_one_of_init_assertion():
    with pytest.raises(AssertionError):
        OneOf(one_of=[MockField(True)], allow_null=True)
