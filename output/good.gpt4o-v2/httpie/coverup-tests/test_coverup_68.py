# file: httpie/plugins/manager.py:42-45
# asked: {"lines": [42, 43, 44], "branches": []}
# gained: {"lines": [42, 43, 44], "branches": []}

import pytest
from unittest.mock import Mock
from httpie.plugins.manager import PluginManager, AuthPlugin

class MockAuthPlugin(AuthPlugin):
    name = 'mock'
    auth_type = 'mock_type'

@pytest.fixture
def plugin_manager(monkeypatch):
    manager = PluginManager()
    mock_get_auth_plugins = Mock(return_value=[MockAuthPlugin])
    monkeypatch.setattr(manager, 'get_auth_plugins', mock_get_auth_plugins)
    return manager

def test_get_auth_plugin_mapping(plugin_manager):
    mapping = plugin_manager.get_auth_plugin_mapping()
    assert 'mock_type' in mapping
    assert mapping['mock_type'] is MockAuthPlugin
