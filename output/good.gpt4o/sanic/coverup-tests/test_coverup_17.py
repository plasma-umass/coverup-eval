# file sanic/response.py:251-274
# lines [251, 253, 254, 255, 256, 267, 268, 269, 270, 271, 272, 273]
# branches ['267->268', '267->269']

import pytest
from sanic.response import json, HTTPResponse
from unittest.mock import Mock

def test_json_response_with_custom_dumps():
    # Mock the custom dumps function
    custom_dumps = Mock(return_value='{"key": "value"}')
    
    # Call the json function with the custom dumps
    response = json({"key": "value"}, dumps=custom_dumps)
    
    # Assert that the custom dumps function was called
    custom_dumps.assert_called_once_with({"key": "value"})
    
    # Assert that the response is an instance of HTTPResponse
    assert isinstance(response, HTTPResponse)
    
    # Assert that the response body is the result of the custom dumps function
    assert response.body == b'{"key": "value"}'
    
    # Assert that the content type is application/json
    assert response.content_type == "application/json"
    
    # Assert that the status code is 200
    assert response.status == 200

def test_json_response_with_default_dumps(mocker):
    # Mock the default _dumps method
    default_dumps = mocker.patch('sanic.response.BaseHTTPResponse._dumps', return_value='{"key": "value"}')
    
    # Call the json function without a custom dumps
    response = json({"key": "value"})
    
    # Assert that the default _dumps method was called
    default_dumps.assert_called_once_with({"key": "value"})
    
    # Assert that the response is an instance of HTTPResponse
    assert isinstance(response, HTTPResponse)
    
    # Assert that the response body is the result of the default _dumps method
    assert response.body == b'{"key": "value"}'
    
    # Assert that the content type is application/json
    assert response.content_type == "application/json"
    
    # Assert that the status code is 200
    assert response.status == 200
