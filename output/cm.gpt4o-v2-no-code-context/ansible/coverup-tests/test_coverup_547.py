# file: lib/ansible/galaxy/api.py:609-614
# asked: {"lines": [609, 610, 611, 612, 613, 614], "branches": []}
# gained: {"lines": [609, 610, 611, 612, 613, 614], "branches": []}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the GalaxyAPI class is imported from ansible/galaxy/api.py
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    api_server = "https://galaxy.ansible.com"
    available_api_versions = {'v1': 'v1'}
    return GalaxyAPI(galaxy="test_galaxy", name="test_name", url=api_server, available_api_versions=available_api_versions)

def test_delete_role_success(galaxy_api, monkeypatch):
    mock_urljoin = MagicMock(return_value="mocked_url")
    mock_call_galaxy = MagicMock(return_value={"status": "success"})

    monkeypatch.setattr("ansible.galaxy.api._urljoin", mock_urljoin)
    monkeypatch.setattr(galaxy_api, "_call_galaxy", mock_call_galaxy)

    github_user = "test_user"
    github_repo = "test_repo"

    result = galaxy_api.delete_role(github_user, github_repo)

    mock_urljoin.assert_called_once_with(galaxy_api.api_server, galaxy_api.available_api_versions['v1'], "removerole",
                                         "?github_user=test_user&github_repo=test_repo")
    mock_call_galaxy.assert_called_once_with("mocked_url", auth_required=True, method='DELETE')
    assert result == {"status": "success"}

def test_delete_role_failure(galaxy_api, monkeypatch):
    mock_urljoin = MagicMock(return_value="mocked_url")
    mock_call_galaxy = MagicMock(return_value={"status": "failure"})

    monkeypatch.setattr("ansible.galaxy.api._urljoin", mock_urljoin)
    monkeypatch.setattr(galaxy_api, "_call_galaxy", mock_call_galaxy)

    github_user = "test_user"
    github_repo = "test_repo"

    result = galaxy_api.delete_role(github_user, github_repo)

    mock_urljoin.assert_called_once_with(galaxy_api.api_server, galaxy_api.available_api_versions['v1'], "removerole",
                                         "?github_user=test_user&github_repo=test_repo")
    mock_call_galaxy.assert_called_once_with("mocked_url", auth_required=True, method='DELETE')
    assert result == {"status": "failure"}
