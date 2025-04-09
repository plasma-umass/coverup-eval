# file: httpie/plugins/manager.py:65-66
# asked: {"lines": [65, 66], "branches": []}
# gained: {"lines": [65, 66], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import TransportPlugin

class DummyTransportPlugin(TransportPlugin):
    name = 'dummy'

def test_get_transport_plugins(monkeypatch):
    # Create a dummy plugin manager with a dummy transport plugin
    plugin_manager = PluginManager([DummyTransportPlugin])

    # Ensure the filter method is called correctly
    def mock_filter(by_type):
        assert by_type == TransportPlugin
        return [DummyTransportPlugin]

    monkeypatch.setattr(plugin_manager, 'filter', mock_filter)

    # Call the method and check the result
    result = plugin_manager.get_transport_plugins()
    assert result == [DummyTransportPlugin]
