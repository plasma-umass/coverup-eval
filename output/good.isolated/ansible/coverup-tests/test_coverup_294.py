# file lib/ansible/galaxy/token.py:66-93
# lines [66, 67, 68, 78, 80, 81, 82, 83, 84, 88, 91, 93]
# branches ['67->68', '67->78']

import json
import pytest
from unittest.mock import MagicMock, patch
from ansible.galaxy.token import KeycloakToken

@pytest.fixture
def keycloak_token():
    with patch('ansible.galaxy.token.open_url') as mock_open_url:
        yield KeycloakToken()

@pytest.fixture
def mock_response():
    mock_resp = MagicMock()
    mock_resp.read.return_value = json.dumps({'access_token': 'test_access_token'}).encode('utf-8')
    return mock_resp

def test_keycloak_token_get(keycloak_token, mock_response):
    with patch('ansible.galaxy.token.open_url', return_value=mock_response) as mock_open_url:
        with patch('ansible.galaxy.token.to_native') as mock_to_native:
            with patch('ansible.galaxy.token.to_text') as mock_to_text:
                mock_to_native.return_value = 'https://auth.example.com'
                mock_to_text.return_value = json.dumps({'access_token': 'test_access_token'})

                token = keycloak_token.get()

                assert token == 'test_access_token'
                mock_open_url.assert_called_once()
                mock_to_native.assert_called_once()
                mock_to_text.assert_called_once()
                assert keycloak_token._token == 'test_access_token', "Token should be cached"
