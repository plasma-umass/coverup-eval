# file: typesystem/fields.py:316-353
# asked: {"lines": [332, 333, 335, 336, 338, 339, 340, 342, 343, 345, 346, 348, 349, 350, 351, 353], "branches": [[332, 333], [332, 335], [335, 336], [335, 338], [338, 339], [338, 353], [339, 340], [339, 342], [342, 343], [342, 345], [345, 346], [345, 348]]}
# gained: {"lines": [332, 333, 335, 336, 338, 339, 340, 342, 343, 345, 346, 348, 349, 350, 351, 353], "branches": [[332, 333], [332, 335], [335, 336], [335, 338], [338, 339], [339, 340], [339, 342], [342, 343], [342, 345], [345, 346], [345, 348]]}

import pytest
from typesystem.fields import Boolean, Field

def test_boolean_validate_with_none_and_allow_null():
    field = Boolean(allow_null=True)
    assert field.validate(None) is None

def test_boolean_validate_with_none_and_not_allow_null():
    field = Boolean(allow_null=False)
    with pytest.raises(Exception) as excinfo:
        field.validate(None)
    assert str(excinfo.value) == "May not be null."

def test_boolean_validate_with_non_bool_strict():
    field = Boolean()
    with pytest.raises(Exception) as excinfo:
        field.validate("true", strict=True)
    assert str(excinfo.value) == "Must be a boolean."

def test_boolean_validate_with_non_bool_non_strict():
    field = Boolean()
    assert field.validate("true") is True
    assert field.validate("false") is False

def test_boolean_validate_with_non_bool_non_strict_invalid():
    field = Boolean()
    with pytest.raises(Exception) as excinfo:
        field.validate("invalid")
    assert str(excinfo.value) == "Must be a boolean."

def test_boolean_validate_with_coerce_null_values():
    field = Boolean(allow_null=True)
    assert field.validate("null") is None
    assert field.validate("none") is None
    assert field.validate("") is None

def test_boolean_validate_with_coerce_values():
    field = Boolean()
    assert field.validate("true") is True
    assert field.validate("false") is False
    assert field.validate("on") is True
    assert field.validate("off") is False
    assert field.validate("1") is True
    assert field.validate("0") is False
    assert field.validate(1) is True
    assert field.validate(0) is False
    assert field.validate("") is False

def test_boolean_validate_with_invalid_key():
    field = Boolean()
    with pytest.raises(Exception) as excinfo:
        field.validate("invalid_key")
    assert str(excinfo.value) == "Must be a boolean."

def test_boolean_validate_with_invalid_type():
    field = Boolean()
    with pytest.raises(Exception) as excinfo:
        field.validate([])
    assert str(excinfo.value) == "Must be a boolean."

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Clean up or reset any state if necessary
    yield
    # Reset any changes made during the tests
