# file sanic/response.py:239-248
# lines [239, 240, 248]
# branches []

import pytest
from sanic.response import HTTPResponse

# Assuming the sanic.response.empty function is as provided in the question
from sanic.response import empty

def test_empty_response():
    # Test the default status code
    response = empty()
    assert response.status == 204
    assert response.body == b""
    assert response.headers == {}

    # Test with a custom status code and headers
    custom_status = 202
    custom_headers = {"X-Custom-Header": "Value"}
    response_with_custom = empty(status=custom_status, headers=custom_headers)
    assert response_with_custom.status == custom_status
    assert response_with_custom.body == b""
    assert response_with_custom.headers == custom_headers

# The test does not require any cleanup as it does not modify any global state
# or external resources. No need for pytest-mock or any other cleanup mechanism.
