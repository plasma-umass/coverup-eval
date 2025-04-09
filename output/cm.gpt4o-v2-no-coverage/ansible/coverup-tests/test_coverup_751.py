# file: lib/ansible/galaxy/token.py:95-98
# asked: {"lines": [95, 96, 97, 98], "branches": []}
# gained: {"lines": [95, 96, 97, 98], "branches": []}

import pytest
from unittest.mock import patch, Mock
from ansible.galaxy.token import KeycloakToken

@pytest.fixture
def mock_open_url():
    with patch('ansible.galaxy.token.open_url') as mock:
        yield mock

@pytest.fixture
def mock_user_agent():
    with patch('ansible.galaxy.token.user_agent', return_value='test-agent'):
        yield

@pytest.fixture
def mock_to_native():
    with patch('ansible.galaxy.token.to_native', side_effect=lambda x: x):
        yield

@pytest.fixture
def mock_to_text():
    with patch('ansible.galaxy.token.to_text', side_effect=lambda x, errors: x):
        yield

def test_keycloak_token_headers(mock_open_url, mock_user_agent, mock_to_native, mock_to_text):
    # Mock the response of open_url
    mock_response = Mock()
    mock_response.read.return_value = '{"access_token": "test_token"}'
    mock_open_url.return_value = mock_response

    # Initialize KeycloakToken with test data
    token = KeycloakToken(access_token='initial_token', auth_url='http://test.url', client_id='test_client')

    # Call headers method and verify the result
    headers = token.headers()
    assert headers['Authorization'] == 'Bearer test_token'

    # Clean up
    del token
