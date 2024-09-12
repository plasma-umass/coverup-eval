# file: tornado/auth.py:385-414
# asked: {"lines": [390, 391, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 403, 404, 405, 407, 408, 409, 411, 413, 414], "branches": [[400, 401], [400, 411], [401, 402], [401, 403], [403, 404], [403, 407], [407, 408], [407, 409]]}
# gained: {"lines": [390, 391, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 403, 404, 405, 407, 408, 409, 413, 414], "branches": [[400, 401], [401, 402], [401, 403], [403, 404], [403, 407], [407, 408], [407, 409]]}

import pytest
import time
import binascii
import uuid
import urllib.parse
from typing import Optional, Dict, Any
from tornado.escape import to_basestring
from tornado.web import RequestHandler
from tornado.auth import OAuthMixin
from unittest.mock import MagicMock, patch

class MockRequestHandler(RequestHandler, OAuthMixin):
    _OAUTH_REQUEST_TOKEN_URL = "http://example.com/request_token"
    _OAUTH_VERSION = "1.0a"

    def _oauth_consumer_token(self):
        return {"key": "test_key", "secret": "test_secret"}

@pytest.fixture
def mock_handler():
    return MockRequestHandler(MagicMock(), MagicMock())

def test_oauth_request_token_url_no_callback_no_extra_params(mock_handler):
    with patch('time.time', return_value=1234567890), \
         patch('uuid.uuid4', return_value=uuid.UUID(int=0)), \
         patch('tornado.escape.to_basestring', side_effect=lambda x: x):
        url = mock_handler._oauth_request_token_url()
        assert url.startswith("http://example.com/request_token?")
        assert "oauth_consumer_key=test_key" in url
        assert "oauth_signature_method=HMAC-SHA1" in url
        assert "oauth_timestamp=1234567890" in url
        assert "oauth_nonce=00000000000000000000000000000000" in url
        assert "oauth_version=1.0" in url
        assert "oauth_signature=" in url

def test_oauth_request_token_url_with_callback(mock_handler):
    with patch('time.time', return_value=1234567890), \
         patch('uuid.uuid4', return_value=uuid.UUID(int=0)), \
         patch('tornado.escape.to_basestring', side_effect=lambda x: x):
        mock_handler.request.full_url = MagicMock(return_value="http://example.com/")
        url = mock_handler._oauth_request_token_url(callback_uri="callback")
        assert url.startswith("http://example.com/request_token?")
        assert "oauth_consumer_key=test_key" in url
        assert "oauth_signature_method=HMAC-SHA1" in url
        assert "oauth_timestamp=1234567890" in url
        assert "oauth_nonce=00000000000000000000000000000000" in url
        assert "oauth_version=1.0" in url
        assert "oauth_callback=http%3A%2F%2Fexample.com%2Fcallback" in url
        assert "oauth_signature=" in url

def test_oauth_request_token_url_with_oob_callback(mock_handler):
    with patch('time.time', return_value=1234567890), \
         patch('uuid.uuid4', return_value=uuid.UUID(int=0)), \
         patch('tornado.escape.to_basestring', side_effect=lambda x: x):
        url = mock_handler._oauth_request_token_url(callback_uri="oob")
        assert url.startswith("http://example.com/request_token?")
        assert "oauth_consumer_key=test_key" in url
        assert "oauth_signature_method=HMAC-SHA1" in url
        assert "oauth_timestamp=1234567890" in url
        assert "oauth_nonce=00000000000000000000000000000000" in url
        assert "oauth_version=1.0" in url
        assert "oauth_callback=oob" in url
        assert "oauth_signature=" in url

def test_oauth_request_token_url_with_extra_params(mock_handler):
    with patch('time.time', return_value=1234567890), \
         patch('uuid.uuid4', return_value=uuid.UUID(int=0)), \
         patch('tornado.escape.to_basestring', side_effect=lambda x: x):
        extra_params = {"scope": "read"}
        url = mock_handler._oauth_request_token_url(extra_params=extra_params)
        assert url.startswith("http://example.com/request_token?")
        assert "oauth_consumer_key=test_key" in url
        assert "oauth_signature_method=HMAC-SHA1" in url
        assert "oauth_timestamp=1234567890" in url
        assert "oauth_nonce=00000000000000000000000000000000" in url
        assert "oauth_version=1.0" in url
        assert "scope=read" in url
        assert "oauth_signature=" in url
