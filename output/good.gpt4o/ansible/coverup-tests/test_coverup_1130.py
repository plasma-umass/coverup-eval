# file lib/ansible/galaxy/api.py:414-424
# lines [416, 417, 419, 420, 421, 423, 424]
# branches ['416->417', '416->419', '419->420', '419->423', '423->exit', '423->424']

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError

# Assuming the GalaxyAPI class is imported from ansible.galaxy.api
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(galaxy='test_galaxy', name='test_name', url='http://example.com')

def test_add_auth_token_with_authorization_header(galaxy_api):
    headers = {'Authorization': 'Bearer existing_token'}
    url = 'http://example.com'
    galaxy_api._add_auth_token(headers, url)
    assert headers['Authorization'] == 'Bearer existing_token'

def test_add_auth_token_no_token_required(galaxy_api):
    headers = {}
    url = 'http://example.com'
    galaxy_api.token = None
    galaxy_api._add_auth_token(headers, url, required=False)
    assert 'Authorization' not in headers

def test_add_auth_token_no_token_required_with_token(galaxy_api):
    headers = {}
    url = 'http://example.com'
    mock_token = MagicMock()
    mock_token.headers.return_value = {'Authorization': 'Bearer new_token'}
    galaxy_api.token = mock_token
    galaxy_api._add_auth_token(headers, url, required=False)
    assert headers['Authorization'] == 'Bearer new_token'

def test_add_auth_token_required_no_token(galaxy_api):
    headers = {}
    url = 'http://example.com'
    galaxy_api.token = None
    with pytest.raises(AnsibleError, match="No access token or username set. A token can be set with --api-key or at"):
        galaxy_api._add_auth_token(headers, url, required=True)

def test_add_auth_token_required_with_token(galaxy_api):
    headers = {}
    url = 'http://example.com'
    mock_token = MagicMock()
    mock_token.headers.return_value = {'Authorization': 'Bearer new_token'}
    galaxy_api.token = mock_token
    galaxy_api._add_auth_token(headers, url, required=True)
    assert headers['Authorization'] == 'Bearer new_token'
