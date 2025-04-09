# file: httpie/plugins/base.py:70-91
# asked: {"lines": [70, 71, 83, 85, 91], "branches": []}
# gained: {"lines": [70, 71, 83, 85, 91], "branches": []}

import pytest
from httpie.plugins.base import BasePlugin, TransportPlugin

class TestTransportPlugin:
    def test_transport_plugin_prefix(self):
        class MyTransportPlugin(TransportPlugin):
            prefix = 'http://'

            def get_adapter(self):
                return 'adapter_instance'

        plugin = MyTransportPlugin()
        assert plugin.prefix == 'http://'
        assert plugin.get_adapter() == 'adapter_instance'

    def test_transport_plugin_not_implemented_error(self):
        class MyTransportPlugin(TransportPlugin):
            prefix = 'http://'

        plugin = MyTransportPlugin()
        with pytest.raises(NotImplementedError):
            plugin.get_adapter()
