# file: httpie/plugins/base.py:70-91
# asked: {"lines": [70, 71, 83, 85, 91], "branches": []}
# gained: {"lines": [70, 71, 83, 85, 91], "branches": []}

import pytest
from httpie.plugins.base import TransportPlugin
from requests.adapters import BaseAdapter

class MockAdapter(BaseAdapter):
    def send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        pass

    def close(self):
        pass

def test_transport_plugin_get_adapter_not_implemented():
    plugin = TransportPlugin()
    with pytest.raises(NotImplementedError):
        plugin.get_adapter()

def test_transport_plugin_prefix():
    plugin = TransportPlugin()
    assert plugin.prefix is None

class CustomTransportPlugin(TransportPlugin):
    def get_adapter(self):
        return MockAdapter()

def test_custom_transport_plugin_get_adapter():
    plugin = CustomTransportPlugin()
    adapter = plugin.get_adapter()
    assert isinstance(adapter, MockAdapter)
