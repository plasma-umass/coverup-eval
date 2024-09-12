# file: lib/ansible/galaxy/api.py:585-595
# asked: {"lines": [587, 588, 589, 590, 591, 592, 594, 595], "branches": []}
# gained: {"lines": [587, 588, 589, 590, 591, 592, 594, 595], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(
        galaxy='mock_galaxy',
        name='mock_name',
        url='http://mockserver',
        available_api_versions={'v1': 'v1'}
    )

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
@patch('ansible.galaxy.api._urljoin', return_value='http://mockserver/api/v1/notification_secrets')
def test_add_secret(mock_urljoin, mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {'result': 'success'}
    
    source = 'source_value'
    github_user = 'github_user_value'
    github_repo = 'github_repo_value'
    secret = 'secret_value'
    
    result = galaxy_api.add_secret(source, github_user, github_repo, secret)
    
    expected_url = 'http://mockserver/api/v1/notification_secrets/'
    expected_args = urlencode({
        'source': source,
        'github_user': github_user,
        'github_repo': github_repo,
        'secret': secret
    })
    
    mock_urljoin.assert_called_once_with(galaxy_api.api_server, galaxy_api.available_api_versions['v1'], 'notification_secrets')
    mock_call_galaxy.assert_called_once_with(expected_url, args=expected_args, method='POST')
    
    assert result == {'result': 'success'}
