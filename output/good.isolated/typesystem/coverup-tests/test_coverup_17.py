# file typesystem/fields.py:745-762
# lines [745, 746, 750, 752, 753, 754, 755, 757, 758, 759, 760, 761, 762]
# branches ['758->759', '758->762', '759->760', '759->761']

import pytest
from typesystem import ValidationError
from typesystem.fields import Const

def test_const_field_validation():
    const_field = Const(const=42)

    # Test that the correct value passes validation
    assert const_field.validate(42) == 42

    # Test that a different value raises the correct validation error
    with pytest.raises(ValidationError) as exc_info:
        const_field.validate(43)
    assert str(exc_info.value) == "Must be the value '42'."

    # Test that None raises the correct validation error if const is not None
    with pytest.raises(ValidationError) as exc_info:
        const_field.validate(None)
    assert str(exc_info.value) == "Must be the value '42'."

    # Test that None passes validation if const is None
    const_field_none = Const(const=None)
    assert const_field_none.validate(None) is None

    # Test that a non-None value raises the correct validation error if const is None
    with pytest.raises(ValidationError) as exc_info:
        const_field_none.validate(42)
    assert str(exc_info.value) == "Must be null."

def test_const_field_allow_null_error():
    with pytest.raises(AssertionError):
        Const(const=42, allow_null=True)
