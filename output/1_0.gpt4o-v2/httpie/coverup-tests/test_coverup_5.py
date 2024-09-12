# file: httpie/plugins/builtin.py:37-44
# asked: {"lines": [37, 38, 39, 40, 43, 44], "branches": []}
# gained: {"lines": [37, 38, 39, 40, 43, 44], "branches": []}

import pytest
from httpie.plugins.builtin import BasicAuthPlugin
from requests.auth import HTTPBasicAuth

def test_basic_auth_plugin_get_auth():
    plugin = BasicAuthPlugin()
    username = 'user'
    password = 'pass'
    auth = plugin.get_auth(username, password)
    
    assert isinstance(auth, HTTPBasicAuth)
    assert auth.username == username
    assert auth.password == password
