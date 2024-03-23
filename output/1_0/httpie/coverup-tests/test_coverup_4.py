# file httpie/plugins/builtin.py:47-58
# lines [47, 48, 49, 50, 53, 58]
# branches []

import pytest
from httpie.plugins.builtin import DigestAuthPlugin
from requests.auth import HTTPDigestAuth

@pytest.fixture
def digest_auth_plugin():
    return DigestAuthPlugin()

def test_digest_auth_plugin_get_auth(digest_auth_plugin):
    username = 'testuser'
    password = 'testpass'
    auth = digest_auth_plugin.get_auth(username, password)
    assert isinstance(auth, HTTPDigestAuth), "The auth object should be an instance of HTTPDigestAuth"
    assert auth.username == username, "The username should be set correctly in the auth object"
    assert auth.password == password, "The password should be set correctly in the auth object"
