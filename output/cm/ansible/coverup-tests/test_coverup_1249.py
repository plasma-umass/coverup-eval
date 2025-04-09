# file lib/ansible/galaxy/api.py:462-476
# lines [467, 468, 469, 470, 471, 473, 475, 476]
# branches ['468->469', '468->470', '470->471', '470->473']

import pytest
from ansible.errors import AnsibleError
from ansible.galaxy.api import GalaxyAPI
from unittest.mock import MagicMock

# Assuming _urljoin, _call_galaxy, and g_connect are defined elsewhere in the module
# and need to be mocked for testing purposes.

@pytest.fixture
def galaxy_api(mocker):
    api = GalaxyAPI("server", "username", "password")
    mocker.patch.object(api, '_call_galaxy', return_value={'results': 'data'})
    mocker.patch.object(api, '_available_api_versions', {'v1': 'api/v1/'})
    return api

def test_get_import_task_with_task_id(galaxy_api):
    task_id = 123
    data = galaxy_api.get_import_task(task_id=task_id)
    assert data == 'data'
    galaxy_api._call_galaxy.assert_called_once()

def test_get_import_task_with_github_user_and_repo(galaxy_api):
    github_user = 'user'
    github_repo = 'repo'
    data = galaxy_api.get_import_task(github_user=github_user, github_repo=github_repo)
    assert data == 'data'
    galaxy_api._call_galaxy.assert_called_once()

def test_get_import_task_without_required_args(galaxy_api):
    with pytest.raises(AnsibleError):
        galaxy_api.get_import_task()
