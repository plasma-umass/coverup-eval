# file tornado/auth.py:440-464
# lines [441, 442, 443, 444, 445, 446, 447, 448, 449, 451, 452, 454, 455, 456, 459, 460, 463, 464]
# branches ['451->452', '451->454', '454->455', '454->459']

import pytest
from tornado.auth import OAuthMixin
from unittest.mock import Mock
import time
import uuid
import binascii
import urllib.parse

class DummyOAuthMixin(OAuthMixin):
    _OAUTH_ACCESS_TOKEN_URL = "http://example.com/access_token"
    def _oauth_consumer_token(self):
        return {"key": "dummy_consumer_key", "secret": "dummy_consumer_secret"}

def _oauth10a_signature(consumer_token, method, url, parameters, token):
    return "dummy_signature_10a"

def _oauth_signature(consumer_token, method, url, parameters, token):
    return "dummy_signature"

@pytest.fixture
def oauth_mixin(mocker):
    mixin = DummyOAuthMixin()
    mocker.patch.object(mixin, '_oauth_consumer_token', return_value={"key": "dummy_consumer_key", "secret": "dummy_consumer_secret"})
    mocker.patch('tornado.auth._oauth10a_signature', _oauth10a_signature)
    mocker.patch('tornado.auth._oauth_signature', _oauth_signature)
    return mixin

def test_oauth_access_token_url_with_verifier(oauth_mixin):
    request_token = {"key": "dummy_request_key", "verifier": "dummy_verifier"}
    url = oauth_mixin._oauth_access_token_url(request_token)
    assert "oauth_verifier=dummy_verifier" in url
    assert "oauth_signature=dummy_signature_10a" in url

def test_oauth_access_token_url_without_verifier(oauth_mixin):
    request_token = {"key": "dummy_request_key"}
    url = oauth_mixin._oauth_access_token_url(request_token)
    assert "oauth_verifier=" not in url
    assert "oauth_signature=dummy_signature" in url

def test_oauth_access_token_url_with_oauth_version_1_0(oauth_mixin):
    request_token = {"key": "dummy_request_key"}
    setattr(oauth_mixin, "_OAUTH_VERSION", "1.0")
    url = oauth_mixin._oauth_access_token_url(request_token)
    assert "oauth_signature=dummy_signature" in url
