# file typesystem/composites.py:57-73
# lines [57, 58, 65, 66, 67, 68, 70, 71, 72, 73]
# branches ['71->72', '71->73']

import pytest
from typesystem.composites import AllOf
from typesystem.fields import Field
import typing

class MockField(Field):
    def validate(self, value: typing.Any, strict: bool = False) -> typing.Any:
        return value

@pytest.fixture
def mock_field(mocker):
    field = MockField()
    mocker.spy(field, 'validate')
    return field

def test_allof_validation(mock_field):
    all_of = AllOf(all_of=[mock_field, mock_field])

    test_value = "test"
    result = all_of.validate(test_value)

    assert result == test_value
    assert mock_field.validate.call_count == 2
    mock_field.validate.assert_any_call(test_value, strict=False)

def test_allof_validation_with_strict(mock_field):
    all_of = AllOf(all_of=[mock_field, mock_field])

    test_value = "test"
    result = all_of.validate(test_value, strict=True)

    assert result == test_value
    assert mock_field.validate.call_count == 2
    mock_field.validate.assert_any_call(test_value, strict=True)

def test_allof_init_with_allow_null():
    with pytest.raises(AssertionError):
        AllOf(all_of=[], allow_null=True)
