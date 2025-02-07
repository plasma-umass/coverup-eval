# file: lib/ansible/module_utils/urls.py:1005-1016
# asked: {"lines": [1005, 1009, 1011, 1012, 1013, 1014, 1015, 1016], "branches": [[1013, 0], [1013, 1014]]}
# gained: {"lines": [1005, 1009, 1011, 1012, 1013, 1014, 1015, 1016], "branches": [[1013, 0], [1013, 1014]]}

import pytest
import re
from ansible.module_utils.urls import SSLValidationHandler, ProxyError

def test_validate_proxy_response_valid_code():
    handler = SSLValidationHandler('hostname', 8080)
    response = b'HTTP/1.1 200 Connection established\r\n'
    handler.validate_proxy_response(response)

def test_validate_proxy_response_invalid_code():
    handler = SSLValidationHandler('hostname', 8080)
    response = b'HTTP/1.1 500 Internal Server Error\r\n'
    with pytest.raises(ProxyError, match='Connection to proxy failed'):
        handler.validate_proxy_response(response)

def test_validate_proxy_response_custom_valid_code():
    handler = SSLValidationHandler('hostname', 8080)
    response = b'HTTP/1.1 201 Created\r\n'
    handler.validate_proxy_response(response, valid_codes=[201])

def test_validate_proxy_response_invalid_format():
    handler = SSLValidationHandler('hostname', 8080)
    response = b'Invalid response format'
    with pytest.raises(ProxyError, match='Connection to proxy failed'):
        handler.validate_proxy_response(response)
