# file sanic/response.py:251-274
# lines [268]
# branches ['267->268']

import pytest
from sanic.response import json, HTTPResponse
from unittest.mock import Mock

@pytest.fixture
def mock_dumps(mocker):
    return mocker.patch('sanic.response.BaseHTTPResponse._dumps', return_value='{}')

def test_json_with_custom_dumps(mock_dumps):
    custom_dumps = Mock(return_value='{"key": "value"}')
    response = json({"key": "value"}, dumps=custom_dumps)
    
    assert response.status == 200
    assert response.content_type == "application/json"
    assert response.body == b'{"key": "value"}'
    custom_dumps.assert_called_once_with({"key": "value"})
    mock_dumps.assert_not_called()

def test_json_without_custom_dumps(mock_dumps):
    response = json({"key": "value"})
    
    assert response.status == 200
    assert response.content_type == "application/json"
    assert response.body == b'{}'
    mock_dumps.assert_called_once_with({"key": "value"})
