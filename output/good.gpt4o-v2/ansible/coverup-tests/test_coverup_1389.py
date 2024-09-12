# file: lib/ansible/galaxy/api.py:431-440
# asked: {"lines": [436, 437, 438, 439, 440], "branches": []}
# gained: {"lines": [436, 437, 438, 439, 440], "branches": []}

import pytest
import json
from unittest.mock import patch, Mock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(
        galaxy=None,
        name="test",
        url="http://testserver",
        username="user",
        password="pass",
        token=None,
        validate_certs=False,
        available_api_versions={'v1': 'v1/'},
        clear_response_cache=True,
        no_cache=True,
        priority=1.0
    )

@patch('ansible.module_utils.urls.Request.open')
def test_authenticate(mock_open, galaxy_api):
    mock_response = Mock()
    mock_response.read.return_value = json.dumps({"token": "test_token"}).encode('utf-8')
    mock_open.return_value = mock_response

    github_token = "fake_github_token"
    result = galaxy_api.authenticate(github_token)

    mock_open.assert_called_once()
    assert result == {"token": "test_token"}
