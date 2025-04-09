# file typesystem/json_schema.py:370-373
# lines [370, 371, 372, 373]
# branches []

import pytest
from typesystem.json_schema import not_from_json_schema, SchemaDefinitions, Field, Not, NO_DEFAULT

def test_not_from_json_schema(mocker):
    # Mock the from_json_schema function
    mock_from_json_schema = mocker.patch('typesystem.json_schema.from_json_schema')
    
    # Define the input data and expected output
    data = {
        "not": {"type": "string"},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()
    mock_field = Field()
    mock_from_json_schema.return_value = mock_field
    
    # Call the function
    result = not_from_json_schema(data, definitions)
    
    # Assertions to verify the function behavior
    mock_from_json_schema.assert_called_once_with(data["not"], definitions=definitions)
    assert isinstance(result, Not)
    assert result.negated == mock_field
    assert result.default == "default_value"
    
    # Clean up
    mock_from_json_schema.reset_mock()
