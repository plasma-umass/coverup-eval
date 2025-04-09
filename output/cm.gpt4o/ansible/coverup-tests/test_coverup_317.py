# file lib/ansible/galaxy/api.py:462-476
# lines [462, 463, 467, 468, 469, 470, 471, 473, 475, 476]
# branches ['468->469', '468->470', '470->471', '470->473']

import pytest
from unittest import mock
from ansible.errors import AnsibleError
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    api = GalaxyAPI(galaxy='galaxy', name='name', url='http://example.com')
    api.api_server = 'http://example.com'
    api._available_api_versions = {'v1': 'v1'}
    return api

def test_get_import_task_with_task_id(galaxy_api, mocker):
    mocker.patch.object(galaxy_api, '_call_galaxy', return_value={'results': 'some_data'})
    
    result = galaxy_api.get_import_task(task_id=123)
    
    assert result == 'some_data'
    galaxy_api._call_galaxy.assert_called_once_with('http://example.com/v1/imports?id=123')

def test_get_import_task_with_github_user_and_repo(galaxy_api, mocker):
    mocker.patch.object(galaxy_api, '_call_galaxy', return_value={'results': 'some_data'})
    
    result = galaxy_api.get_import_task(github_user='user', github_repo='repo')
    
    assert result == 'some_data'
    galaxy_api._call_galaxy.assert_called_once_with('http://example.com/v1/imports?github_user=user&github_repo=repo')

def test_get_import_task_raises_error(galaxy_api):
    with pytest.raises(AnsibleError, match="Expected task_id or github_user and github_repo"):
        galaxy_api.get_import_task()
