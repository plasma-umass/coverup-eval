# file httpie/plugins/base.py:56-67
# lines [67]
# branches []

import pytest
from httpie.plugins.base import AuthPlugin

def test_auth_plugin_not_implemented_error():
    plugin = AuthPlugin()
    with pytest.raises(NotImplementedError):
        plugin.get_auth()

