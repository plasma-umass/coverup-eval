# file: tornado/auth.py:385-414
# asked: {"lines": [390, 391, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 403, 404, 405, 407, 408, 409, 411, 413, 414], "branches": [[400, 401], [400, 411], [401, 402], [401, 403], [403, 404], [403, 407], [407, 408], [407, 409]]}
# gained: {"lines": [390, 391, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 403, 404, 405, 407, 408, 409, 411, 413, 414], "branches": [[400, 401], [400, 411], [401, 402], [401, 403], [403, 404], [407, 408], [407, 409]]}

import pytest
from unittest.mock import Mock, patch
from tornado.web import RequestHandler
from tornado.auth import OAuthMixin

class TestOAuthMixin(OAuthMixin):
    _OAUTH_REQUEST_TOKEN_URL = "http://example.com/request_token"
    _OAUTH_VERSION = "1.0a"

    def _oauth_consumer_token(self):
        return {"key": "test_key", "secret": "test_secret"}

@pytest.fixture
def mock_request_handler():
    handler = Mock(spec=RequestHandler)
    handler.request = Mock()
    handler.request.full_url.return_value = "http://example.com/callback"
    return handler

def test_oauth_request_token_url_oob(mock_request_handler):
    mixin = TestOAuthMixin()
    mixin.__dict__['_OAUTH_VERSION'] = "1.0a"
    mixin.__dict__['request'] = mock_request_handler.request

    with patch('tornado.auth._oauth10a_signature', return_value=b'signature'):
        url = mixin._oauth_request_token_url(callback_uri="oob")
        assert "oauth_callback=oob" in url
        assert "oauth_signature=signature" in url

def test_oauth_request_token_url_with_callback(mock_request_handler):
    mixin = TestOAuthMixin()
    mixin.__dict__['_OAUTH_VERSION'] = "1.0a"
    mixin.__dict__['request'] = mock_request_handler.request

    with patch('tornado.auth._oauth10a_signature', return_value=b'signature'):
        url = mixin._oauth_request_token_url(callback_uri="/callback")
        assert "oauth_callback=http%3A%2F%2Fexample.com%2Fcallback" in url
        assert "oauth_signature=signature" in url

def test_oauth_request_token_url_with_extra_params(mock_request_handler):
    mixin = TestOAuthMixin()
    mixin.__dict__['_OAUTH_VERSION'] = "1.0a"
    mixin.__dict__['request'] = mock_request_handler.request

    extra_params = {"extra_param": "extra_value"}
    with patch('tornado.auth._oauth10a_signature', return_value=b'signature'):
        url = mixin._oauth_request_token_url(callback_uri="/callback", extra_params=extra_params)
        assert "extra_param=extra_value" in url
        assert "oauth_signature=signature" in url

def test_oauth_request_token_url_version_1_0(mock_request_handler):
    mixin = TestOAuthMixin()
    mixin.__dict__['_OAUTH_VERSION'] = "1.0"
    mixin.__dict__['request'] = mock_request_handler.request

    with patch('tornado.auth._oauth_signature', return_value=b'signature'):
        url = mixin._oauth_request_token_url()
        assert "oauth_signature=signature" in url
