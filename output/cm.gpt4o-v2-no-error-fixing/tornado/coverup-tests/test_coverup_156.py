# file: tornado/auth.py:466-471
# asked: {"lines": [471], "branches": []}
# gained: {"lines": [471], "branches": []}

import pytest
from tornado.auth import OAuthMixin

class TestOAuthMixin(OAuthMixin):
    def _oauth_consumer_token(self):
        return super()._oauth_consumer_token()

def test_oauth_consumer_token_not_implemented():
    mixin = TestOAuthMixin()
    with pytest.raises(NotImplementedError):
        mixin._oauth_consumer_token()
