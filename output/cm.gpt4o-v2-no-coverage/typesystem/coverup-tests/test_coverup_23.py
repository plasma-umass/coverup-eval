# file: typesystem/fields.py:745-762
# asked: {"lines": [745, 746, 750, 752, 753, 754, 755, 757, 758, 759, 760, 761, 762], "branches": [[758, 759], [758, 762], [759, 760], [759, 761]]}
# gained: {"lines": [745, 746, 750, 752, 753, 754, 755, 757, 758, 759, 760, 761, 762], "branches": [[758, 759], [758, 762], [759, 760], [759, 761]]}

import pytest
from typesystem.fields import Const
from typesystem import Field, ValidationError

class MockField(Field):
    def __init__(self, **kwargs):
        pass

    def validation_error(self, code):
        return ValidationError(Const.errors[code])

@pytest.fixture
def mock_field(monkeypatch):
    monkeypatch.setattr("typesystem.fields.Field", MockField)

def test_const_init(mock_field):
    const_value = 42
    const_field = Const(const=const_value)
    assert const_field.const == const_value

    with pytest.raises(AssertionError):
        Const(const=const_value, allow_null=True)

def test_const_validate(mock_field):
    const_value = 42
    const_field = Const(const=const_value)

    assert const_field.validate(42) == 42

    with pytest.raises(ValidationError, match="Must be the value '42'."):
        const_field.validate(43)

    null_const_field = Const(const=None)

    assert null_const_field.validate(None) is None

    with pytest.raises(ValidationError, match="Must be null."):
        null_const_field.validate(43)
