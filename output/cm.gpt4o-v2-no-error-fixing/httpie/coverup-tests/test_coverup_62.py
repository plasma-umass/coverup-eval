# file: httpie/plugins/manager.py:39-40
# asked: {"lines": [39, 40], "branches": []}
# gained: {"lines": [39, 40], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins import AuthPlugin

class DummyAuthPlugin(AuthPlugin):
    name = 'dummy-auth'
    auth_type = 'dummy'

def test_get_auth_plugins():
    manager = PluginManager()
    manager.append(DummyAuthPlugin)
    
    auth_plugins = manager.get_auth_plugins()
    
    assert len(auth_plugins) == 1
    assert auth_plugins[0] is DummyAuthPlugin

    # Clean up
    manager.clear()
