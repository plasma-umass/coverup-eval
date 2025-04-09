# file httpie/plugins/manager.py:42-45
# lines [43, 44]
# branches []

import pytest
from httpie.plugins.manager import PluginManager

class DummyAuthPlugin:
    auth_type = 'dummy'

@pytest.fixture
def plugin_manager():
    manager = PluginManager()
    yield manager
    manager.clear()

def test_get_auth_plugin_mapping(plugin_manager, mocker):
    mocker.patch.object(plugin_manager, 'get_auth_plugins', return_value=[DummyAuthPlugin])
    auth_mapping = plugin_manager.get_auth_plugin_mapping()
    assert 'dummy' in auth_mapping
    assert auth_mapping['dummy'] is DummyAuthPlugin
