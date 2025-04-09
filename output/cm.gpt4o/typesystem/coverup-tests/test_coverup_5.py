# file typesystem/composites.py:97-122
# lines [97, 98, 104, 107, 108, 111, 112, 113, 114, 115, 117, 118, 119, 120, 122]
# branches ['119->120', '119->122']

import pytest
from typesystem.fields import Field, Any
from typesystem.composites import IfThenElse

class MockField(Field):
    def __init__(self, should_error=False):
        self.should_error = should_error

    def validate_or_error(self, value, strict=False):
        if self.should_error:
            return None, "error"
        return value, None

    def validate(self, value, strict=False):
        if self.should_error:
            raise ValueError("Validation failed")
        return value

def test_if_then_else():
    if_clause = MockField(should_error=False)
    then_clause = MockField(should_error=False)
    else_clause = MockField(should_error=True)

    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    
    # Test when if_clause passes
    value = "test_value"
    assert field.validate(value) == value

    # Test when if_clause fails and else_clause is used
    if_clause.should_error = True
    else_clause.should_error = False
    assert field.validate(value) == value

    # Test default then_clause and else_clause
    field = IfThenElse(if_clause=if_clause)
    assert field.validate(value) == value

    if_clause.should_error = False
    assert field.validate(value) == value

    # Test assertion error for "allow_null" in kwargs
    with pytest.raises(AssertionError):
        IfThenElse(if_clause=if_clause, allow_null=True)
