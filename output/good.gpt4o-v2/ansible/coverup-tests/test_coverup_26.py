# file: lib/ansible/galaxy/api.py:63-128
# asked: {"lines": [63, 70, 71, 72, 73, 77, 78, 80, 81, 83, 84, 85, 88, 89, 92, 93, 94, 95, 96, 97, 98, 100, 101, 102, 106, 110, 111, 112, 114, 115, 116, 119, 120, 121, 122, 123, 124, 126, 127, 128], "branches": [[72, 73], [72, 119], [80, 81], [80, 83], [88, 89], [88, 92], [96, 97], [96, 98], [100, 101], [100, 106], [111, 112], [111, 114], [121, 122], [121, 126]]}
# gained: {"lines": [63, 70, 71, 72, 73, 77, 78, 80, 81, 83, 84, 85, 88, 92, 93, 94, 95, 96, 97, 100, 101, 102, 106, 110, 111, 112, 114, 115, 116, 119, 120, 121, 122, 123, 124, 126, 127, 128], "branches": [[72, 73], [80, 81], [80, 83], [88, 92], [96, 97], [100, 101], [100, 106], [111, 112], [111, 114], [121, 122], [121, 126]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.galaxy.api import g_connect, GalaxyError

class MockGalaxy:
    def __init__(self, api_server, name):
        self.api_server = api_server
        self.name = name
        self._available_api_versions = None

    def _call_galaxy(self, url, method, error_context_msg, cache):
        if "error" in url:
            raise AnsibleError("Mocked error")
        if "404" in url:
            raise GalaxyError(MagicMock(code=404, reason="Not Found", geturl=lambda: url), "Mocked 404 error")
        return {"available_versions": {"v1": "v1/"}}

    @g_connect(["v1", "v2"])
    def some_method(self):
        return "success"

def test_g_connect_initial_connection(monkeypatch):
    mock_galaxy = MockGalaxy("https://galaxy.ansible.com", "test_server")
    monkeypatch.setattr("ansible.galaxy.api.display.vvvv", MagicMock())
    result = mock_galaxy.some_method()
    assert result == "success"
    assert mock_galaxy.api_server == "https://galaxy.ansible.com/api/"
    assert "v2" in mock_galaxy._available_api_versions

def test_g_connect_error_handling(monkeypatch):
    mock_galaxy = MockGalaxy("https://error.ansible.com", "test_server")
    monkeypatch.setattr("ansible.galaxy.api.display.vvvv", MagicMock())
    with pytest.raises(AnsibleError, match="Mocked error"):
        mock_galaxy.some_method()

def test_g_connect_404_handling(monkeypatch):
    mock_galaxy = MockGalaxy("https://404.ansible.com", "test_server")
    monkeypatch.setattr("ansible.galaxy.api.display.vvvv", MagicMock())
    with pytest.raises(AnsibleError, match="Mocked 404 error"):
        mock_galaxy.some_method()

def test_g_connect_no_available_versions(monkeypatch):
    mock_galaxy = MockGalaxy("https://no_versions.ansible.com", "test_server")
    monkeypatch.setattr("ansible.galaxy.api.display.vvvv", MagicMock())
    monkeypatch.setattr(mock_galaxy, "_call_galaxy", lambda *args, **kwargs: {})
    with pytest.raises(AnsibleError, match="no 'available_versions' are available"):
        mock_galaxy.some_method()

def test_g_connect_version_mismatch(monkeypatch):
    mock_galaxy = MockGalaxy("https://mismatch.ansible.com", "test_server")
    monkeypatch.setattr("ansible.galaxy.api.display.vvvv", MagicMock())
    monkeypatch.setattr(mock_galaxy, "_call_galaxy", lambda *args, **kwargs: {"available_versions": {"v3": "v3/"}})
    with pytest.raises(AnsibleError, match="requires API versions 'v1, v2' but only 'v3' are available"):
        mock_galaxy.some_method()
