# file: typesystem/fields.py:745-762
# asked: {"lines": [745, 746, 750, 752, 753, 754, 755, 757, 758, 759, 760, 761, 762], "branches": [[758, 759], [758, 762], [759, 760], [759, 761]]}
# gained: {"lines": [745, 746, 750, 752, 753, 754, 755, 757, 758, 759, 760, 761, 762], "branches": [[758, 759], [758, 762], [759, 760], [759, 761]]}

import pytest
from typesystem.fields import Field, Const

def test_const_field_initialization():
    const_value = 42
    field = Const(const=const_value)
    assert field.const == const_value

def test_const_field_validation_success():
    const_value = 42
    field = Const(const=const_value)
    assert field.validate(const_value) == const_value

def test_const_field_validation_failure():
    const_value = 42
    field = Const(const=const_value)
    with pytest.raises(Exception) as exc_info:
        field.validate(43)
    assert str(exc_info.value) == "Must be the value '42'."

def test_const_field_validation_null_success():
    field = Const(const=None)
    assert field.validate(None) == None

def test_const_field_validation_null_failure():
    field = Const(const=None)
    with pytest.raises(Exception) as exc_info:
        field.validate(42)
    assert str(exc_info.value) == "Must be null."

def test_const_field_allow_null_not_in_kwargs():
    with pytest.raises(AssertionError):
        Const(const=42, allow_null=True)
