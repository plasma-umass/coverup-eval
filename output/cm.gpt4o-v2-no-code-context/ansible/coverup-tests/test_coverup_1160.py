# file: lib/ansible/galaxy/api.py:414-424
# asked: {"lines": [416, 417, 419, 420, 421, 423, 424], "branches": [[416, 417], [416, 419], [419, 420], [419, 423], [423, 0], [423, 424]]}
# gained: {"lines": [416, 417, 419, 420, 421, 423, 424], "branches": [[416, 417], [416, 419], [419, 420], [419, 423], [423, 424]]}

import pytest
from ansible.errors import AnsibleError
from ansible.galaxy.api import GalaxyAPI

class MockToken:
    def headers(self):
        return {'Authorization': 'Bearer mocktoken'}

@pytest.fixture
def galaxy_api():
    api = GalaxyAPI(galaxy='mock_galaxy', name='mock_name', url='http://example.com')
    api.token = MockToken()
    return api

def test_add_auth_token_already_present(galaxy_api):
    headers = {'Authorization': 'Bearer existingtoken'}
    url = 'http://example.com'
    galaxy_api._add_auth_token(headers, url)
    assert headers['Authorization'] == 'Bearer existingtoken'

def test_add_auth_token_required_no_token(galaxy_api, monkeypatch):
    headers = {}
    url = 'http://example.com'
    monkeypatch.setattr(galaxy_api, 'token', None)
    with pytest.raises(AnsibleError, match="No access token or username set. A token can be set with --api-key"):
        galaxy_api._add_auth_token(headers, url, required=True)

def test_add_auth_token_with_token(galaxy_api):
    headers = {}
    url = 'http://example.com'
    galaxy_api._add_auth_token(headers, url)
    assert headers['Authorization'] == 'Bearer mocktoken'
