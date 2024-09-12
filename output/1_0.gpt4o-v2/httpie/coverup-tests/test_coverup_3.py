# file: httpie/plugins/builtin.py:47-58
# asked: {"lines": [47, 48, 49, 50, 53, 58], "branches": []}
# gained: {"lines": [47, 48, 49, 50, 53, 58], "branches": []}

import pytest
import requests.auth
from httpie.plugins.builtin import DigestAuthPlugin

def test_digest_auth_plugin_get_auth():
    plugin = DigestAuthPlugin()
    username = 'user'
    password = 'pass'
    auth = plugin.get_auth(username, password)
    
    assert isinstance(auth, requests.auth.HTTPDigestAuth)
    assert auth.username == username
    assert auth.password == password
