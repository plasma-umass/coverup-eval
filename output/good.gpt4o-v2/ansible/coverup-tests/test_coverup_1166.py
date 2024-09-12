# file: lib/ansible/galaxy/api.py:184-221
# asked: {"lines": [204, 205, 206, 208, 209, 210, 211, 212, 213, 215], "branches": [[203, 204], [205, 206], [205, 208], [209, 210], [209, 215]]}
# gained: {"lines": [204, 205, 206, 208, 209, 210, 211, 212, 213, 215], "branches": [[203, 204], [205, 206], [205, 208], [209, 210], [209, 215]]}

import pytest
import json
from unittest.mock import Mock
from ansible.module_utils._text import to_native
from ansible.galaxy.api import GalaxyError

def test_galaxy_error_v3_with_errors():
    http_error = Mock()
    http_error.code = 404
    http_error.geturl.return_value = 'http://example.com/api/v3/some_endpoint'
    http_error.reason = 'Not Found'
    http_error.read.return_value = json.dumps({
        'errors': [
            {'detail': 'Not Found', 'code': '404'}
        ]
    }).encode('utf-8')
    message = "An error occurred"

    error = GalaxyError(http_error, message)

    assert error.http_code == 404
    assert error.url == 'http://example.com/api/v3/some_endpoint'
    assert error.message == to_native("An error occurred (HTTP Code: 404, Message: Not Found Code: 404)")

def test_galaxy_error_v3_without_errors():
    http_error = Mock()
    http_error.code = 500
    http_error.geturl.return_value = 'http://example.com/api/v3/some_endpoint'
    http_error.reason = 'Internal Server Error'
    http_error.read.return_value = json.dumps({}).encode('utf-8')
    message = "An error occurred"

    error = GalaxyError(http_error, message)

    assert error.http_code == 500
    assert error.url == 'http://example.com/api/v3/some_endpoint'
    assert error.message == to_native("An error occurred (HTTP Code: 500, Message: Internal Server Error Code: Unknown)")
