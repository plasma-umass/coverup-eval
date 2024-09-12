# file: lib/ansible/galaxy/api.py:609-614
# asked: {"lines": [609, 610, 611, 612, 613, 614], "branches": []}
# gained: {"lines": [609, 610, 611, 612, 613, 614], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(galaxy='test_galaxy', name='test_name', url='https://test.url', available_api_versions={'v1': 'v1/'})

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
@patch('ansible.galaxy.api._urljoin')
def test_delete_role(mock_urljoin, mock_call_galaxy, galaxy_api):
    github_user = 'test_user'
    github_repo = 'test_repo'
    mock_urljoin.return_value = 'mocked_url'
    mock_call_galaxy.return_value = {'status': 'success'}

    result = galaxy_api.delete_role(github_user, github_repo)

    mock_urljoin.assert_called_once_with(galaxy_api.api_server, galaxy_api._available_api_versions['v1'], "removerole", "?github_user=test_user&github_repo=test_repo")
    mock_call_galaxy.assert_called_once_with('mocked_url', auth_required=True, method='DELETE')
    assert result == {'status': 'success'}
