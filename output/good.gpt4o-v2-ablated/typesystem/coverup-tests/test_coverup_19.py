# file: typesystem/json_schema.py:358-361
# asked: {"lines": [358, 359, 360, 361], "branches": []}
# gained: {"lines": [358, 359, 360, 361], "branches": []}

import pytest
from typesystem.json_schema import any_of_from_json_schema, from_json_schema, SchemaDefinitions, Union, NO_DEFAULT

@pytest.fixture
def mock_from_json_schema(mocker):
    return mocker.patch('typesystem.json_schema.from_json_schema')

@pytest.fixture
def mock_union(mocker):
    return mocker.patch('typesystem.json_schema.Union')

def test_any_of_from_json_schema_with_default(mock_from_json_schema, mock_union):
    data = {
        "anyOf": [{"type": "string"}, {"type": "number"}],
        "default": "default_value"
    }
    definitions = SchemaDefinitions()
    mock_from_json_schema.side_effect = lambda item, definitions: item

    result = any_of_from_json_schema(data, definitions)

    assert mock_from_json_schema.call_count == 2
    assert mock_from_json_schema.call_args_list[0][0][0] == {"type": "string"}
    assert mock_from_json_schema.call_args_list[1][0][0] == {"type": "number"}
    assert mock_union.call_count == 1
    assert mock_union.call_args[1] == {"any_of": [{"type": "string"}, {"type": "number"}], "default": "default_value"}
    assert result == mock_union.return_value

def test_any_of_from_json_schema_without_default(mock_from_json_schema, mock_union):
    data = {
        "anyOf": [{"type": "string"}, {"type": "number"}]
    }
    definitions = SchemaDefinitions()
    mock_from_json_schema.side_effect = lambda item, definitions: item

    result = any_of_from_json_schema(data, definitions)

    assert mock_from_json_schema.call_count == 2
    assert mock_from_json_schema.call_args_list[0][0][0] == {"type": "string"}
    assert mock_from_json_schema.call_args_list[1][0][0] == {"type": "number"}
    assert mock_union.call_count == 1
    assert mock_union.call_args[1] == {"any_of": [{"type": "string"}, {"type": "number"}], "default": NO_DEFAULT}
    assert result == mock_union.return_value
