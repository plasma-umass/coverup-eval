# file tornado/auth.py:273-289
# lines [273, 274]
# branches []

import pytest
from tornado.auth import OAuthMixin

class TestOAuthMixin(OAuthMixin):
    _OAUTH_AUTHORIZE_URL = "http://example.com/authorize"
    _OAUTH_ACCESS_TOKEN_URL = "http://example.com/access_token"
    _OAUTH_VERSION = "1.0a"
    _OAUTH_NO_CALLBACKS = False

    def _oauth_get_user_future(self, access_token):
        pass

    def _oauth_consumer_token(self):
        return {"key": "dummy_key", "secret": "dummy_secret"}

@pytest.fixture
def oauth_mixin():
    return TestOAuthMixin()

def test_oauth_mixin_attributes(oauth_mixin):
    assert oauth_mixin._OAUTH_AUTHORIZE_URL == "http://example.com/authorize"
    assert oauth_mixin._OAUTH_ACCESS_TOKEN_URL == "http://example.com/access_token"
    assert oauth_mixin._OAUTH_VERSION == "1.0a"
    assert oauth_mixin._OAUTH_NO_CALLBACKS is False

def test_oauth_mixin_methods(oauth_mixin):
    assert oauth_mixin._oauth_consumer_token() == {"key": "dummy_key", "secret": "dummy_secret"}
    assert oauth_mixin._oauth_get_user_future(None) is None
