# file httpie/plugins/manager.py:65-66
# lines [65, 66]
# branches []

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import TransportPlugin

# Mock TransportPlugin to simulate a real plugin
class MockTransportPlugin(TransportPlugin):
    pass

# Test function to cover get_transport_plugins method
def test_get_transport_plugins(mocker):
    # Create a PluginManager instance
    plugin_manager = PluginManager()

    # Add a mock transport plugin to the manager
    plugin_manager.append(MockTransportPlugin)

    # Use mocker to ensure isolation and cleanup
    mocker.patch.object(plugin_manager, 'filter', return_value=[MockTransportPlugin])

    # Call the method under test
    transport_plugins = plugin_manager.get_transport_plugins()

    # Assert that the filter method was called with TransportPlugin as argument
    plugin_manager.filter.assert_called_once_with(TransportPlugin)

    # Assert that the returned list contains the mock transport plugin
    assert transport_plugins == [MockTransportPlugin]
