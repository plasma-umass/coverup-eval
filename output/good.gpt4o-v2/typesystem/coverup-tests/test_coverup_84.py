# file: typesystem/fields.py:745-762
# asked: {"lines": [758, 759, 760, 761, 762], "branches": [[758, 759], [758, 762], [759, 760], [759, 761]]}
# gained: {"lines": [758, 759, 760, 761, 762], "branches": [[758, 759], [758, 762], [759, 760], [759, 761]]}

import pytest
from typesystem.fields import Const
from typesystem.base import ValidationError

def test_const_validate_correct_value():
    field = Const(const=5)
    assert field.validate(5) == 5

def test_const_validate_incorrect_value():
    field = Const(const=5)
    with pytest.raises(ValidationError) as exc_info:
        field.validate(3)
    assert str(exc_info.value) == "Must be the value '5'."

def test_const_validate_null_value():
    field = Const(const=None)
    with pytest.raises(ValidationError) as exc_info:
        field.validate(3)
    assert str(exc_info.value) == "Must be null."

def test_const_validate_correct_null_value():
    field = Const(const=None)
    assert field.validate(None) is None
