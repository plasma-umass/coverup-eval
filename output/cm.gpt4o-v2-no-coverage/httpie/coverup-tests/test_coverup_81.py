# file: httpie/plugins/manager.py:65-66
# asked: {"lines": [65, 66], "branches": []}
# gained: {"lines": [65, 66], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import TransportPlugin, BasePlugin

class DummyTransportPlugin(TransportPlugin):
    pass

class DummyBasePlugin(BasePlugin):
    pass

def test_get_transport_plugins(monkeypatch):
    # Create a PluginManager instance with dummy plugins
    plugins = PluginManager([DummyTransportPlugin, DummyBasePlugin])

    # Patch the filter method to ensure it is called
    original_filter = plugins.filter
    def mock_filter(by_type):
        result = original_filter(by_type)
        assert by_type == TransportPlugin
        return result

    monkeypatch.setattr(plugins, 'filter', mock_filter)

    # Call get_transport_plugins and verify the result
    transport_plugins = plugins.get_transport_plugins()
    assert transport_plugins == [DummyTransportPlugin]

    # Clean up
    monkeypatch.undo()
