# file: dataclasses_json/undefined.py:193-201
# asked: {"lines": [193, 194, 195, 196, 197, 198, 199, 200, 201], "branches": [[198, 199], [198, 201]]}
# gained: {"lines": [193, 194, 195, 196, 197, 198, 199, 200, 201], "branches": [[198, 199], [198, 201]]}

import pytest
from unittest.mock import MagicMock
from dataclasses import Field
from typing import Any, Dict
from dataclasses_json.undefined import _CatchAllUndefinedParameters

@pytest.fixture
def mock_obj():
    class MockObj:
        pass
    return MockObj()

@pytest.fixture
def mock_field():
    field = MagicMock(spec=Field)
    field.name = "catch_all"
    return field

def test_handle_to_dict_with_dict(mock_obj, mock_field, monkeypatch):
    # Mock the _get_catch_all_field method to return the mock field
    monkeypatch.setattr(_CatchAllUndefinedParameters, "_get_catch_all_field", lambda obj: mock_field)
    
    # Create a dictionary with the catch-all field name
    kvs = {"catch_all": {"key1": "value1", "key2": "value2"}}
    
    # Call the handle_to_dict method
    result = _CatchAllUndefinedParameters.handle_to_dict(mock_obj, kvs)
    
    # Assert that the result contains the updated key-value pairs
    assert result == {"key1": "value1", "key2": "value2"}

def test_handle_to_dict_without_dict(mock_obj, mock_field, monkeypatch):
    # Mock the _get_catch_all_field method to return the mock field
    monkeypatch.setattr(_CatchAllUndefinedParameters, "_get_catch_all_field", lambda obj: mock_field)
    
    # Create a dictionary without the catch-all field name
    kvs = {"catch_all": "not_a_dict"}
    
    # Call the handle_to_dict method
    result = _CatchAllUndefinedParameters.handle_to_dict(mock_obj, kvs)
    
    # Assert that the result is unchanged
    assert result == kvs
