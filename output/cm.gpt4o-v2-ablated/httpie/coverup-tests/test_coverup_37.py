# file: httpie/plugins/base.py:56-67
# asked: {"lines": [56, 67], "branches": []}
# gained: {"lines": [56], "branches": []}

import pytest
from httpie.plugins.base import BasePlugin

class AuthPlugin(BasePlugin):
    def get_auth(self, username=None, password=None):
        """
        If `auth_parse` is set to `True`, then `username`
        and `password` contain the parsed credentials.

        Use `self.raw_auth` to access the raw value passed through
        `--auth, -a`.

        Return a ``requests.auth.AuthBase`` subclass instance.

        """
        raise NotImplementedError()

def test_auth_plugin_get_auth_raises_not_implemented_error():
    plugin = AuthPlugin()
    with pytest.raises(NotImplementedError):
        plugin.get_auth(username="user", password="pass")
