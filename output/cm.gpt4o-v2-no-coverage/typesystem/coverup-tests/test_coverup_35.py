# file: typesystem/fields.py:316-353
# asked: {"lines": [316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 331, 332, 333, 335, 336, 338, 339, 340, 342, 343, 345, 346, 348, 349, 350, 351, 353], "branches": [[332, 333], [332, 335], [335, 336], [335, 338], [338, 339], [338, 353], [339, 340], [339, 342], [342, 343], [342, 345], [345, 346], [345, 348]]}
# gained: {"lines": [316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 331, 332, 333, 335, 336, 338, 339, 340, 342, 343, 345, 346, 348, 349, 350, 351, 353], "branches": [[332, 333], [332, 335], [335, 336], [335, 338], [338, 339], [338, 353], [339, 340], [339, 342], [342, 343], [342, 345], [345, 346], [345, 348]]}

import pytest
from typesystem.fields import Boolean

class MockField(Boolean):
    def __init__(self, allow_null=False):
        self.allow_null = allow_null

    def validation_error(self, error_type):
        return ValueError(Boolean.errors[error_type])

@pytest.fixture
def boolean_field():
    return MockField()

def test_validate_none_with_allow_null():
    field = MockField(allow_null=True)
    assert field.validate(None) is None

def test_validate_none_without_allow_null():
    field = MockField(allow_null=False)
    with pytest.raises(ValueError, match="May not be null."):
        field.validate(None)

def test_validate_non_bool_strict():
    field = MockField(allow_null=False)
    with pytest.raises(ValueError, match="Must be a boolean."):
        field.validate(1, strict=True)

def test_validate_non_bool_non_strict():
    field = MockField(allow_null=False)
    assert field.validate(1) is True

def test_validate_string_value():
    field = MockField(allow_null=False)
    assert field.validate("true") is True

def test_validate_string_value_with_allow_null():
    field = MockField(allow_null=True)
    assert field.validate("null") is None

def test_validate_invalid_string_value():
    field = MockField(allow_null=False)
    with pytest.raises(ValueError, match="Must be a boolean."):
        field.validate("invalid")

def test_validate_invalid_type():
    field = MockField(allow_null=False)
    with pytest.raises(ValueError, match="Must be a boolean."):
        field.validate([])

def test_validate_boolean_value():
    field = MockField(allow_null=False)
    assert field.validate(True) is True
    assert field.validate(False) is False
