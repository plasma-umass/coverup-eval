# file: typesystem/fields.py:78-79
# asked: {"lines": [78, 79], "branches": []}
# gained: {"lines": [78, 79], "branches": []}

import pytest
from typesystem.fields import Field

def test_get_error_text():
    field = Field(title="Test Field", description="A test field", default="default", allow_null=False)
    field.errors = {"required": "This field is required."}
    
    # Test with a valid error code
    error_text = field.get_error_text("required")
    assert error_text == "This field is required."
    
    # Test with an invalid error code
    with pytest.raises(KeyError):
        field.get_error_text("invalid_code")
