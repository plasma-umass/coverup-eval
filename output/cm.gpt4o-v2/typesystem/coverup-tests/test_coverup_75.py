# file: typesystem/fields.py:74-76
# asked: {"lines": [74, 75, 76], "branches": []}
# gained: {"lines": [74, 75, 76], "branches": []}

import pytest
from typesystem.fields import Field
from typesystem.base import ValidationError

class MockField(Field):
    def get_error_text(self, code: str) -> str:
        return f"Error text for {code}"

def test_validation_error():
    field = MockField()
    error_code = "invalid"
    error = field.validation_error(error_code)
    
    assert isinstance(error, ValidationError)
    assert error._messages[0].code == error_code
    assert error._messages[0].text == "Error text for invalid"
