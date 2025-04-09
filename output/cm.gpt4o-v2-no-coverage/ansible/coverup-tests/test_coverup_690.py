# file: lib/ansible/galaxy/api.py:597-601
# asked: {"lines": [597, 598, 599, 600, 601], "branches": []}
# gained: {"lines": [597, 598, 599, 600, 601], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(
        galaxy="test_galaxy",
        name="test_name",
        url="http://testserver/api",
        username="test_user",
        password="test_pass",
        token="test_token",
        validate_certs=False,
        available_api_versions={'v1': 'v1_endpoint'},
        clear_response_cache=True,
        no_cache=True
    )

@patch('ansible.galaxy.api._urljoin', return_value="http://testserver/api/v1_endpoint/notification_secrets")
@patch('ansible.galaxy.api.GalaxyAPI._call_galaxy', return_value={"secrets": []})
def test_list_secrets(mock_call_galaxy, mock_urljoin, galaxy_api):
    result = galaxy_api.list_secrets()
    mock_urljoin.assert_called_once_with("http://testserver/api", 'v1_endpoint', "notification_secrets")
    mock_call_galaxy.assert_called_once_with("http://testserver/api/v1_endpoint/notification_secrets", auth_required=True)
    assert result == {"secrets": []}
