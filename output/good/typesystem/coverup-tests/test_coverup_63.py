# file typesystem/fields.py:186-189
# lines [186, 187, 188, 189]
# branches ['187->188', '187->189']

import pytest
from typesystem.fields import String

# Define a custom format for testing purposes
class CustomFormat:
    @classmethod
    def serialize(cls, obj):
        return f"custom-{obj}"

# Test function to cover the missing branch
def test_string_field_with_custom_format(mocker):
    # Mock the FORMATS dictionary to include the custom format
    mocker.patch.dict('typesystem.fields.FORMATS', {'custom': CustomFormat})

    # Setup: Create a String field with the custom format
    string_field = String(format="custom")

    # Execute: Serialize a value using the custom format
    serialized_value = string_field.serialize("test")

    # Verify: Check that the custom format was used
    assert serialized_value == "custom-test"
