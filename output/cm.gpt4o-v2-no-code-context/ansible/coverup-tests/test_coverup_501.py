# file: lib/ansible/galaxy/api.py:431-440
# asked: {"lines": [431, 432, 436, 437, 438, 439, 440], "branches": []}
# gained: {"lines": [431, 432, 436, 437, 438, 439, 440], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api():
    api = GalaxyAPI(galaxy="fake_galaxy", name="fake_name", url="http://fakeurl.com")
    api._available_api_versions = {'v1': 'v1'}
    return api

def test_authenticate_success(galaxy_api, monkeypatch):
    mock_response = MagicMock()
    mock_response.read.return_value = b'{"token": "fake_token"}'
    
    def mock_open_url(url, data, validate_certs, method, http_agent):
        return mock_response
    
    monkeypatch.setattr('ansible.galaxy.api.open_url', mock_open_url)
    monkeypatch.setattr('ansible.galaxy.api._urljoin', lambda *args: "http://fakeurl.com")
    monkeypatch.setattr('ansible.galaxy.api.urlencode', lambda x: "github_token=fake_token")
    monkeypatch.setattr('ansible.galaxy.api.user_agent', lambda: "fake_agent")
    monkeypatch.setattr('ansible.galaxy.api.to_text', lambda x, errors: x.decode('utf-8'))
    
    galaxy_api.api_server = "http://fakeurl.com"
    galaxy_api.validate_certs = True
    
    result = galaxy_api.authenticate("fake_token")
    
    assert result == {"token": "fake_token"}

def test_authenticate_failure(galaxy_api, monkeypatch):
    def mock_open_url(url, data, validate_certs, method, http_agent):
        raise Exception("Authentication failed")
    
    monkeypatch.setattr('ansible.galaxy.api.open_url', mock_open_url)
    monkeypatch.setattr('ansible.galaxy.api._urljoin', lambda *args: "http://fakeurl.com")
    monkeypatch.setattr('ansible.galaxy.api.urlencode', lambda x: "github_token=fake_token")
    monkeypatch.setattr('ansible.galaxy.api.user_agent', lambda: "fake_agent")
    
    galaxy_api.api_server = "http://fakeurl.com"
    galaxy_api.validate_certs = True
    
    with pytest.raises(Exception, match="Authentication failed"):
        galaxy_api.authenticate("fake_token")
