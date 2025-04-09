# file: lib/ansible/galaxy/api.py:462-476
# asked: {"lines": [462, 463, 467, 468, 469, 470, 471, 473, 475, 476], "branches": [[468, 469], [468, 470], [470, 471], [470, 473]]}
# gained: {"lines": [462, 463, 467, 468, 469, 470, 471, 473, 475, 476], "branches": [[468, 469], [468, 470], [470, 471], [470, 473]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    api_versions = {'v1': 'v1/'}
    return GalaxyAPI(galaxy='mock_galaxy', name='mock_name', url='http://mockserver', available_api_versions=api_versions)

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
@patch('ansible.galaxy.api._urljoin', return_value='http://mockserver/api/v1/imports')
def test_get_import_task_with_task_id(mock_urljoin, mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'results': 'mock_results'}
    result = galaxy_api.get_import_task(task_id=123)
    mock_urljoin.assert_called_once_with(galaxy_api.api_server, galaxy_api.available_api_versions['v1'], 'imports')
    mock_call_galaxy.assert_called_once_with('http://mockserver/api/v1/imports?id=123')
    assert result == 'mock_results'

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
@patch('ansible.galaxy.api._urljoin', return_value='http://mockserver/api/v1/imports')
def test_get_import_task_with_github_user_and_repo(mock_urljoin, mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'results': 'mock_results'}
    result = galaxy_api.get_import_task(github_user='testuser', github_repo='testrepo')
    mock_urljoin.assert_called_once_with(galaxy_api.api_server, galaxy_api.available_api_versions['v1'], 'imports')
    mock_call_galaxy.assert_called_once_with('http://mockserver/api/v1/imports?github_user=testuser&github_repo=testrepo')
    assert result == 'mock_results'

def test_get_import_task_with_no_params(galaxy_api):
    with pytest.raises(AnsibleError, match="Expected task_id or github_user and github_repo"):
        galaxy_api.get_import_task()
