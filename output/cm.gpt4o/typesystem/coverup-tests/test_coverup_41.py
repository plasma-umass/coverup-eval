# file typesystem/json_schema.py:358-361
# lines [358, 359, 360, 361]
# branches []

import pytest
from typesystem.json_schema import any_of_from_json_schema, SchemaDefinitions, from_json_schema, Union, NO_DEFAULT

def test_any_of_from_json_schema(mocker):
    # Mock the from_json_schema function to return a simple Field object
    mock_field = mocker.Mock()
    mock_from_json_schema = mocker.patch('typesystem.json_schema.from_json_schema', return_value=mock_field)
    
    # Create a mock SchemaDefinitions object
    mock_definitions = mocker.Mock(spec=SchemaDefinitions)
    
    # Define the input data
    data = {
        "anyOf": [
            {"type": "string"},
            {"type": "number"}
        ],
        "default": "default_value"
    }
    
    # Call the function
    result = any_of_from_json_schema(data, mock_definitions)
    
    # Assertions to verify the correct behavior
    assert isinstance(result, Union)
    assert result.any_of == [mock_field, mock_field]
    assert result.default == "default_value"
    
    # Verify that from_json_schema was called with the correct arguments
    mock_from_json_schema.assert_any_call({"type": "string"}, definitions=mock_definitions)
    mock_from_json_schema.assert_any_call({"type": "number"}, definitions=mock_definitions)
    
    # Clean up
    mocker.stopall()
