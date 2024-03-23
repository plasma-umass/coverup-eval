# file typesystem/fields.py:697-733
# lines [697, 698, 700, 701, 703, 704, 705, 707, 708, 709, 710, 711, 713, 714, 715, 716, 717, 721, 722, 723, 724, 725, 727, 729, 732, 733]
# branches ['704->exit', '704->705', '708->709', '708->710', '710->711', '710->713', '714->715', '714->729', '716->717', '716->721', '722->714', '722->727', '729->732', '729->733']

import pytest
from typesystem.fields import Field, Union
from typesystem import ValidationError

class MockField(Field):
    def __init__(self, allow_null=False, raises=None, error_code=None):
        super().__init__()
        self.allow_null = allow_null
        self.raises = raises
        self.error_code = error_code
        self.errors = {error_code: "Error message for {error_code}."} if error_code else {}

    def validate(self, value, strict=False):
        if self.raises:
            raise self.validation_error(self.error_code)
        return value

@pytest.fixture
def mock_field():
    return MockField

def test_union_field_validation_error(mock_field):
    field1 = mock_field(raises=True, error_code="error1")
    field2 = mock_field(raises=True, error_code="error2")
    union_field = Union(any_of=[field1, field2])

    with pytest.raises(ValidationError) as exc_info:
        union_field.validate("test_value")
    assert str(exc_info.value) == "Did not match any valid type."

def test_union_field_single_candidate_error(mock_field):
    field1 = mock_field(raises=True, error_code="error1")
    field2 = mock_field()
    union_field = Union(any_of=[field1, field2])

    # Should not raise, as field2 does not raise an error
    assert union_field.validate("test_value") == "test_value"

def test_union_field_allow_null_with_null_value(mock_field):
    field1 = mock_field(allow_null=True)
    field2 = mock_field()
    union_field = Union(any_of=[field1, field2])

    # Should return None as field1 allows null
    assert union_field.validate(None) is None

def test_union_field_not_allow_null_with_null_value(mock_field):
    field1 = mock_field()
    field2 = mock_field()
    union_field = Union(any_of=[field1, field2])

    with pytest.raises(ValidationError) as exc_info:
        union_field.validate(None)
    assert str(exc_info.value) == "May not be null."
