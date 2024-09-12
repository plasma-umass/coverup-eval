# file: lib/ansible/galaxy/api.py:442-460
# asked: {"lines": [442, 443, 447, 448, 449, 450, 451, 453, 454, 455, 456, 457, 458, 459, 460], "branches": [[453, 454], [453, 455], [455, 456], [455, 457], [458, 459], [458, 460]]}
# gained: {"lines": [442, 443, 447, 448, 449, 450, 451, 453, 454, 455, 456, 457, 458, 459, 460], "branches": [[453, 454], [453, 455], [455, 456], [455, 457], [458, 459], [458, 460]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.errors import AnsibleError

# Assuming GalaxyAPI and g_connect are imported from the appropriate module
from ansible.galaxy.api import GalaxyAPI, g_connect

@pytest.fixture
def galaxy_api():
    api = GalaxyAPI(galaxy='test_galaxy', name='test_name', url='https://galaxy.ansible.com')
    api._available_api_versions = {'v1': 'v1/'}
    return api

def test_create_import_task_with_role_name(galaxy_api, monkeypatch):
    def mock_call_galaxy(url, args, method):
        return {'results': 'success'}

    monkeypatch.setattr(galaxy_api, '_call_galaxy', mock_call_galaxy)
    result = galaxy_api.create_import_task('test_user', 'test_repo', role_name='test_role')
    assert result == 'success'

def test_create_import_task_without_role_name(galaxy_api, monkeypatch):
    def mock_call_galaxy(url, args, method):
        return {'results': 'success'}

    monkeypatch.setattr(galaxy_api, '_call_galaxy', mock_call_galaxy)
    result = galaxy_api.create_import_task('test_user', 'ansible-role-test_repo')
    assert result == 'success'

def test_create_import_task_without_role_name_no_prefix(galaxy_api, monkeypatch):
    def mock_call_galaxy(url, args, method):
        return {'results': 'success'}

    monkeypatch.setattr(galaxy_api, '_call_galaxy', mock_call_galaxy)
    result = galaxy_api.create_import_task('test_user', 'test_repo')
    assert result == 'success'

def test_create_import_task_no_results(galaxy_api, monkeypatch):
    def mock_call_galaxy(url, args, method):
        return {}

    monkeypatch.setattr(galaxy_api, '_call_galaxy', mock_call_galaxy)
    result = galaxy_api.create_import_task('test_user', 'test_repo')
    assert result == {}
