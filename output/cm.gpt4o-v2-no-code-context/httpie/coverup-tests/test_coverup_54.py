# file: httpie/plugins/manager.py:47-48
# asked: {"lines": [47, 48], "branches": []}
# gained: {"lines": [47, 48], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager, AuthPlugin

class DummyAuthPlugin(AuthPlugin):
    name = 'dummy'
    auth_type = 'dummy'

@pytest.fixture
def plugin_manager():
    pm = PluginManager()
    pm.append(DummyAuthPlugin)
    return pm

def test_get_auth_plugin(plugin_manager):
    auth_plugin = plugin_manager.get_auth_plugin('dummy')
    assert auth_plugin is DummyAuthPlugin

def test_get_auth_plugin_not_found(plugin_manager):
    with pytest.raises(KeyError):
        plugin_manager.get_auth_plugin('nonexistent')
