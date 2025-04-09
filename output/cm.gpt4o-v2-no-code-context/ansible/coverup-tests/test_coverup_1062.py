# file: lib/ansible/galaxy/api.py:184-221
# asked: {"lines": [195, 196], "branches": []}
# gained: {"lines": [195, 196], "branches": []}

import pytest
import json
from unittest.mock import Mock, patch

# Assuming the GalaxyError class is imported from ansible/galaxy/api.py
from ansible.galaxy.api import GalaxyError

def test_galaxy_error_attribute_error():
    http_error_mock = Mock()
    http_error_mock.code = 500
    http_error_mock.geturl.return_value = 'http://example.com/v2'
    http_error_mock.read.side_effect = AttributeError
    http_error_mock.reason = "Internal Server Error"

    error_message = "An error occurred"
    error = GalaxyError(http_error_mock, error_message)

    assert error.http_code == 500
    assert error.url == 'http://example.com/v2'
    assert error.message == "An error occurred (HTTP Code: 500, Message: Internal Server Error Code: Unknown)"

def test_galaxy_error_value_error():
    http_error_mock = Mock()
    http_error_mock.code = 500
    http_error_mock.geturl.return_value = 'http://example.com/v2'
    http_error_mock.read.return_value = 'invalid json'
    http_error_mock.reason = "Internal Server Error"

    error_message = "An error occurred"
    error = GalaxyError(http_error_mock, error_message)

    assert error.http_code == 500
    assert error.url == 'http://example.com/v2'
    assert error.message == "An error occurred (HTTP Code: 500, Message: Internal Server Error Code: Unknown)"
