# file tornado/auth.py:385-414
# lines [390, 391, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 403, 404, 405, 407, 408, 409, 411, 413, 414]
# branches ['400->401', '400->411', '401->402', '401->403', '403->404', '403->407', '407->408', '407->409']

import pytest
from unittest.mock import Mock
from tornado.auth import OAuthMixin
from tornado import escape
import time
import binascii
import uuid
import urllib.parse

# Mock the _oauth_consumer_token and _oauth_signature methods
class TestOAuthMixin(OAuthMixin):
    _OAUTH_REQUEST_TOKEN_URL = "http://example.com/request_token"

    def _oauth_consumer_token(self):
        return {"key": "test_consumer_key", "secret": "test_consumer_secret"}

    def _oauth_signature(self, consumer_token, method, url, parameters, token=None):
        return "test_signature"

# Mock the RequestHandler to be used in the OAuthMixin
class MockRequestHandler:
    def __init__(self):
        self.request = Mock()
        self.request.full_url = Mock(return_value="http://example.com/")

# Test function to cover lines 390-414
def test_oauth_request_token_url(mocker):
    mocker.patch('tornado.auth._oauth10a_signature', return_value='test_signature')
    mocker.patch('tornado.auth._oauth_signature', return_value='test_signature')

    mixin = TestOAuthMixin()
    mixin._OAUTH_VERSION = "1.0a"  # Set the OAuth version to 1.0a
    mixin.request = MockRequestHandler().request

    # Test with callback_uri and extra_params
    callback_uri = "callback"
    extra_params = {"extra": "param"}
    url = mixin._oauth_request_token_url(callback_uri=callback_uri, extra_params=extra_params)

    # Assertions to verify the URL is constructed correctly
    assert "oauth_consumer_key=test_consumer_key" in url
    assert "oauth_signature_method=HMAC-SHA1" in url
    assert "oauth_nonce=" in url
    assert "oauth_version=1.0" in url
    assert "oauth_callback=http%3A%2F%2Fexample.com%2Fcallback" in url
    assert "extra=param" in url
    assert "oauth_signature=test_signature" in url

    # Test with callback_uri set to 'oob'
    callback_uri = "oob"
    url = mixin._oauth_request_token_url(callback_uri=callback_uri)
    assert "oauth_callback=oob" in url

    # Test without callback_uri and extra_params
    url = mixin._oauth_request_token_url()
    assert "oauth_callback=" not in url
    assert "extra=" not in url

    # Test with OAuth version other than 1.0a
    mixin._OAUTH_VERSION = "2.0"
    url = mixin._oauth_request_token_url()
    assert "oauth_signature=test_signature" in url
