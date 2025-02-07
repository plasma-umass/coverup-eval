# file: httpie/plugins/manager.py:47-48
# asked: {"lines": [47, 48], "branches": []}
# gained: {"lines": [47, 48], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager, AuthPlugin

class DummyAuthPlugin(AuthPlugin):
    name = 'dummy'
    auth_type = 'dummy'

def test_get_auth_plugin(monkeypatch):
    def mock_get_auth_plugins(self):
        return [DummyAuthPlugin]

    monkeypatch.setattr(PluginManager, 'get_auth_plugins', mock_get_auth_plugins)
    
    manager = PluginManager()
    plugin = manager.get_auth_plugin('dummy')
    
    assert plugin is DummyAuthPlugin
