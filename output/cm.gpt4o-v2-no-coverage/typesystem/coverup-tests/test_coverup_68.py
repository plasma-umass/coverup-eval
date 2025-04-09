# file: typesystem/fields.py:74-76
# asked: {"lines": [74, 75, 76], "branches": []}
# gained: {"lines": [74, 75, 76], "branches": []}

import pytest
from typesystem.base import ValidationError
from typesystem.fields import Field

class MockField(Field):
    errors = {
        "required": "This field is required.",
        "invalid": "Invalid value."
    }

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

@pytest.fixture
def mock_field():
    return MockField()

def test_validation_error_required(mock_field):
    error = mock_field.validation_error("required")
    assert isinstance(error, ValidationError)
    assert error._messages[0].text == "This field is required."
    assert error._messages[0].code == "required"

def test_validation_error_invalid(mock_field):
    error = mock_field.validation_error("invalid")
    assert isinstance(error, ValidationError)
    assert error._messages[0].text == "Invalid value."
    assert error._messages[0].code == "invalid"

def test_validation_error_unknown_code(mock_field):
    with pytest.raises(KeyError):
        mock_field.validation_error("unknown")

