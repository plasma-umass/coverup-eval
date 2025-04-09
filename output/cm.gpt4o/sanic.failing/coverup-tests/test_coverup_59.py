# file sanic/response.py:251-274
# lines [251, 253, 254, 255, 256, 267, 268, 269, 270, 271, 272, 273]
# branches ['267->268', '267->269']

import pytest
from sanic.response import json, HTTPResponse
from unittest.mock import patch

def test_json_response_with_custom_dumps():
    def custom_dumps(body, **kwargs):
        return f"custom: {body}"

    body = {"key": "value"}
    response = json(body, dumps=custom_dumps)
    
    assert isinstance(response, HTTPResponse)
    assert response.body == b"custom: {'key': 'value'}"
    assert response.status == 200
    assert response.content_type == "application/json"

def test_json_response_with_default_dumps(mocker):
    body = {"key": "value"}
    mock_dumps = mocker.patch('sanic.response.BaseHTTPResponse._dumps', return_value='{"key": "value"}')
    
    response = json(body)
    
    mock_dumps.assert_called_once_with(body)
    assert isinstance(response, HTTPResponse)
    assert response.body == b'{"key": "value"}'
    assert response.status == 200
    assert response.content_type == "application/json"

def test_json_response_with_custom_headers():
    body = {"key": "value"}
    headers = {"X-Custom-Header": "value"}
    
    response = json(body, headers=headers)
    
    assert isinstance(response, HTTPResponse)
    assert response.headers["X-Custom-Header"] == "value"
    assert response.status == 200
    assert response.content_type == "application/json"
