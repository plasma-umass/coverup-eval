# file: httpie/client.py:147-173
# asked: {"lines": [147, 149, 150, 152, 155, 156, 157, 159, 160, 163, 166, 167, 168, 169, 170, 173], "branches": [[166, 167], [166, 173]]}
# gained: {"lines": [147, 149, 150, 152, 155, 156, 157, 159, 160, 163, 166, 167, 168, 169, 170, 173], "branches": [[166, 167], [166, 173]]}

import pytest
import requests
from unittest.mock import patch, create_autospec
from httpie.client import build_requests_session
from httpie.ssl import HTTPieHTTPSAdapter, AVAILABLE_SSL_VERSION_ARG_MAPPING
from httpie.plugins.registry import plugin_manager

class MockTransportPlugin:
    prefix = 'mock://'
    
    def get_adapter(self):
        return requests.adapters.HTTPAdapter()

@pytest.fixture
def mock_plugin_manager(monkeypatch):
    mock_get_transport_plugins = create_autospec(plugin_manager.get_transport_plugins, return_value=[MockTransportPlugin])
    monkeypatch.setattr(plugin_manager, 'get_transport_plugins', mock_get_transport_plugins)
    return mock_get_transport_plugins

def test_build_requests_session_no_ssl(mock_plugin_manager):
    session = build_requests_session(verify=True)
    assert isinstance(session, requests.Session)
    assert 'https://' in session.adapters
    assert isinstance(session.adapters['https://'], HTTPieHTTPSAdapter)
    assert session.adapters['https://']._ssl_context is not None
    assert 'mock://' in session.adapters
    assert isinstance(session.adapters['mock://'], requests.adapters.HTTPAdapter)

def test_build_requests_session_with_ssl(mock_plugin_manager):
    ssl_version = next(iter(AVAILABLE_SSL_VERSION_ARG_MAPPING))  # Get a valid SSL version
    session = build_requests_session(verify=False, ssl_version=ssl_version, ciphers='ECDHE+AESGCM')
    assert isinstance(session, requests.Session)
    assert 'https://' in session.adapters
    assert isinstance(session.adapters['https://'], HTTPieHTTPSAdapter)
    assert session.adapters['https://']._ssl_context is not None
    assert 'mock://' in session.adapters
    assert isinstance(session.adapters['mock://'], requests.adapters.HTTPAdapter)
