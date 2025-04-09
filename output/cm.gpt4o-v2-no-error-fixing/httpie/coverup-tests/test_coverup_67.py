# file: httpie/plugins/manager.py:47-48
# asked: {"lines": [47, 48], "branches": []}
# gained: {"lines": [47, 48], "branches": []}

import pytest
from typing import Type
from httpie.plugins import AuthPlugin
from httpie.plugins.manager import PluginManager

class DummyAuthPlugin(AuthPlugin):
    auth_type = 'dummy'

def test_get_auth_plugin(monkeypatch):
    # Create a PluginManager instance and add DummyAuthPlugin to it
    manager = PluginManager()
    manager.append(DummyAuthPlugin)

    # Mock the get_auth_plugins method to return our DummyAuthPlugin
    def mock_get_auth_plugins():
        return [DummyAuthPlugin]
    
    monkeypatch.setattr(manager, 'get_auth_plugins', mock_get_auth_plugins)

    # Test get_auth_plugin method
    auth_plugin = manager.get_auth_plugin('dummy')
    assert auth_plugin is DummyAuthPlugin

    # Clean up
    manager.clear()
