# file lib/ansible/module_utils/urls.py:1005-1016
# lines [1005, 1009, 1011, 1012, 1013, 1014, 1015, 1016]
# branches ['1013->exit', '1013->1014']

import pytest
from ansible.module_utils.urls import SSLValidationHandler, ProxyError
from unittest.mock import MagicMock

# Define a test function to cover the missing lines/branches
def test_validate_proxy_response():
    # Create a mock for the SSLValidationHandler with the required arguments
    handler = SSLValidationHandler(MagicMock(), MagicMock())

    # Test with a valid response code
    valid_response = b'HTTP/1.1 200 OK'
    handler.validate_proxy_response(valid_response)  # Should not raise an exception

    # Test with an invalid response code
    invalid_response = b'HTTP/1.1 500 Internal Server Error'
    with pytest.raises(ProxyError) as exc_info:
        handler.validate_proxy_response(invalid_response)
    assert 'Connection to proxy failed' in str(exc_info.value)

    # Test with a non-matching response
    non_matching_response = b'INVALID RESPONSE'
    with pytest.raises(ProxyError) as exc_info:
        handler.validate_proxy_response(non_matching_response)
    assert 'Connection to proxy failed' in str(exc_info.value)

    # Test with a custom valid code
    custom_valid_response = b'HTTP/1.1 201 Created'
    handler.validate_proxy_response(custom_valid_response, valid_codes=[201])  # Should not raise an exception

# Run the test function without patching
def test_suite():
    test_validate_proxy_response()
