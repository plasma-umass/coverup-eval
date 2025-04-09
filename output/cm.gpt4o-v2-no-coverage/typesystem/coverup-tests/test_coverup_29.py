# file: typesystem/composites.py:57-73
# asked: {"lines": [57, 58, 65, 66, 67, 68, 70, 71, 72, 73], "branches": [[71, 72], [71, 73]]}
# gained: {"lines": [57, 58, 65, 66, 67, 68, 70, 71, 72, 73], "branches": [[71, 72], [71, 73]]}

import pytest
import typing
from typesystem.fields import Field
from typesystem.composites import AllOf

class MockField(Field):
    def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
        return value

def test_allof_init():
    field1 = MockField()
    field2 = MockField()
    all_of = AllOf(all_of=[field1, field2])
    assert all_of.all_of == [field1, field2]

def test_allof_init_with_allow_null():
    with pytest.raises(AssertionError):
        AllOf(all_of=[], allow_null=True)

def test_allof_validate():
    field1 = MockField()
    field2 = MockField()
    all_of = AllOf(all_of=[field1, field2])
    value = "test"
    assert all_of.validate(value) == value

def test_allof_validate_strict():
    field1 = MockField()
    field2 = MockField()
    all_of = AllOf(all_of=[field1, field2])
    value = "test"
    assert all_of.validate(value, strict=True) == value
