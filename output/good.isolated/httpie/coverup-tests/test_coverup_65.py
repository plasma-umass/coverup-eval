# file httpie/plugins/manager.py:39-40
# lines [39, 40]
# branches []

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import AuthPlugin

# Mock AuthPlugin class for testing
class MockAuthPlugin(AuthPlugin):
    name = 'mock_auth_plugin'
    auth_type = 'mock'
    description = 'Mock authentication plugin'

# Test function to improve coverage
def test_get_auth_plugins(mocker):
    # Create a PluginManager instance
    plugin_manager = PluginManager()

    # Add a mock AuthPlugin to the plugin manager
    plugin_manager.append(MockAuthPlugin)

    # Use mocker to ensure isolation and cleanup
    mocker.patch.object(plugin_manager, 'filter', return_value=[MockAuthPlugin])

    # Call get_auth_plugins and assert the returned list contains MockAuthPlugin
    auth_plugins = plugin_manager.get_auth_plugins()
    assert MockAuthPlugin in auth_plugins

    # Assert that the filter method was called with AuthPlugin as argument
    plugin_manager.filter.assert_called_once_with(AuthPlugin)
