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

    # Ensure the get_transport_plugins method returns the correct plugin
    transport_plugins = plugin_manager.get_transport_plugins()
    assert transport_plugins == [DummyTransportPlugin]

    # Clean up after the test
    monkeypatch.undo()
