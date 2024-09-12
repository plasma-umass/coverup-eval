# file: lib/ansible/galaxy/api.py:414-424
# asked: {"lines": [414, 416, 417, 419, 420, 421, 423, 424], "branches": [[416, 417], [416, 419], [419, 420], [419, 423], [423, 0], [423, 424]]}
# gained: {"lines": [414, 416, 417, 419, 420, 421, 423, 424], "branches": [[416, 417], [416, 419], [419, 420], [419, 423], [423, 424]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible import constants as C
from unittest.mock import MagicMock, patch

class TestGalaxyAPI:
    
    @pytest.fixture
    def galaxy_api(self):
        from ansible.galaxy.api import GalaxyAPI
        return GalaxyAPI(galaxy=None, name="test", url="http://test.url", token=MagicMock())

    def test_add_auth_token_with_authorization_header(self, galaxy_api):
        headers = {'Authorization': 'Bearer existing_token'}
        url = "http://test.url"
        galaxy_api._add_auth_token(headers, url)
        assert headers['Authorization'] == 'Bearer existing_token'

    def test_add_auth_token_without_token_and_required(self, galaxy_api):
        headers = {}
        url = "http://test.url"
        galaxy_api.token = None
        with pytest.raises(AnsibleError, match="No access token or username set. A token can be set with --api-key or at"):
            galaxy_api._add_auth_token(headers, url, required=True)

    def test_add_auth_token_with_token(self, galaxy_api):
        headers = {}
        url = "http://test.url"
        token_headers = {'Authorization': 'Bearer new_token'}
        galaxy_api.token.headers = MagicMock(return_value=token_headers)
        galaxy_api._add_auth_token(headers, url)
        assert headers['Authorization'] == 'Bearer new_token'
