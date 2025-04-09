# file: typesystem/composites.py:8-20
# asked: {"lines": [8, 9, 13, 15, 16, 17, 19, 20], "branches": []}
# gained: {"lines": [8, 9, 13, 15, 16, 17, 19, 20], "branches": []}

import pytest
from typesystem.composites import NeverMatch
from typesystem.fields import Field

class MockValidationError(Exception):
    def __init__(self, text, code):
        self.detail = text
        self.code = code

def mock_validation_error(self, code: str):
    text = self.get_error_text(code)
    return MockValidationError(text=text, code=code)

@pytest.fixture
def patch_validation_error(monkeypatch):
    monkeypatch.setattr(Field, 'validation_error', mock_validation_error)

def test_nevermatch_init():
    # Test that NeverMatch can be initialized without 'allow_null'
    field = NeverMatch()
    assert isinstance(field, NeverMatch)

    # Test that NeverMatch raises an assertion error if 'allow_null' is in kwargs
    with pytest.raises(AssertionError):
        NeverMatch(allow_null=True)

def test_nevermatch_validate(patch_validation_error):
    field = NeverMatch()
    
    # Test that validate always raises a ValidationError with the correct message
    with pytest.raises(MockValidationError) as exc_info:
        field.validate("any_value")
    assert exc_info.value.detail == "This never validates."
    assert exc_info.value.code == "never"
