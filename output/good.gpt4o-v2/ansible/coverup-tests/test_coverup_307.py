# file: lib/ansible/galaxy/api.py:462-476
# asked: {"lines": [462, 463, 467, 468, 469, 470, 471, 473, 475, 476], "branches": [[468, 469], [468, 470], [470, 471], [470, 473]]}
# gained: {"lines": [462, 463, 467, 468, 469, 470, 471, 473, 475, 476], "branches": [[468, 469], [468, 470], [470, 471], [470, 473]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(galaxy='galaxy', name='name', url='some_url', available_api_versions={'v1': 'v1'})

def test_get_import_task_with_task_id(galaxy_api):
    with patch.object(galaxy_api, '_call_galaxy', return_value={'results': 'some_data'}) as mock_call:
        result = galaxy_api.get_import_task(task_id=123)
        mock_call.assert_called_once_with('some_url/v1/imports?id=123')
        assert result == 'some_data'

def test_get_import_task_with_github_user_and_repo(galaxy_api):
    with patch.object(galaxy_api, '_call_galaxy', return_value={'results': 'some_data'}) as mock_call:
        result = galaxy_api.get_import_task(github_user='user', github_repo='repo')
        mock_call.assert_called_once_with('some_url/v1/imports?github_user=user&github_repo=repo')
        assert result == 'some_data'

def test_get_import_task_raises_error(galaxy_api):
    with pytest.raises(AnsibleError, match="Expected task_id or github_user and github_repo"):
        galaxy_api.get_import_task()
