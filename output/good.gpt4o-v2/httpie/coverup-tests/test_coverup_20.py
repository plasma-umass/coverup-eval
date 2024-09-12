# file: httpie/client.py:147-173
# asked: {"lines": [147, 149, 150, 152, 155, 156, 157, 159, 160, 163, 166, 167, 168, 169, 170, 173], "branches": [[166, 167], [166, 173]]}
# gained: {"lines": [147, 149, 150, 152, 155, 156, 157, 159, 160, 163, 166, 167, 168, 169, 170, 173], "branches": [[166, 167], [166, 173]]}

import pytest
import requests
from httpie.client import build_requests_session
from httpie.plugins.registry import plugin_manager
from httpie.ssl import HTTPieHTTPSAdapter, AVAILABLE_SSL_VERSION_ARG_MAPPING

class MockTransportPlugin:
    prefix = 'mock://'
    
    @staticmethod
    def get_adapter():
        return requests.adapters.HTTPAdapter()

def test_build_requests_session_with_ssl_version_and_ciphers(monkeypatch):
    def mock_get_transport_plugins():
        return [MockTransportPlugin]
    
    monkeypatch.setattr(plugin_manager, 'get_transport_plugins', mock_get_transport_plugins)
    
    # Use a valid SSL version key from AVAILABLE_SSL_VERSION_ARG_MAPPING
    valid_ssl_version = next(iter(AVAILABLE_SSL_VERSION_ARG_MAPPING.keys()))
    
    session = build_requests_session(verify=True, ssl_version=valid_ssl_version, ciphers='ECDHE+AESGCM')
    
    assert isinstance(session, requests.Session)
    assert 'https://' in session.adapters
    assert isinstance(session.adapters['https://'], HTTPieHTTPSAdapter)
    assert 'mock://' in session.adapters
    assert isinstance(session.adapters['mock://'], requests.adapters.HTTPAdapter)

def test_build_requests_session_without_ssl_version_and_ciphers(monkeypatch):
    def mock_get_transport_plugins():
        return [MockTransportPlugin]
    
    monkeypatch.setattr(plugin_manager, 'get_transport_plugins', mock_get_transport_plugins)
    
    session = build_requests_session(verify=False)
    
    assert isinstance(session, requests.Session)
    assert 'https://' in session.adapters
    assert isinstance(session.adapters['https://'], HTTPieHTTPSAdapter)
    assert 'mock://' in session.adapters
    assert isinstance(session.adapters['mock://'], requests.adapters.HTTPAdapter)
