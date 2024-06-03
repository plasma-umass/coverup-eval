# file tornado/auth.py:385-414
# lines [390, 391, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 403, 404, 405, 407, 408, 409, 411, 413, 414]
# branches ['400->401', '400->411', '401->402', '401->403', '403->404', '403->407', '407->408', '407->409']

import pytest
from unittest.mock import MagicMock, patch
from tornado.auth import OAuthMixin
from tornado.escape import utf8
import time
import binascii
import uuid
import urllib.parse

class TestOAuthMixin(OAuthMixin):
    _OAUTH_REQUEST_TOKEN_URL = "http://example.com/request_token"
    _OAUTH_VERSION = "1.0a"

    def _oauth_consumer_token(self):
        return {"key": "test_key", "secret": "test_secret"}

    @property
    def request(self):
        mock_request = MagicMock()
        mock_request.full_url.return_value = "http://example.com/"
        return mock_request

@pytest.fixture
def oauth_mixin():
    return TestOAuthMixin()

@patch('tornado.auth._oauth10a_signature', return_value='test_signature')
@patch('tornado.auth._oauth_signature', return_value='test_signature')
def test_oauth_request_token_url(mock_oauth10a_signature, mock_oauth_signature, oauth_mixin):
    # Test with callback_uri as "oob"
    url = oauth_mixin._oauth_request_token_url(callback_uri="oob")
    assert "oauth_callback=oob" in url
    assert "oauth_signature=test_signature" in url

    # Test with callback_uri as a valid URL
    url = oauth_mixin._oauth_request_token_url(callback_uri="/callback")
    assert "oauth_callback=http%3A%2F%2Fexample.com%2Fcallback" in url
    assert "oauth_signature=test_signature" in url

    # Test with extra_params
    extra_params = {"extra_param": "extra_value"}
    url = oauth_mixin._oauth_request_token_url(callback_uri="/callback", extra_params=extra_params)
    assert "extra_param=extra_value" in url
    assert "oauth_signature=test_signature" in url

    # Test with _OAUTH_VERSION not equal to "1.0a"
    oauth_mixin._OAUTH_VERSION = "1.0"
    url = oauth_mixin._oauth_request_token_url()
    assert "oauth_signature=test_signature" in url

    # Reset _OAUTH_VERSION to avoid side effects
    oauth_mixin._OAUTH_VERSION = "1.0a"
