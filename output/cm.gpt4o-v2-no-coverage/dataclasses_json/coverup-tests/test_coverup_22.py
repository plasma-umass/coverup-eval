# file: dataclasses_json/undefined.py:133-167
# asked: {"lines": [135, 136, 137, 138, 140, 142, 143, 144, 145, 148, 149, 150, 151, 152, 154, 155, 156, 158, 160, 161, 162, 164, 166, 167], "branches": [[140, 142], [140, 164], [148, 149], [148, 150], [150, 151], [150, 152], [152, 154], [152, 158], [155, 156], [155, 166]]}
# gained: {"lines": [135, 136, 137, 138, 140, 142, 143, 144, 145, 148, 150, 151, 152, 154, 155, 156, 158, 160, 161, 162, 164, 166, 167], "branches": [[140, 142], [140, 164], [148, 150], [150, 151], [150, 152], [152, 154], [152, 158], [155, 156]]}

import pytest
from unittest.mock import MagicMock, patch
from dataclasses import dataclass, Field
from typing import Any, Dict, Optional, Mapping, TypeVar
from dataclasses_json.undefined import _CatchAllUndefinedParameters, UndefinedParameterError

CatchAllVar = TypeVar('CatchAllVar', bound=Mapping)

@dataclass
class TestClass:
    known_field: int
    catch_all: Optional[CatchAllVar] = None

@pytest.fixture
def mock_separate_defined_undefined_kvs():
    with patch('dataclasses_json.undefined._UndefinedParameterAction._separate_defined_undefined_kvs') as mock:
        yield mock

@pytest.fixture
def mock_get_catch_all_field():
    with patch('dataclasses_json.undefined._CatchAllUndefinedParameters._get_catch_all_field') as mock:
        yield mock

@pytest.fixture
def mock_get_default():
    with patch('dataclasses_json.undefined._CatchAllUndefinedParameters._get_default') as mock:
        yield mock

def test_handle_from_dict_no_catch_all_field(mock_separate_defined_undefined_kvs, mock_get_catch_all_field):
    mock_separate_defined_undefined_kvs.return_value = ({'known_field': 1}, {'unknown_field': 'value'})
    mock_field = MagicMock(spec=Field)
    mock_field.name = 'catch_all'
    mock_get_catch_all_field.return_value = mock_field

    result = _CatchAllUndefinedParameters.handle_from_dict(TestClass, {'known_field': 1, 'unknown_field': 'value'})
    assert result == {'known_field': 1, 'catch_all': {'unknown_field': 'value'}}

def test_handle_from_dict_with_catch_all_field_default(mock_separate_defined_undefined_kvs, mock_get_catch_all_field, mock_get_default):
    mock_separate_defined_undefined_kvs.return_value = ({'known_field': 1, 'catch_all': None}, {'unknown_field': 'value'})
    mock_field = MagicMock(spec=Field)
    mock_field.name = 'catch_all'
    mock_get_catch_all_field.return_value = mock_field
    mock_get_default.return_value = None

    result = _CatchAllUndefinedParameters.handle_from_dict(TestClass, {'known_field': 1, 'unknown_field': 'value'})
    assert result == {'known_field': 1, 'catch_all': {'unknown_field': 'value'}}

def test_handle_from_dict_with_catch_all_field_already_parsed(mock_separate_defined_undefined_kvs, mock_get_catch_all_field, mock_get_default):
    mock_separate_defined_undefined_kvs.return_value = ({'known_field': 1, 'catch_all': {'existing': 'value'}}, {'unknown_field': 'value'})
    mock_field = MagicMock(spec=Field)
    mock_field.name = 'catch_all'
    mock_get_catch_all_field.return_value = mock_field
    mock_get_default.return_value = None

    result = _CatchAllUndefinedParameters.handle_from_dict(TestClass, {'known_field': 1, 'unknown_field': 'value'})
    assert result == {'known_field': 1, 'catch_all': {'existing': 'value', 'unknown_field': 'value'}}

def test_handle_from_dict_with_catch_all_field_conflict(mock_separate_defined_undefined_kvs, mock_get_catch_all_field, mock_get_default):
    mock_separate_defined_undefined_kvs.return_value = ({'known_field': 1, 'catch_all': 'conflict_value'}, {'unknown_field': 'value'})
    mock_field = MagicMock(spec=Field)
    mock_field.name = 'catch_all'
    mock_get_catch_all_field.return_value = mock_field
    mock_get_default.return_value = None

    with pytest.raises(UndefinedParameterError, match="Received input field with same name as catch-all field"):
        _CatchAllUndefinedParameters.handle_from_dict(TestClass, {'known_field': 1, 'unknown_field': 'value'})
