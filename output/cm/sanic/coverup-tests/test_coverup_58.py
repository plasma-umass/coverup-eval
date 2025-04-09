# file sanic/response.py:37-43
# lines [37, 38, 42]
# branches []

import pytest
from sanic.response import BaseHTTPResponse
from unittest.mock import Mock
import json

# Test function to cover the _dumps attribute
def test_base_http_response_dumps():
    # Setup a mock for json.dumps
    mock_dumps = Mock(return_value='{"key": "value"}')
    original_dumps = BaseHTTPResponse._dumps
    BaseHTTPResponse._dumps = mock_dumps

    # Create an instance of BaseHTTPResponse and use the _dumps method
    response = BaseHTTPResponse()
    result = response._dumps({"key": "value"})

    # Assertions to verify the postconditions
    mock_dumps.assert_called_once_with({"key": "value"})
    assert result == '{"key": "value"}'

    # Cleanup: Restore the original _dumps method
    BaseHTTPResponse._dumps = original_dumps
