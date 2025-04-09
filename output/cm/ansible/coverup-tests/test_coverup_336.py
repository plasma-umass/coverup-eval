# file lib/ansible/galaxy/api.py:414-424
# lines [414, 416, 417, 419, 420, 421, 423, 424]
# branches ['416->417', '416->419', '419->420', '419->423', '423->exit', '423->424']

import pytest
from ansible.errors import AnsibleError
from ansible.galaxy.api import GalaxyAPI
from ansible.module_utils._text import to_native
from ansible import constants as C
from unittest.mock import MagicMock

@pytest.fixture
def galaxy_api(mocker):
    api = GalaxyAPI(galaxy="test_galaxy", name="test_name", url="http://example.com/api/")
    mocker.patch.object(api, 'token', new_callable=MagicMock)
    return api

def test_add_auth_token_already_present(galaxy_api):
    headers = {'Authorization': 'Bearer already_set_token'}
    url = "http://example.com/api/"
    galaxy_api._add_auth_token(headers, url)
    assert headers == {'Authorization': 'Bearer already_set_token'}

def test_add_auth_token_required_without_token(galaxy_api):
    galaxy_api.token = None
    headers = {}
    url = "http://example.com/api/"
    with pytest.raises(AnsibleError) as excinfo:
        galaxy_api._add_auth_token(headers, url, required=True)
    assert "No access token or username set." in str(excinfo.value)

def test_add_auth_token_with_token(galaxy_api):
    headers = {}
    url = "http://example.com/api/"
    token_headers = {'Authorization': 'Bearer test_token'}
    galaxy_api.token.headers.return_value = token_headers
    galaxy_api._add_auth_token(headers, url)
    assert headers == token_headers
