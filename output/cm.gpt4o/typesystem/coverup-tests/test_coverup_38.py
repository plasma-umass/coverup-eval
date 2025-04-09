# file typesystem/json_schema.py:352-355
# lines [352, 353, 354, 355]
# branches []

import pytest
from typesystem.json_schema import all_of_from_json_schema, SchemaDefinitions, from_json_schema, AllOf, NO_DEFAULT

def test_all_of_from_json_schema(mocker):
    # Mock the from_json_schema function to return a simple Field object
    mock_field = mocker.Mock()
    mock_from_json_schema = mocker.patch('typesystem.json_schema.from_json_schema', return_value=mock_field)
    
    # Create a sample data dictionary
    data = {
        "allOf": [
            {"type": "string"},
            {"type": "number"}
        ],
        "default": "default_value"
    }
    
    # Create a mock SchemaDefinitions object
    definitions = mocker.Mock(spec=SchemaDefinitions)
    
    # Call the function
    result = all_of_from_json_schema(data, definitions)
    
    # Assertions to verify the function's behavior
    assert isinstance(result, AllOf)
    assert result.all_of == [mock_field, mock_field]
    assert result.default == "default_value"
    
    # Verify that from_json_schema was called with the correct arguments
    mock_from_json_schema.assert_any_call({"type": "string"}, definitions=definitions)
    mock_from_json_schema.assert_any_call({"type": "number"}, definitions=definitions)
