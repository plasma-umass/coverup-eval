# file: typesystem/composites.py:57-73
# asked: {"lines": [57, 58, 65, 66, 67, 68, 70, 71, 72, 73], "branches": [[71, 72], [71, 73]]}
# gained: {"lines": [57, 58, 65, 66, 67, 68, 70, 71, 72, 73], "branches": [[71, 72], [71, 73]]}

import pytest
from typesystem.composites import AllOf
from typesystem.fields import Field

class MockField(Field):
    def validate(self, value, strict=False):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")

def test_allof_init():
    field1 = MockField()
    field2 = MockField()
    all_of = AllOf(all_of=[field1, field2])
    assert all_of.all_of == [field1, field2]

def test_allof_validate_success():
    field1 = MockField()
    field2 = MockField()
    all_of = AllOf(all_of=[field1, field2])
    assert all_of.validate(10) == 10

def test_allof_validate_failure():
    field1 = MockField()
    field2 = MockField()
    all_of = AllOf(all_of=[field1, field2])
    with pytest.raises(ValueError, match="Value must be an integer"):
        all_of.validate("not an integer")

def test_allof_init_with_allow_null():
    with pytest.raises(AssertionError):
        AllOf(all_of=[], allow_null=True)
