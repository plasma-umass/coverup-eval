# file lib/ansible/galaxy/api.py:184-221
# lines [184, 185, 187, 188, 189, 190, 192, 193, 194, 195, 196, 198, 199, 200, 201, 202, 203, 204, 205, 206, 208, 209, 210, 211, 212, 213, 215, 218, 219, 221]
# branches ['199->200', '199->203', '203->204', '203->218', '205->206', '205->208', '209->210', '209->215']

import json
import pytest
from ansible.galaxy.api import GalaxyError
from ansible.module_utils._text import to_native, to_text
from unittest.mock import MagicMock

@pytest.fixture
def http_error_mock():
    mock = MagicMock()
    mock.code = 404
    mock.geturl.return_value = 'https://galaxy.ansible.com/api/v2/collections/namespace/name/versions'
    mock.reason = 'Not Found'
    mock.read.return_value = json.dumps({
        "message": "Not found.",
        "code": "not_found"
    }).encode('utf-8')
    return mock

def test_galaxy_error_v2(http_error_mock):
    message = "Error while retrieving collection"
    error = GalaxyError(http_error_mock, message)
    
    assert error.http_code == 404
    assert error.url == 'https://galaxy.ansible.com/api/v2/collections/namespace/name/versions'
    assert "Error while retrieving collection (HTTP Code: 404, Message: Not found. Code: not_found)" in error.message

@pytest.fixture
def http_error_mock_v3():
    mock = MagicMock()
    mock.code = 500
    mock.geturl.return_value = 'https://galaxy.ansible.com/api/v3/collections/namespace/name/versions'
    mock.reason = 'Internal Server Error'
    mock.read.return_value = json.dumps({
        "errors": [
            {"detail": "Server error.", "code": "server_error"}
        ]
    }).encode('utf-8')
    return mock

def test_galaxy_error_v3(http_error_mock_v3):
    message = "Error while retrieving collection"
    error = GalaxyError(http_error_mock_v3, message)
    
    assert error.http_code == 500
    assert error.url == 'https://galaxy.ansible.com/api/v3/collections/namespace/name/versions'
    assert "Error while retrieving collection (HTTP Code: 500, Message: Server error. Code: server_error)" in error.message

@pytest.fixture
def http_error_mock_v1():
    mock = MagicMock()
    mock.code = 400
    mock.geturl.return_value = 'https://galaxy.ansible.com/api/v1/collections/namespace/name/versions'
    mock.reason = 'Bad Request'
    mock.read.return_value = json.dumps({
        "default": "Invalid request."
    }).encode('utf-8')
    return mock

def test_galaxy_error_v1(http_error_mock_v1):
    message = "Error while retrieving collection"
    error = GalaxyError(http_error_mock_v1, message)
    
    assert error.http_code == 400
    assert error.url == 'https://galaxy.ansible.com/api/v1/collections/namespace/name/versions'
    assert "Error while retrieving collection (HTTP Code: 400, Message: Invalid request.)" in error.message
