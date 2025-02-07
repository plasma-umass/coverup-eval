# file: tornado/auth.py:466-471
# asked: {"lines": [466, 471], "branches": []}
# gained: {"lines": [466, 471], "branches": []}

import pytest
from tornado.auth import OAuthMixin
from typing import Dict, Any

class TestOAuthMixin(OAuthMixin):
    def _oauth_consumer_token(self) -> Dict[str, Any]:
        return {"key": "dummy_key", "secret": "dummy_secret"}

def test_oauth_consumer_token_not_implemented():
    mixin = OAuthMixin()
    with pytest.raises(NotImplementedError):
        mixin._oauth_consumer_token()

def test_oauth_consumer_token_implemented():
    mixin = TestOAuthMixin()
    token = mixin._oauth_consumer_token()
    assert token == {"key": "dummy_key", "secret": "dummy_secret"}
