# file httpie/plugins/manager.py:42-45
# lines [42, 43, 44]
# branches []

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import AuthPlugin

# Mock AuthPlugin to test the PluginManager
class MockAuthPlugin(AuthPlugin):
    auth_type = 'mock_auth'
    name = 'mock_auth_plugin'
    description = 'Mock authentication plugin for testing'

    def get_auth(self, username=None, password=None):
        pass

@pytest.fixture
def plugin_manager():
    manager = PluginManager()
    yield manager
    manager.clear()

def test_get_auth_plugin_mapping(plugin_manager):
    # Add a mock plugin to the manager
    plugin_manager.append(MockAuthPlugin)

    # Get the auth plugin mapping
    auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()

    # Assert that the mapping contains the mock plugin
    assert 'mock_auth' in auth_plugin_mapping
    assert auth_plugin_mapping['mock_auth'] == MockAuthPlugin

    # Clean up the plugin manager
    plugin_manager.remove(MockAuthPlugin)
