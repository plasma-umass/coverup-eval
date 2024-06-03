# file tornado/auth.py:541-552
# lines [541, 542]
# branches []

import pytest
from tornado.auth import OAuth2Mixin

def test_oauth2mixin_class_attributes():
    class TestOAuth2Mixin(OAuth2Mixin):
        _OAUTH_AUTHORIZE_URL = "https://example.com/authorize"
        _OAUTH_ACCESS_TOKEN_URL = "https://example.com/token"

    mixin = TestOAuth2Mixin()
    assert hasattr(mixin, '_OAUTH_AUTHORIZE_URL')
    assert hasattr(mixin, '_OAUTH_ACCESS_TOKEN_URL')
    assert mixin._OAUTH_AUTHORIZE_URL == "https://example.com/authorize"
    assert mixin._OAUTH_ACCESS_TOKEN_URL == "https://example.com/token"
