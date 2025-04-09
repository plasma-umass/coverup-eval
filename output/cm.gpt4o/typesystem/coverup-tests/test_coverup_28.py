# file typesystem/json_schema.py:150-171
# lines [150, 154, 156, 157, 158, 159, 161, 163, 165, 166, 168, 169, 170]
# branches ['156->157', '156->165', '165->166', '165->168']

import pytest
from typesystem.json_schema import type_from_json_schema, SchemaDefinitions, Field, Union, Const, NeverMatch
from typesystem.json_schema import from_json_schema_type, get_valid_types

@pytest.fixture
def mock_get_valid_types(mocker):
    return mocker.patch('typesystem.json_schema.get_valid_types')

@pytest.fixture
def mock_from_json_schema_type(mocker):
    return mocker.patch('typesystem.json_schema.from_json_schema_type')

def test_type_from_json_schema_multiple_types(mock_get_valid_types, mock_from_json_schema_type):
    mock_get_valid_types.return_value = (['string', 'number'], False)
    mock_from_json_schema_type.side_effect = [Field(), Field()]
    data = {}
    definitions = SchemaDefinitions()
    
    result = type_from_json_schema(data, definitions)
    
    assert isinstance(result, Union)
    assert len(result.any_of) == 2
    assert not result.allow_null

def test_type_from_json_schema_no_types_allow_null(mock_get_valid_types):
    mock_get_valid_types.return_value = ([], True)
    data = {}
    definitions = SchemaDefinitions()
    
    result = type_from_json_schema(data, definitions)
    
    assert isinstance(result, Const)

def test_type_from_json_schema_no_types_disallow_null(mock_get_valid_types):
    mock_get_valid_types.return_value = ([], False)
    data = {}
    definitions = SchemaDefinitions()
    
    result = type_from_json_schema(data, definitions)
    
    assert isinstance(result, NeverMatch)

def test_type_from_json_schema_single_type(mock_get_valid_types, mock_from_json_schema_type):
    mock_get_valid_types.return_value = (['string'], False)
    mock_from_json_schema_type.return_value = Field()
    data = {}
    definitions = SchemaDefinitions()
    
    result = type_from_json_schema(data, definitions)
    
    assert isinstance(result, Field)
    mock_from_json_schema_type.assert_called_once_with(data, type_string='string', allow_null=False, definitions=definitions)
