# file: lib/ansible/galaxy/api.py:597-601
# asked: {"lines": [599, 600, 601], "branches": []}
# gained: {"lines": [599, 600, 601], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
import functools

# Assuming the GalaxyAPI class is defined in ansible/galaxy/api.py
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    return GalaxyAPI(galaxy="mocked_galaxy", name="mocked_name", url="mocked_url")

def test_list_secrets(galaxy_api, monkeypatch):
    mock_urljoin = MagicMock(return_value="mocked_url")
    mock_call_galaxy = MagicMock(return_value={"secrets": ["secret1", "secret2"]})

    monkeypatch.setattr("ansible.galaxy.api._urljoin", mock_urljoin)
    monkeypatch.setattr(galaxy_api, "_call_galaxy", mock_call_galaxy)
    monkeypatch.setattr(galaxy_api, "api_server", "mocked_server")
    monkeypatch.setattr(galaxy_api, "_available_api_versions", {'v1': 'mocked_version'})

    result = galaxy_api.list_secrets()

    mock_urljoin.assert_called_once_with("mocked_server", "mocked_version", "notification_secrets")
    mock_call_galaxy.assert_called_once_with("mocked_url", auth_required=True)
    assert result == {"secrets": ["secret1", "secret2"]}
