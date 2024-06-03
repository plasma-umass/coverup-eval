# file lib/ansible/galaxy/api.py:184-221
# lines [184, 185, 187, 188, 189, 190, 192, 193, 194, 195, 196, 198, 199, 200, 201, 202, 203, 204, 205, 206, 208, 209, 210, 211, 212, 213, 215, 218, 219, 221]
# branches ['199->200', '199->203', '203->204', '203->218', '205->206', '205->208', '209->210', '209->215']

import pytest
import json
from unittest.mock import Mock, patch
from ansible.errors import AnsibleError
from ansible.galaxy.api import GalaxyError
from ansible.module_utils._text import to_text, to_native

def test_galaxy_error_v2(mocker):
    http_error = Mock()
    http_error.code = 404
    http_error.geturl.return_value = 'http://example.com/api/v2/some_endpoint'
    http_error.read.return_value = json.dumps({'message': 'Not Found', 'code': '404'})
    http_error.reason = 'Not Found'

    error = GalaxyError(http_error, 'Test message')
    
    assert error.http_code == 404
    assert error.url == 'http://example.com/api/v2/some_endpoint'
    assert error.message == 'Test message (HTTP Code: 404, Message: Not Found Code: 404)'

def test_galaxy_error_v3(mocker):
    http_error = Mock()
    http_error.code = 500
    http_error.geturl.return_value = 'http://example.com/api/v3/some_endpoint'
    http_error.read.return_value = json.dumps({'errors': [{'detail': 'Internal Server Error', 'code': '500'}]})
    http_error.reason = 'Internal Server Error'

    error = GalaxyError(http_error, 'Test message')
    
    assert error.http_code == 500
    assert error.url == 'http://example.com/api/v3/some_endpoint'
    assert error.message == 'Test message (HTTP Code: 500, Message: Internal Server Error Code: 500)'

def test_galaxy_error_v1(mocker):
    http_error = Mock()
    http_error.code = 400
    http_error.geturl.return_value = 'http://example.com/api/v1/some_endpoint'
    http_error.read.return_value = json.dumps({'default': 'Bad Request'})
    http_error.reason = 'Bad Request'

    error = GalaxyError(http_error, 'Test message')
    
    assert error.http_code == 400
    assert error.url == 'http://example.com/api/v1/some_endpoint'
    assert error.message == 'Test message (HTTP Code: 400, Message: Bad Request)'

def test_galaxy_error_unknown_api(mocker):
    http_error = Mock()
    http_error.code = 403
    http_error.geturl.return_value = 'http://example.com/api/unknown/some_endpoint'
    http_error.read.return_value = json.dumps({'default': 'Forbidden'})
    http_error.reason = 'Forbidden'

    error = GalaxyError(http_error, 'Test message')
    
    assert error.http_code == 403
    assert error.url == 'http://example.com/api/unknown/some_endpoint'
    assert error.message == 'Test message (HTTP Code: 403, Message: Forbidden)'

def test_galaxy_error_v3_no_errors(mocker):
    http_error = Mock()
    http_error.code = 500
    http_error.geturl.return_value = 'http://example.com/api/v3/some_endpoint'
    http_error.read.return_value = json.dumps({})
    http_error.reason = 'Internal Server Error'

    error = GalaxyError(http_error, 'Test message')
    
    assert error.http_code == 500
    assert error.url == 'http://example.com/api/v3/some_endpoint'
    assert error.message == 'Test message (HTTP Code: 500, Message: Internal Server Error Code: Unknown)'
