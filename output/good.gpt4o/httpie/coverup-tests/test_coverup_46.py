# file httpie/plugins/base.py:70-91
# lines [70, 71, 83, 85, 91]
# branches []

import pytest
from httpie.plugins.base import TransportPlugin
from requests.adapters import BaseAdapter

def test_transport_plugin_get_adapter_not_implemented():
    class MyTransportPlugin(TransportPlugin):
        prefix = 'http://'

    plugin = MyTransportPlugin()
    with pytest.raises(NotImplementedError):
        plugin.get_adapter()

def test_transport_plugin_prefix():
    class MyTransportPlugin(TransportPlugin):
        prefix = 'http://'

    plugin = MyTransportPlugin()
    assert plugin.prefix == 'http://'

def test_transport_plugin_custom_adapter(mocker):
    class MyAdapter(BaseAdapter):
        def send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
            pass

        def close(self):
            pass

    class MyTransportPlugin(TransportPlugin):
        prefix = 'http://'

        def get_adapter(self):
            return MyAdapter()

    plugin = MyTransportPlugin()
    adapter = plugin.get_adapter()
    assert isinstance(adapter, MyAdapter)
