# file lib/ansible/galaxy/api.py:184-221
# lines [195, 196]
# branches []

import pytest
from unittest import mock
import json
from ansible.galaxy.api import GalaxyError
from ansible.errors import AnsibleError

def test_galaxy_error_attribute_value_error(mocker):
    # Mocking the http_error object
    http_error_mock = mock.Mock()
    http_error_mock.code = 500
    http_error_mock.geturl.return_value = 'http://example.com/v2/some_endpoint'
    http_error_mock.read.side_effect = AttributeError("Mocked attribute error")
    http_error_mock.reason = "Mocked reason"

    # Test GalaxyError with AttributeError
    error_message = "Test error message"
    galaxy_error = GalaxyError(http_error_mock, error_message)
    
    assert galaxy_error.http_code == 500
    assert galaxy_error.url == 'http://example.com/v2/some_endpoint'
    assert galaxy_error.message == "Test error message (HTTP Code: 500, Message: Mocked reason Code: Unknown)"

    # Mocking the http_error object for ValueError
    http_error_mock.read.side_effect = lambda: b'Invalid JSON'

    # Test GalaxyError with ValueError
    galaxy_error = GalaxyError(http_error_mock, error_message)
    
    assert galaxy_error.http_code == 500
    assert galaxy_error.url == 'http://example.com/v2/some_endpoint'
    assert galaxy_error.message == "Test error message (HTTP Code: 500, Message: Mocked reason Code: Unknown)"
