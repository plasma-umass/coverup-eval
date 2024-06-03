# file httpie/plugins/manager.py:47-48
# lines [48]
# branches []

import pytest
from httpie.plugins.manager import PluginManager, AuthPlugin

class DummyAuthPlugin(AuthPlugin):
    name = 'dummy'
    auth_type = 'dummy'

@pytest.fixture
def plugin_manager():
    manager = PluginManager()
    manager.append(DummyAuthPlugin)
    yield manager
    manager.clear()

def test_get_auth_plugin(plugin_manager):
    plugin_mapping = plugin_manager.get_auth_plugin_mapping()
    assert 'dummy' in plugin_mapping
    assert plugin_mapping['dummy'] == DummyAuthPlugin

    auth_plugin = plugin_manager.get_auth_plugin('dummy')
    assert auth_plugin == DummyAuthPlugin
