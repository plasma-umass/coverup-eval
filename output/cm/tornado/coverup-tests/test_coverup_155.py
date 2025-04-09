# file tornado/auth.py:541-552
# lines [541, 542]
# branches []

import pytest
from tornado.auth import OAuth2Mixin
from unittest.mock import Mock

class ExampleOAuth2Mixin(OAuth2Mixin):
    _OAUTH_AUTHORIZE_URL = "https://example.com/authorize"
    _OAUTH_ACCESS_TOKEN_URL = "https://example.com/access_token"

@pytest.fixture
def oauth2_mixin():
    return ExampleOAuth2Mixin()

def test_oauth2_mixin_authorize_url(oauth2_mixin):
    assert oauth2_mixin._OAUTH_AUTHORIZE_URL == "https://example.com/authorize"

def test_oauth2_mixin_access_token_url(oauth2_mixin):
    assert oauth2_mixin._OAUTH_ACCESS_TOKEN_URL == "https://example.com/access_token"
