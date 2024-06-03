# file sanic/response.py:37-43
# lines [37, 38, 42]
# branches []

import pytest
from sanic.response import BaseHTTPResponse
import json

def test_base_http_response_dumps():
    # Create a sample dictionary to test the _dumps method
    sample_dict = {"key": "value"}
    
    # Use the _dumps method to convert the dictionary to a JSON string
    json_str = BaseHTTPResponse._dumps(sample_dict)
    
    # Assert that the output is a valid JSON string
    assert json.loads(json_str) == sample_dict
