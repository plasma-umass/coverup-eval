# file: lib/ansible/galaxy/api.py:585-595
# asked: {"lines": [587, 588, 589, 590, 591, 592, 594, 595], "branches": []}
# gained: {"lines": [587, 588, 589, 590, 591, 592, 594, 595], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    api = GalaxyAPI(galaxy="mockgalaxy", name="mockname", url="http://mockserver")
    api._available_api_versions = {'v1': 'v1'}
    return api

def test_add_secret(galaxy_api, monkeypatch):
    mock_urljoin = MagicMock(return_value="http://mockserver/api/v1/notification_secrets")
    mock_urlencode = MagicMock(return_value="source=mocksource&github_user=mockuser&github_repo=mockrepo&secret=mocksecret")
    mock_call_galaxy = MagicMock(return_value={"status": "success"})

    monkeypatch.setattr("ansible.galaxy.api._urljoin", mock_urljoin)
    monkeypatch.setattr("ansible.galaxy.api.urlencode", mock_urlencode)
    monkeypatch.setattr(galaxy_api, "_call_galaxy", mock_call_galaxy)

    result = galaxy_api.add_secret("mocksource", "mockuser", "mockrepo", "mocksecret")

    mock_urljoin.assert_called_once_with(galaxy_api.api_server, galaxy_api.available_api_versions['v1'], "notification_secrets")
    mock_urlencode.assert_called_once_with({
        "source": "mocksource",
        "github_user": "mockuser",
        "github_repo": "mockrepo",
        "secret": "mocksecret"
    })
    mock_call_galaxy.assert_called_once_with("http://mockserver/api/v1/notification_secrets/", args="source=mocksource&github_user=mockuser&github_repo=mockrepo&secret=mocksecret", method="POST")
    
    assert result == {"status": "success"}
