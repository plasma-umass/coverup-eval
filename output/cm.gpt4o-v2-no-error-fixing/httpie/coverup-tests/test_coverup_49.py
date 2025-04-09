# file: httpie/plugins/manager.py:42-45
# asked: {"lines": [42, 43, 44], "branches": []}
# gained: {"lines": [42, 43, 44], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager, AuthPlugin

class DummyAuthPlugin(AuthPlugin):
    auth_type = 'dummy'

def test_get_auth_plugin_mapping(monkeypatch):
    def mock_get_auth_plugins(self):
        return [DummyAuthPlugin]

    monkeypatch.setattr(PluginManager, 'get_auth_plugins', mock_get_auth_plugins)
    
    manager = PluginManager()
    auth_plugin_mapping = manager.get_auth_plugin_mapping()
    
    assert 'dummy' in auth_plugin_mapping
    assert auth_plugin_mapping['dummy'] is DummyAuthPlugin
