# file: httpie/plugins/base.py:56-67
# asked: {"lines": [56, 67], "branches": []}
# gained: {"lines": [56, 67], "branches": []}

import pytest
from httpie.plugins.base import AuthPlugin
from requests.auth import AuthBase

def test_auth_plugin_get_auth_not_implemented():
    plugin = AuthPlugin()
    with pytest.raises(NotImplementedError):
        plugin.get_auth(username="user", password="pass")
