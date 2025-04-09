# file: typesystem/composites.py:23-54
# asked: {"lines": [23, 24, 31, 32, 33, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54], "branches": [[44, 45], [44, 50], [46, 44], [46, 47], [50, 51], [50, 52], [52, 53], [52, 54]]}
# gained: {"lines": [23, 24, 31, 32, 33, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54], "branches": [[44, 45], [44, 50], [46, 44], [46, 47], [50, 51], [50, 52], [52, 53], [52, 54]]}

import pytest
from typesystem.composites import OneOf
from typesystem.fields import String, Integer

def test_oneof_no_match():
    field = OneOf([String(), Integer()])
    with pytest.raises(Exception) as excinfo:
        field.validate(3.14)
    assert str(excinfo.value) == "Did not match any valid type."

def test_oneof_single_match():
    field = OneOf([String(), Integer()])
    assert field.validate("test") == "test"

def test_oneof_multiple_matches():
    class CustomField:
        def validate_or_error(self, value, strict=False):
            if value == "match":
                return value, None
            return None, "error"

    field = OneOf([CustomField(), CustomField()])
    with pytest.raises(Exception) as excinfo:
        field.validate("match")
    assert str(excinfo.value) == "Matched more than one type."

def test_oneof_init():
    with pytest.raises(AssertionError):
        OneOf([String(), Integer()], allow_null=True)

@pytest.fixture
def mock_field(mocker):
    mock_field = mocker.Mock()
    mock_field.validate_or_error.side_effect = lambda value, strict=False: (value, None) if value == "valid" else (None, "error")
    return mock_field

def test_oneof_validate_with_mock(mock_field):
    field = OneOf([mock_field])
    assert field.validate("valid") == "valid"
    with pytest.raises(Exception) as excinfo:
        field.validate("invalid")
    assert str(excinfo.value) == "Did not match any valid type."
