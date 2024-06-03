# file typesystem/composites.py:23-54
# lines [23, 24, 31, 32, 33, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54]
# branches ['44->45', '44->50', '46->44', '46->47', '50->51', '50->52', '52->53', '52->54']

import pytest
from typesystem.composites import OneOf
from typesystem.fields import Integer, String

def test_oneof_no_match():
    field = OneOf([Integer(), String()])
    with pytest.raises(Exception) as excinfo:
        field.validate(3.14)
    assert str(excinfo.value) == "Did not match any valid type."

def test_oneof_multiple_matches():
    class CustomField:
        def validate_or_error(self, value, strict=False):
            if value == "test":
                return value, None
            return None, "error"

    field = OneOf([String(), CustomField()])
    with pytest.raises(Exception) as excinfo:
        field.validate("test")
    assert str(excinfo.value) == "Matched more than one type."

def test_oneof_single_match():
    field = OneOf([Integer(), String()])
    assert field.validate(123) == 123
    assert field.validate("test") == "test"
