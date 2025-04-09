# file: lib/ansible/galaxy/api.py:184-221
# asked: {"lines": [184, 185, 187, 188, 189, 190, 192, 193, 194, 195, 196, 198, 199, 200, 201, 202, 203, 204, 205, 206, 208, 209, 210, 211, 212, 213, 215, 218, 219, 221], "branches": [[199, 200], [199, 203], [203, 204], [203, 218], [205, 206], [205, 208], [209, 210], [209, 215]]}
# gained: {"lines": [184, 185, 187, 188, 189, 190, 192, 193, 194, 198, 199, 200, 201, 202, 203, 204, 205, 206, 208, 209, 210, 211, 212, 213, 215, 218, 219, 221], "branches": [[199, 200], [199, 203], [203, 204], [203, 218], [205, 206], [205, 208], [209, 210], [209, 215]]}

import pytest
import json
from unittest.mock import Mock, patch
from ansible.errors import AnsibleError
from ansible.utils.display import Display

# Assuming the GalaxyError class is defined in ansible/galaxy/api.py
from ansible.galaxy.api import GalaxyError

def test_galaxy_error_v2(monkeypatch):
    http_error = Mock()
    http_error.code = 404
    http_error.geturl.return_value = 'http://example.com/v2/some_endpoint'
    http_error.read.return_value = json.dumps({'message': 'Not Found', 'code': '404'})
    http_error.reason = 'Not Found'

    error_message = "An error occurred"
    error = GalaxyError(http_error, error_message)

    assert error.http_code == 404
    assert error.url == 'http://example.com/v2/some_endpoint'
    assert error.message == "An error occurred (HTTP Code: 404, Message: Not Found Code: 404)"

def test_galaxy_error_v3_with_errors(monkeypatch):
    http_error = Mock()
    http_error.code = 400
    http_error.geturl.return_value = 'http://example.com/v3/some_endpoint'
    http_error.read.return_value = json.dumps({'errors': [{'detail': 'Invalid request', 'code': '400'}]})
    http_error.reason = 'Invalid request'

    error_message = "An error occurred"
    error = GalaxyError(http_error, error_message)

    assert error.http_code == 400
    assert error.url == 'http://example.com/v3/some_endpoint'
    assert error.message == "An error occurred (HTTP Code: 400, Message: Invalid request Code: 400)"

def test_galaxy_error_v3_without_errors(monkeypatch):
    http_error = Mock()
    http_error.code = 400
    http_error.geturl.return_value = 'http://example.com/v3/some_endpoint'
    http_error.read.return_value = json.dumps({})
    http_error.reason = 'Bad Request'

    error_message = "An error occurred"
    error = GalaxyError(http_error, error_message)

    assert error.http_code == 400
    assert error.url == 'http://example.com/v3/some_endpoint'
    assert error.message == "An error occurred (HTTP Code: 400, Message: Bad Request Code: Unknown)"

def test_galaxy_error_v1_or_unknown(monkeypatch):
    http_error = Mock()
    http_error.code = 500
    http_error.geturl.return_value = 'http://example.com/v1/some_endpoint'
    http_error.read.return_value = json.dumps({'default': 'Server error'})
    http_error.reason = 'Server error'

    error_message = "An error occurred"
    error = GalaxyError(http_error, error_message)

    assert error.http_code == 500
    assert error.url == 'http://example.com/v1/some_endpoint'
    assert error.message == "An error occurred (HTTP Code: 500, Message: Server error)"

def test_galaxy_error_v1_or_unknown_no_default(monkeypatch):
    http_error = Mock()
    http_error.code = 500
    http_error.geturl.return_value = 'http://example.com/v1/some_endpoint'
    http_error.read.return_value = json.dumps({})
    http_error.reason = 'Internal Server Error'

    error_message = "An error occurred"
    error = GalaxyError(http_error, error_message)

    assert error.http_code == 500
    assert error.url == 'http://example.com/v1/some_endpoint'
    assert error.message == "An error occurred (HTTP Code: 500, Message: Internal Server Error)"
