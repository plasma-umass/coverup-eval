# file: httpie/plugins/builtin.py:13-34
# asked: {"lines": [13, 15, 26, 27, 28, 30, 31, 32, 33, 34], "branches": []}
# gained: {"lines": [13, 15, 26, 27, 28, 30, 31, 32, 33, 34], "branches": []}

import pytest
from base64 import b64encode
from httpie.plugins.builtin import HTTPBasicAuth
from requests import PreparedRequest

@pytest.fixture
def auth_instance():
    return HTTPBasicAuth('testuser', 'testpass')

def test_http_basic_auth_call(auth_instance, monkeypatch):
    request = PreparedRequest()
    request.prepare(
        method='GET',
        url='http://example.com',
    )

    def mock_make_header(username, password):
        return 'mocked_header'

    monkeypatch.setattr(HTTPBasicAuth, 'make_header', mock_make_header)
    modified_request = auth_instance(request)
    
    assert modified_request.headers['Authorization'] == 'mocked_header'.encode('latin1')

def test_http_basic_auth_make_header():
    header = HTTPBasicAuth.make_header('testuser', 'testpass')
    expected_credentials = 'testuser:testpass'
    expected_token = b64encode(expected_credentials.encode('utf8')).strip().decode('latin1')
    expected_header = f'Basic {expected_token}'
    
    assert header == expected_header
