# file: lib/ansible/galaxy/api.py:609-614
# asked: {"lines": [609, 610, 611, 612, 613, 614], "branches": []}
# gained: {"lines": [609, 610, 611, 612, 613, 614], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(
        galaxy="test_galaxy",
        name="test_name",
        url="http://testserver",
        username="test_user",
        password="test_pass",
        token="test_token",
        validate_certs=False,
        available_api_versions={'v1': 'v1'},
        clear_response_cache=True,
        no_cache=True
    )

@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy')
def test_delete_role(mock_call_galaxy, galaxy_api):
    mock_call_galaxy.return_value = {"status": "success"}
    github_user = "testuser"
    github_repo = "testrepo"
    
    result = galaxy_api.delete_role(github_user, github_repo)
    
    expected_url = "http://testserver/v1/removerole/?github_user=testuser&github_repo=testrepo"
    mock_call_galaxy.assert_called_once_with(expected_url, auth_required=True, method='DELETE')
    assert result == {"status": "success"}
