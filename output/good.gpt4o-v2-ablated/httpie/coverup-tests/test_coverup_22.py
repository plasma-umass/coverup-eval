# file: httpie/plugins/base.py:70-91
# asked: {"lines": [70, 71, 83, 85, 91], "branches": []}
# gained: {"lines": [70, 71, 83, 85], "branches": []}

import pytest
from httpie.plugins.base import BasePlugin

class TransportPlugin(BasePlugin):
    """
    Requests transport adapter docs:

        <https://requests.readthedocs.io/en/latest/user/advanced/#transport-adapters>

    See httpie-unixsocket for an example transport plugin:

        <https://github.com/httpie/httpie-unixsocket>

    """

    # The URL prefix the adapter should be mount to.
    prefix = None

    def get_adapter(self):
        """
        Return a ``requests.adapters.BaseAdapter`` subclass instance to be
        mounted to ``self.prefix``.

        """
        raise NotImplementedError()

def test_transport_plugin_prefix():
    plugin = TransportPlugin()
    assert plugin.prefix is None

def test_transport_plugin_get_adapter():
    plugin = TransportPlugin()
    with pytest.raises(NotImplementedError):
        plugin.get_adapter()
