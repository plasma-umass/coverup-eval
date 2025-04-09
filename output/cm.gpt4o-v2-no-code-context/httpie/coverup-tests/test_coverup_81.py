# file: httpie/client.py:147-173
# asked: {"lines": [152, 155, 156, 157, 159, 160, 163, 166, 167, 168, 169, 170, 173], "branches": [[166, 167], [166, 173]]}
# gained: {"lines": [152, 155, 156, 157, 159, 160, 163, 166, 167, 168, 169, 170, 173], "branches": [[166, 167], [166, 173]]}

import pytest
import requests
from httpie.client import build_requests_session, HTTPieHTTPSAdapter, plugin_manager

class MockTransportPlugin:
    prefix = 'mock://'
    
    def get_adapter(self):
        return requests.adapters.HTTPAdapter()

@pytest.fixture
def mock_plugin_manager(monkeypatch):
    class MockPluginManager:
        def get_transport_plugins(self):
            return [MockTransportPlugin]
    
    monkeypatch.setattr('httpie.client.plugin_manager', MockPluginManager())

@pytest.fixture
def mock_ssl_version_mapping(monkeypatch):
    mock_mapping = {
        'TLSv1_2': 'PROTOCOL_TLSv1_2'
    }
    monkeypatch.setattr('httpie.client.AVAILABLE_SSL_VERSION_ARG_MAPPING', mock_mapping)

def test_build_requests_session_with_ssl_version(mock_plugin_manager, mock_ssl_version_mapping):
    session = build_requests_session(verify=True, ssl_version='TLSv1_2', ciphers='ECDHE-RSA-AES128-GCM-SHA256')
    assert isinstance(session, requests.Session)
    assert 'https://' in session.adapters
    assert isinstance(session.adapters['https://'], HTTPieHTTPSAdapter)
    assert 'mock://' in session.adapters
    assert isinstance(session.adapters['mock://'], requests.adapters.HTTPAdapter)

def test_build_requests_session_without_ssl_version(mock_plugin_manager):
    session = build_requests_session(verify=False)
    assert isinstance(session, requests.Session)
    assert 'https://' in session.adapters
    assert isinstance(session.adapters['https://'], HTTPieHTTPSAdapter)
    assert 'mock://' in session.adapters
    assert isinstance(session.adapters['mock://'], requests.adapters.HTTPAdapter)
