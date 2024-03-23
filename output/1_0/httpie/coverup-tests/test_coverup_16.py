# file httpie/plugins/builtin.py:37-44
# lines [44]
# branches []

import pytest
from httpie.plugins.builtin import BasicAuthPlugin
from requests.auth import HTTPBasicAuth

class TestBasicAuthPlugin:
    def test_get_auth_executes_line_44(self):
        # Setup
        username = 'user'
        password = 'pass'
        basic_auth_plugin = BasicAuthPlugin()

        # Exercise
        auth = basic_auth_plugin.get_auth(username, password)

        # Verify
        assert isinstance(auth, HTTPBasicAuth)
        assert auth.username == username
        assert auth.password == password

        # No cleanup necessary as no external resources or state changes are involved
