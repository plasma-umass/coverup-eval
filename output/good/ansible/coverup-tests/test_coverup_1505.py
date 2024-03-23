# file lib/ansible/galaxy/api.py:414-424
# lines []
# branches ['423->exit']

import pytest
from ansible.errors import AnsibleError
from ansible.galaxy.api import GalaxyAPI
from ansible.module_utils._text import to_native
from ansible import constants as C
from unittest.mock import MagicMock

class TestGalaxyAPI:

    @pytest.fixture
    def galaxy_api(self, mocker):
        mocker.patch.object(GalaxyAPI, '__init__', return_value=None)
        api = GalaxyAPI()
        api.token = None
        return api

    def test_add_auth_token_without_token_and_not_required(self, galaxy_api):
        headers = {}
        galaxy_api._add_auth_token(headers=headers, url='http://example.com', required=False)
        assert headers == {}

    def test_add_auth_token_with_required_token(self, galaxy_api):
        with pytest.raises(AnsibleError) as excinfo:
            galaxy_api._add_auth_token(headers={}, url='http://example.com', required=True)
        assert "No access token or username set." in str(excinfo.value)
        assert to_native(C.GALAXY_TOKEN_PATH) in str(excinfo.value)

    def test_add_auth_token_with_existing_authorization(self, galaxy_api):
        headers = {'Authorization': 'Bearer existing_token'}
        galaxy_api._add_auth_token(headers=headers, url='http://example.com')
        assert headers == {'Authorization': 'Bearer existing_token'}

    def test_add_auth_token_with_token(self, galaxy_api):
        galaxy_api.token = MagicMock()
        galaxy_api.token.headers.return_value = {'Authorization': 'Bearer new_token'}
        headers = {}
        galaxy_api._add_auth_token(headers=headers, url='http://example.com')
        assert headers == {'Authorization': 'Bearer new_token'}
