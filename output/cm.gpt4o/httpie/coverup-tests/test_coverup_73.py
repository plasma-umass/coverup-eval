# file httpie/plugins/manager.py:65-66
# lines [65, 66]
# branches []

import pytest
from httpie.plugins.manager import PluginManager, TransportPlugin

class MockTransportPlugin(TransportPlugin):
    name = 'mock_transport'

def test_get_transport_plugins(mocker):
    # Create a mock TransportPlugin
    mock_plugin = MockTransportPlugin()
    
    # Mock the filter method to return the mock plugin
    mocker.patch.object(PluginManager, 'filter', return_value=[mock_plugin])
    
    # Create an instance of PluginManager
    plugin_manager = PluginManager()
    
    # Call the get_transport_plugins method
    transport_plugins = plugin_manager.get_transport_plugins()
    
    # Assert that the returned list contains the mock plugin
    assert transport_plugins == [mock_plugin]
    
    # Clean up by unpatching
    mocker.stopall()
