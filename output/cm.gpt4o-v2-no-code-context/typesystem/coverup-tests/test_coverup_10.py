# file: typesystem/composites.py:97-122
# asked: {"lines": [97, 98, 104, 107, 108, 111, 112, 113, 114, 115, 117, 118, 119, 120, 122], "branches": [[119, 120], [119, 122]]}
# gained: {"lines": [97, 98, 104, 107, 108, 111, 112, 113, 114, 115, 117, 118, 119, 120, 122], "branches": [[119, 120], [119, 122]]}

import pytest
from typesystem.composites import IfThenElse
from typesystem.fields import Field, Any

class MockField(Field):
    def __init__(self, should_error=False):
        self.should_error = should_error

    def validate_or_error(self, value, strict=False):
        if self.should_error:
            return None, "error"
        return value, None

    def validate(self, value, strict=False):
        if self.should_error:
            raise ValueError("error")
        return value

def test_if_then_else_then_clause():
    if_clause = MockField(should_error=False)
    then_clause = MockField(should_error=False)
    else_clause = MockField(should_error=True)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    
    result = field.validate("test")
    assert result == "test"

def test_if_then_else_else_clause():
    if_clause = MockField(should_error=True)
    then_clause = MockField(should_error=False)
    else_clause = MockField(should_error=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)
    
    result = field.validate("test")
    assert result == "test"

def test_if_then_else_default_then_clause():
    if_clause = MockField(should_error=False)
    else_clause = MockField(should_error=True)
    field = IfThenElse(if_clause=if_clause, else_clause=else_clause)
    
    result = field.validate("test")
    assert result == "test"

def test_if_then_else_default_else_clause():
    if_clause = MockField(should_error=True)
    then_clause = MockField(should_error=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause)
    
    result = field.validate("test")
    assert result == "test"

def test_if_then_else_assert_allow_null():
    if_clause = MockField(should_error=False)
    then_clause = MockField(should_error=False)
    else_clause = MockField(should_error=False)
    
    with pytest.raises(AssertionError):
        IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause, allow_null=True)
