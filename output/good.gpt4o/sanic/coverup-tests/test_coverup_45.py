# file sanic/response.py:37-43
# lines [37, 38, 42]
# branches []

import pytest
from sanic.response import BaseHTTPResponse
from sanic.response import json_dumps

def test_base_http_response_dumps():
    # Ensure that the _dumps attribute is correctly set to json_dumps
    assert BaseHTTPResponse._dumps is json_dumps
