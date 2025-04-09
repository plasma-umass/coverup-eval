# file lib/ansible/module_utils/urls.py:1005-1016
# lines [1005, 1009, 1011, 1012, 1013, 1014, 1015, 1016]
# branches ['1013->exit', '1013->1014']

import pytest
import re
from unittest.mock import patch, Mock
from ansible.module_utils.urls import SSLValidationHandler, ProxyError

class MockSSLValidationHandler(SSLValidationHandler):
    def __init__(self):
        pass

def test_validate_proxy_response_valid_code():
    handler = MockSSLValidationHandler()
    response = b'HTTP/1.1 200 OK'
    try:
        handler.validate_proxy_response(response)
    except ProxyError:
        pytest.fail("ProxyError raised unexpectedly!")

def test_validate_proxy_response_invalid_code():
    handler = MockSSLValidationHandler()
    response = b'HTTP/1.1 404 Not Found'
    with pytest.raises(ProxyError):
        handler.validate_proxy_response(response)

def test_validate_proxy_response_custom_valid_code():
    handler = MockSSLValidationHandler()
    response = b'HTTP/1.1 201 Created'
    try:
        handler.validate_proxy_response(response, valid_codes=[201])
    except ProxyError:
        pytest.fail("ProxyError raised unexpectedly!")

def test_validate_proxy_response_invalid_format():
    handler = MockSSLValidationHandler()
    response = b'Invalid Response'
    with pytest.raises(ProxyError):
        handler.validate_proxy_response(response)
