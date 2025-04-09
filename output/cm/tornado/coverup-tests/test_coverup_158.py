# file tornado/auth.py:273-289
# lines [273, 274]
# branches []

import pytest
from tornado.auth import OAuthMixin
from unittest.mock import Mock

class DummyOAuthMixin(OAuthMixin):
    _OAUTH_AUTHORIZE_URL = "http://example.com/authorize"
    _OAUTH_ACCESS_TOKEN_URL = "http://example.com/access_token"
    _OAUTH_VERSION = "1.0"
    _OAUTH_NO_CALLBACKS = False

    def _oauth_get_user_future(self, access_token):
        pass

    def _oauth_consumer_token(self):
        pass

@pytest.fixture
def dummy_oauth_mixin():
    return DummyOAuthMixin()

def test_oauth_mixin_attributes(dummy_oauth_mixin):
    assert hasattr(dummy_oauth_mixin, '_OAUTH_AUTHORIZE_URL')
    assert hasattr(dummy_oauth_mixin, '_OAUTH_ACCESS_TOKEN_URL')
    assert hasattr(dummy_oauth_mixin, '_OAUTH_VERSION')
    assert hasattr(dummy_oauth_mixin, '_OAUTH_NO_CALLBACKS')
    assert dummy_oauth_mixin._OAUTH_AUTHORIZE_URL == "http://example.com/authorize"
    assert dummy_oauth_mixin._OAUTH_ACCESS_TOKEN_URL == "http://example.com/access_token"
    assert dummy_oauth_mixin._OAUTH_VERSION == "1.0"
    assert dummy_oauth_mixin._OAUTH_NO_CALLBACKS is False
