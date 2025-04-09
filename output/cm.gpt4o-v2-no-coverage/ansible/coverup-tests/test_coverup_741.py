# file: lib/ansible/galaxy/api.py:320-324
# asked: {"lines": [320, 321, 322, 324], "branches": []}
# gained: {"lines": [320, 321, 322, 324], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(
        galaxy='test_galaxy',
        name='test_name',
        url='https://galaxy.ansible.com',
        username='test_user',
        password='test_pass',
        token='test_token',
        validate_certs=True,
        available_api_versions=None,
        clear_response_cache=False,
        no_cache=True,
        priority=float('inf')
    )

def test_available_api_versions(galaxy_api):
    with patch.object(GalaxyAPI, '_call_galaxy', return_value={'available_versions': {'v1': 'v1/', 'v2': 'v2/', 'v3': 'v3/'}}):
        versions = galaxy_api.available_api_versions
        assert versions == {'v1': 'v1/', 'v2': 'v2/', 'v3': 'v3/'}

def test_available_api_versions_no_versions(galaxy_api):
    with patch.object(GalaxyAPI, '_call_galaxy', return_value={}):
        with pytest.raises(AnsibleError, match="Tried to find galaxy API root at https://galaxy.ansible.com/api/ but no 'available_versions' are available on https://galaxy.ansible.com"):
            _ = galaxy_api.available_api_versions

def test_available_api_versions_no_common_versions(galaxy_api):
    with patch.object(GalaxyAPI, '_call_galaxy', return_value={'available_versions': {'v4': 'v4/'}}):
        with pytest.raises(AnsibleError, match="Galaxy action available_api_versions requires API versions 'v1, v2, v3' but only 'v4' are available on test_name https://galaxy.ansible.com/api/"):
            _ = galaxy_api.available_api_versions
