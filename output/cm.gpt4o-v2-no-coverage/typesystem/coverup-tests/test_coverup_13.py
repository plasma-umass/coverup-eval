# file: typesystem/composites.py:97-122
# asked: {"lines": [97, 98, 104, 107, 108, 111, 112, 113, 114, 115, 117, 118, 119, 120, 122], "branches": [[119, 120], [119, 122]]}
# gained: {"lines": [97, 98, 104, 107, 108, 111, 112, 113, 114, 115, 117, 118, 119, 120, 122], "branches": [[119, 120], [119, 122]]}

import pytest
from typesystem.fields import Field, String, Integer
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
            raise ValueError("error")
        return value

def test_if_then_else_init():
    if_clause = MockField()
    then_clause = MockField()
    else_clause = MockField()
    
    field = IfThenElse(if_clause, then_clause, else_clause)
    
    assert field.if_clause == if_clause
    assert field.then_clause == then_clause
    assert field.else_clause == else_clause

def test_if_then_else_init_defaults():
    if_clause = MockField()
    
    field = IfThenElse(if_clause)
    
    assert field.if_clause == if_clause
    assert isinstance(field.then_clause, Field)
    assert isinstance(field.else_clause, Field)

def test_if_then_else_validate_then_clause():
    if_clause = MockField()
    then_clause = MockField()
    else_clause = MockField()
    
    field = IfThenElse(if_clause, then_clause, else_clause)
    
    result = field.validate("test")
    
    assert result == "test"

def test_if_then_else_validate_else_clause():
    if_clause = MockField(should_error=True)
    then_clause = MockField()
    else_clause = MockField()
    
    field = IfThenElse(if_clause, then_clause, else_clause)
    
    result = field.validate("test")
    
    assert result == "test"

def test_if_then_else_validate_strict():
    if_clause = MockField()
    then_clause = MockField()
    else_clause = MockField()
    
    field = IfThenElse(if_clause, then_clause, else_clause)
    
    result = field.validate("test", strict=True)
    
    assert result == "test"

def test_if_then_else_validate_else_clause_strict():
    if_clause = MockField(should_error=True)
    then_clause = MockField()
    else_clause = MockField()
    
    field = IfThenElse(if_clause, then_clause, else_clause)
    
    result = field.validate("test", strict=True)
    
    assert result == "test"
