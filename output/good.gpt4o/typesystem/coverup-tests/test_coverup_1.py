# file typesystem/composites.py:57-73
# lines [57, 58, 65, 66, 67, 68, 70, 71, 72, 73]
# branches ['71->72', '71->73']

import pytest
from typesystem.composites import AllOf
from typesystem.fields import Field

class MockField(Field):
    def validate(self, value, strict=False):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")

def test_allof_validate():
    field1 = MockField()
    field2 = MockField()
    all_of = AllOf(all_of=[field1, field2])

    # Test with valid value
    value = 10
    assert all_of.validate(value) == value

    # Test with invalid value
    with pytest.raises(ValueError, match="Value must be an integer"):
        all_of.validate("invalid")

    # Test with strict mode
    assert all_of.validate(value, strict=True) == value

    # Test with invalid value in strict mode
    with pytest.raises(ValueError, match="Value must be an integer"):
        all_of.validate("invalid", strict=True)
