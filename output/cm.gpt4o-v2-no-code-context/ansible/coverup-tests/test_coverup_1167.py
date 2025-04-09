# file: lib/ansible/galaxy/api.py:462-476
# asked: {"lines": [467, 468, 469, 470, 471, 473, 475, 476], "branches": [[468, 469], [468, 470], [470, 471], [470, 473]]}
# gained: {"lines": [467, 468, 469, 470, 471, 473, 475, 476], "branches": [[468, 469], [468, 470], [470, 471], [470, 473]]}

import pytest
from unittest.mock import patch, Mock
from ansible.errors import AnsibleError
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api(mocker):
    mocker.patch('ansible.galaxy.api.GalaxyAPI.__init__', return_value=None)
    api_instance = GalaxyAPI()
    api_instance.api_server = 'http://example.com'
    api_instance._available_api_versions = {'v1': 'v1'}
    return api_instance

def test_get_import_task_with_task_id(galaxy_api, mocker):
    mock_call_galaxy = mocker.patch.object(galaxy_api, '_call_galaxy', return_value={'results': 'some_data'})

    result = galaxy_api.get_import_task(task_id=123)

    mock_call_galaxy.assert_called_once_with('http://example.com/v1/imports?id=123')
    assert result == 'some_data'

def test_get_import_task_with_github_user_and_repo(galaxy_api, mocker):
    mock_call_galaxy = mocker.patch.object(galaxy_api, '_call_galaxy', return_value={'results': 'some_data'})

    result = galaxy_api.get_import_task(github_user='user', github_repo='repo')

    mock_call_galaxy.assert_called_once_with('http://example.com/v1/imports?github_user=user&github_repo=repo')
    assert result == 'some_data'

def test_get_import_task_raises_error(galaxy_api, mocker):
    with pytest.raises(AnsibleError, match="Expected task_id or github_user and github_repo"):
        galaxy_api.get_import_task()
