# file: lib/ansible/module_utils/urls.py:1005-1016
# asked: {"lines": [1005, 1009, 1011, 1012, 1013, 1014, 1015, 1016], "branches": [[1013, 0], [1013, 1014]]}
# gained: {"lines": [1005, 1009, 1011, 1012, 1013, 1014, 1015, 1016], "branches": [[1013, 0], [1013, 1014]]}

import pytest
import re
from ansible.module_utils.urls import SSLValidationHandler, ProxyError

class MockResponse:
    def __init__(self, response):
        self.response = response

@pytest.fixture
def ssl_validation_handler():
    return SSLValidationHandler('hostname', 8080)

def test_validate_proxy_response_valid_code(ssl_validation_handler):
    response = b'HTTP/1.1 200 Connection established'
    try:
        ssl_validation_handler.validate_proxy_response(response)
    except ProxyError:
        pytest.fail("ProxyError raised unexpectedly!")

def test_validate_proxy_response_invalid_code(ssl_validation_handler):
    response = b'HTTP/1.1 500 Internal Server Error'
    with pytest.raises(ProxyError):
        ssl_validation_handler.validate_proxy_response(response)

def test_validate_proxy_response_custom_valid_code(ssl_validation_handler):
    response = b'HTTP/1.1 201 Created'
    try:
        ssl_validation_handler.validate_proxy_response(response, valid_codes=[201])
    except ProxyError:
        pytest.fail("ProxyError raised unexpectedly!")

def test_validate_proxy_response_malformed_response(ssl_validation_handler):
    response = b'Malformed response'
    with pytest.raises(ProxyError):
        ssl_validation_handler.validate_proxy_response(response)
