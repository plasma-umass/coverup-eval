# file typesystem/json_schema.py:364-367
# lines [365, 366, 367]
# branches []

import pytest
from typesystem.json_schema import one_of_from_json_schema, SchemaDefinitions, Field, OneOf, from_json_schema

def test_one_of_from_json_schema(mocker):
    # Mock the from_json_schema function to return a simple Field object
    mock_field = mocker.Mock(spec=Field)
    mock_from_json_schema = mocker.patch('typesystem.json_schema.from_json_schema', return_value=mock_field)

    # Create a sample data dictionary that will trigger the lines in question
    data = {
        "oneOf": [
            {"type": "string"},
            {"type": "number"}
        ],
        "default": "default_value"
    }

    # Create a mock SchemaDefinitions object
    definitions = mocker.Mock(spec=SchemaDefinitions)

    # Call the function under test
    result = one_of_from_json_schema(data, definitions)

    # Assertions to verify the correct behavior
    assert isinstance(result, OneOf)
    assert result.one_of == [mock_field, mock_field]
    assert result.default == "default_value"

    # Verify that from_json_schema was called with the correct arguments
    mock_from_json_schema.assert_any_call({"type": "string"}, definitions=definitions)
    mock_from_json_schema.assert_any_call({"type": "number"}, definitions=definitions)
