# file httpie/plugins/base.py:70-91
# lines [70, 71, 83, 85, 91]
# branches []

import pytest
from httpie.plugins.base import TransportPlugin
from requests.adapters import BaseAdapter

class DummyAdapter(BaseAdapter):
    pass

class DummyTransportPlugin(TransportPlugin):
    prefix = 'http://example.com'

    def get_adapter(self):
        return DummyAdapter()

@pytest.fixture
def dummy_transport_plugin():
    return DummyTransportPlugin()

def test_transport_plugin_get_adapter(dummy_transport_plugin):
    adapter = dummy_transport_plugin.get_adapter()
    assert isinstance(adapter, BaseAdapter)

def test_transport_plugin_get_adapter_not_implemented():
    plugin = TransportPlugin()
    with pytest.raises(NotImplementedError):
        plugin.get_adapter()
