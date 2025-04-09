# file httpie/plugins/manager.py:47-48
# lines [47, 48]
# branches []

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import AuthPlugin

class DummyAuthPlugin(AuthPlugin):
    auth_type = 'dummy'
    auth_require = None

    def get_auth(self, username=None, password=None):
        pass

@pytest.fixture
def plugin_manager():
    pm = PluginManager()
    yield pm
    pm.clear()

def test_get_auth_plugin(plugin_manager):
    plugin_manager.append(DummyAuthPlugin)
    auth_plugin = plugin_manager.get_auth_plugin('dummy')
    assert auth_plugin == DummyAuthPlugin

    with pytest.raises(KeyError):
        plugin_manager.get_auth_plugin('nonexistent')
