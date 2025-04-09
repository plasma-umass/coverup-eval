# file: typesystem/composites.py:97-122
# asked: {"lines": [118, 119, 120, 122], "branches": [[119, 120], [119, 122]]}
# gained: {"lines": [118, 119, 120, 122], "branches": [[119, 120], [119, 122]]}

import pytest
from typesystem.fields import Field, Any
from typesystem.composites import IfThenElse

class MockField(Field):
    def __init__(self, should_error=False):
        super().__init__()
        self.should_error = should_error

    def validate_or_error(self, value, strict=False):
        if self.should_error:
            return None, "error"
        return value, None

    def validate(self, value, strict=False):
        if self.should_error:
            raise ValueError("Validation failed")
        return value

def test_if_then_else_then_clause():
    if_clause = MockField(should_error=False)
    then_clause = MockField(should_error=False)
    else_clause = MockField(should_error=True)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    result = field.validate("test_value")
    assert result == "test_value"

def test_if_then_else_else_clause():
    if_clause = MockField(should_error=True)
    then_clause = MockField(should_error=False)
    else_clause = MockField(should_error=False)
    field = IfThenElse(if_clause=if_clause, then_clause=then_clause, else_clause=else_clause)

    result = field.validate("test_value")
    assert result == "test_value"

def test_if_then_else_default_then_clause():
    if_clause = MockField(should_error=False)
    field = IfThenElse(if_clause=if_clause)

    result = field.validate("test_value")
    assert result == "test_value"

def test_if_then_else_default_else_clause():
    if_clause = MockField(should_error=True)
    field = IfThenElse(if_clause=if_clause)

    result = field.validate("test_value")
    assert result == "test_value"
