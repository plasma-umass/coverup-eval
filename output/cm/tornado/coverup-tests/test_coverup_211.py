# file tornado/auth.py:466-471
# lines [466, 471]
# branches []

import pytest
from tornado.auth import OAuthMixin

class DummyOAuthMixin(OAuthMixin):
    def _oauth_consumer_token(self):
        return {'key': 'dummy_key', 'secret': 'dummy_secret'}

@pytest.fixture
def dummy_oauth_mixin():
    return DummyOAuthMixin()

def test_oauth_consumer_token(dummy_oauth_mixin):
    token = dummy_oauth_mixin._oauth_consumer_token()
    assert token['key'] == 'dummy_key'
    assert token['secret'] == 'dummy_secret'

def test_not_implemented_oauth_consumer_token():
    with pytest.raises(NotImplementedError):
        OAuthMixin()._oauth_consumer_token()
