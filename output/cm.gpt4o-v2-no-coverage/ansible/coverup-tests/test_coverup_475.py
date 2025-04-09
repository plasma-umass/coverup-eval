# file: lib/ansible/galaxy/api.py:585-595
# asked: {"lines": [585, 586, 587, 588, 589, 590, 591, 592, 594, 595], "branches": []}
# gained: {"lines": [585, 586, 587, 588, 589, 590, 591, 592, 594, 595], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(
        galaxy="test_galaxy",
        name="test_name",
        url="http://testserver/api/",
        username="test_user",
        password="test_pass",
        token="test_token",
        validate_certs=False,
        available_api_versions={"v1": "v1_endpoint"},
        clear_response_cache=True,
        no_cache=True,
        priority=1
    )

@patch('ansible.galaxy.api._urljoin', return_value="http://testserver/api/v1/notification_secrets")
@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy', return_value={"result": "success"})
def test_add_secret(mock_call_galaxy, mock_urljoin, galaxy_api):
    source = "test_source"
    github_user = "test_github_user"
    github_repo = "test_github_repo"
    secret = "test_secret"
    
    result = galaxy_api.add_secret(source, github_user, github_repo, secret)
    
    expected_url = "http://testserver/api/v1/notification_secrets/"
    expected_args = urlencode({
        "source": source,
        "github_user": github_user,
        "github_repo": github_repo,
        "secret": secret
    })
    
    mock_urljoin.assert_called_once_with(galaxy_api.api_server, galaxy_api.available_api_versions['v1'], "notification_secrets")
    mock_call_galaxy.assert_called_once_with(expected_url, args=expected_args, method="POST")
    
    assert result == {"result": "success"}
