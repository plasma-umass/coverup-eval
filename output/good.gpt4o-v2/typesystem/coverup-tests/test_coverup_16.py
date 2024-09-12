# file: typesystem/composites.py:57-73
# asked: {"lines": [57, 58, 65, 66, 67, 68, 70, 71, 72, 73], "branches": [[71, 72], [71, 73]]}
# gained: {"lines": [57, 58, 65, 66, 67, 68, 70, 71, 72, 73], "branches": [[71, 72], [71, 73]]}

import pytest
import typing
from typesystem.fields import Field
from typesystem.composites import AllOf

class MockField(Field):
    def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        return value

def test_allof_initialization():
    field1 = MockField()
    field2 = MockField()
    all_of = AllOf(all_of=[field1, field2])
    assert all_of.all_of == [field1, field2]

def test_allof_validate():
    field1 = MockField()
    field2 = MockField()
    all_of = AllOf(all_of=[field1, field2])
    
    # This should pass as both fields expect an integer
    assert all_of.validate(5) == 5
    
    # This should raise a ValueError as both fields expect an integer
    with pytest.raises(ValueError):
        all_of.validate("not an integer")

def test_allof_allow_null_assertion():
    field1 = MockField()
    field2 = MockField()
    
    # This should raise an AssertionError because 'allow_null' is in kwargs
    with pytest.raises(AssertionError):
        AllOf(all_of=[field1, field2], allow_null=True)
