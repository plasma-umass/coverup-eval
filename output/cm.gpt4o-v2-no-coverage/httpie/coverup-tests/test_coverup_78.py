# file: httpie/plugins/manager.py:47-48
# asked: {"lines": [47, 48], "branches": []}
# gained: {"lines": [47, 48], "branches": []}

import pytest
from unittest.mock import Mock, patch
from httpie.plugins.manager import PluginManager, AuthPlugin

class MockAuthPlugin(AuthPlugin):
    auth_type = 'mock'

def test_get_auth_plugin():
    manager = PluginManager()
    
    with patch.object(manager, 'get_auth_plugin_mapping', return_value={'mock': MockAuthPlugin}):
        plugin = manager.get_auth_plugin('mock')
        assert plugin is MockAuthPlugin

def test_get_auth_plugin_mapping():
    manager = PluginManager()
    
    with patch.object(manager, 'get_auth_plugins', return_value=[MockAuthPlugin]):
        mapping = manager.get_auth_plugin_mapping()
        assert mapping == {'mock': MockAuthPlugin}
