# file: lib/ansible/galaxy/api.py:414-424
# asked: {"lines": [], "branches": [[423, 0]]}
# gained: {"lines": [], "branches": [[423, 0]]}

import pytest
from unittest.mock import MagicMock
from ansible.errors import AnsibleError
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(galaxy='test_galaxy', name='test_name', url='http://test_url', token=None)

def test_add_auth_token_with_existing_authorization_header(galaxy_api):
    headers = {'Authorization': 'Bearer existing_token'}
    url = 'http://test_url'
    galaxy_api._add_auth_token(headers, url)
    assert headers['Authorization'] == 'Bearer existing_token'

def test_add_auth_token_with_required_but_no_token(galaxy_api):
    headers = {}
    url = 'http://test_url'
    with pytest.raises(AnsibleError, match="No access token or username set. A token can be set with --api-key or at"):
        galaxy_api._add_auth_token(headers, url, required=True)

def test_add_auth_token_with_token(galaxy_api):
    headers = {}
    url = 'http://test_url'
    mock_token = MagicMock()
    mock_token.headers.return_value = {'Authorization': 'Bearer new_token'}
    galaxy_api.token = mock_token
    galaxy_api._add_auth_token(headers, url)
    assert headers['Authorization'] == 'Bearer new_token'

def test_add_auth_token_without_required_and_no_token(galaxy_api):
    headers = {}
    url = 'http://test_url'
    galaxy_api._add_auth_token(headers, url)
    assert 'Authorization' not in headers
