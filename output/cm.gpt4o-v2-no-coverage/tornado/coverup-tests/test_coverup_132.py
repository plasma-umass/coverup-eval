# file: tornado/auth.py:466-471
# asked: {"lines": [466, 471], "branches": []}
# gained: {"lines": [466, 471], "branches": []}

import pytest
from tornado.auth import OAuthMixin

class TestOAuthMixin(OAuthMixin):
    def _oauth_consumer_token(self):
        return {"key": "test_key", "secret": "test_secret"}

def test_oauth_consumer_token_not_implemented():
    mixin = OAuthMixin()
    with pytest.raises(NotImplementedError):
        mixin._oauth_consumer_token()

def test_oauth_consumer_token_implemented():
    mixin = TestOAuthMixin()
    token = mixin._oauth_consumer_token()
    assert token == {"key": "test_key", "secret": "test_secret"}
