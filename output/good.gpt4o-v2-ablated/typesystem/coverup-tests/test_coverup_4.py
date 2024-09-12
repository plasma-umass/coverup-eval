# file: typesystem/composites.py:23-54
# asked: {"lines": [23, 24, 31, 32, 33, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54], "branches": [[44, 45], [44, 50], [46, 44], [46, 47], [50, 51], [50, 52], [52, 53], [52, 54]]}
# gained: {"lines": [23, 24, 31, 32, 33, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54], "branches": [[44, 45], [44, 50], [46, 44], [46, 47], [50, 51], [50, 52], [52, 53], [52, 54]]}

import pytest
from typesystem import Field, ValidationError
from typesystem.composites import OneOf

class MockField(Field):
    def __init__(self, should_validate, return_value=None):
        self.should_validate = should_validate
        self.return_value = return_value

    def validate_or_error(self, value, strict=False):
        if self.should_validate:
            return self.return_value, None
        return None, "error"

def test_one_of_no_match():
    field1 = MockField(should_validate=False)
    field2 = MockField(should_validate=False)
    one_of = OneOf(one_of=[field1, field2])
    
    with pytest.raises(ValidationError) as excinfo:
        one_of.validate("test_value")
    
    assert str(excinfo.value) == "Did not match any valid type."

def test_one_of_single_match():
    field1 = MockField(should_validate=False)
    field2 = MockField(should_validate=True, return_value="validated_value")
    one_of = OneOf(one_of=[field1, field2])
    
    result = one_of.validate("test_value")
    
    assert result == "validated_value"

def test_one_of_multiple_matches():
    field1 = MockField(should_validate=True, return_value="validated_value1")
    field2 = MockField(should_validate=True, return_value="validated_value2")
    one_of = OneOf(one_of=[field1, field2])
    
    with pytest.raises(ValidationError) as excinfo:
        one_of.validate("test_value")
    
    assert str(excinfo.value) == "Matched more than one type."

def test_one_of_init_assertion():
    with pytest.raises(AssertionError):
        OneOf(one_of=[], allow_null=True)
