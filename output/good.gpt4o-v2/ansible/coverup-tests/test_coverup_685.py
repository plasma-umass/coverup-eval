# file: lib/ansible/galaxy/api.py:597-601
# asked: {"lines": [597, 598, 599, 600, 601], "branches": []}
# gained: {"lines": [597, 598, 599, 600, 601], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.api import GalaxyAPI
from ansible.errors import AnsibleError

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(galaxy='test_galaxy', name='test_name', url='https://test_url.com', available_api_versions={'v1': 'v1/'})

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
@patch('ansible.galaxy.api._urljoin')
def test_list_secrets(mock_urljoin, mock_call_galaxy, galaxy_api):
    # Setup mock return values
    mock_urljoin.return_value = 'mocked_url'
    mock_call_galaxy.return_value = {'key': 'value'}

    # Call the method
    result = galaxy_api.list_secrets()

    # Assertions
    mock_urljoin.assert_called_once_with(galaxy_api.api_server, galaxy_api._available_api_versions['v1'], "notification_secrets")
    mock_call_galaxy.assert_called_once_with('mocked_url', auth_required=True)
    assert result == {'key': 'value'}
