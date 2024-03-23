# file httpie/plugins/builtin.py:13-34
# lines [13, 15, 26, 27, 28, 30, 31, 32, 33, 34]
# branches []

import pytest
from httpie.plugins.builtin import HTTPBasicAuth
from requests import PreparedRequest
from base64 import b64encode

def test_http_basic_auth_unicode_credentials(mocker):
    # Mock a PreparedRequest object
    request = mocker.Mock(spec=PreparedRequest)
    request.headers = {}

    # Create an instance of HTTPBasicAuth with unicode credentials
    auth = HTTPBasicAuth('user', 'pässwörd')

    # Call the auth instance with the mocked request
    updated_request = auth(request)

    # Verify that the Authorization header is correctly set
    assert 'Authorization' in updated_request.headers
    credentials = f'user:pässwörd'.encode('utf8')
    expected_auth_value = 'Basic ' + b64encode(credentials).strip().decode('latin1')
    assert updated_request.headers['Authorization'].decode('latin1') == expected_auth_value

    # Clean up by removing the Authorization header
    del updated_request.headers['Authorization']
