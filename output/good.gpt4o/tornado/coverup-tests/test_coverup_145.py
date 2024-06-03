# file tornado/auth.py:466-471
# lines [466, 471]
# branches []

import pytest
from tornado.auth import OAuthMixin

def test_oauth_consumer_token_not_implemented():
    class TestOAuthMixin(OAuthMixin):
        pass

    mixin = TestOAuthMixin()
    with pytest.raises(NotImplementedError):
        mixin._oauth_consumer_token()
