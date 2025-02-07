# file: tornado/auth.py:440-464
# asked: {"lines": [441, 442, 443, 444, 445, 446, 447, 448, 449, 451, 452, 454, 455, 456, 459, 460, 463, 464], "branches": [[451, 452], [451, 454], [454, 455], [454, 459]]}
# gained: {"lines": [441, 442, 443, 444, 445, 446, 447, 448, 449, 451, 452, 454, 455, 456, 459, 460, 463, 464], "branches": [[451, 452], [451, 454], [454, 455], [454, 459]]}

import pytest
import time
import binascii
import uuid
from tornado import escape
from unittest.mock import patch
from typing import Any, Dict
from tornado.auth import OAuthMixin, _oauth10a_signature, _oauth_signature

class TestOAuthMixin(OAuthMixin):
    _OAUTH_ACCESS_TOKEN_URL = "http://example.com/access_token"
    _OAUTH_VERSION = "1.0a"
    
    def _oauth_consumer_token(self) -> Dict[str, Any]:
        return {"key": "test_consumer_key", "secret": "test_consumer_secret"}

@pytest.fixture
def oauth_mixin():
    return TestOAuthMixin()

def test_oauth_access_token_url_with_verifier(oauth_mixin):
    request_token = {"key": "test_request_key", "secret": "test_request_secret", "verifier": "test_verifier"}
    with patch('time.time', return_value=1234567890), \
         patch('uuid.uuid4', return_value=uuid.UUID(int=0)):
        url = oauth_mixin._oauth_access_token_url(request_token)
        assert url.startswith(oauth_mixin._OAUTH_ACCESS_TOKEN_URL)
        assert "oauth_verifier=test_verifier" in url

def test_oauth_access_token_url_without_verifier(oauth_mixin):
    request_token = {"key": "test_request_key", "secret": "test_request_secret"}
    with patch('time.time', return_value=1234567890), \
         patch('uuid.uuid4', return_value=uuid.UUID(int=0)):
        url = oauth_mixin._oauth_access_token_url(request_token)
        assert url.startswith(oauth_mixin._OAUTH_ACCESS_TOKEN_URL)
        assert "oauth_verifier" not in url

def test_oauth_access_token_url_oauth_version_1_0a(oauth_mixin, mocker):
    request_token = {"key": "test_request_key", "secret": "test_request_secret"}
    mocker.patch.object(oauth_mixin.__class__, '_OAUTH_VERSION', '1.0a')
    with patch('time.time', return_value=1234567890), \
         patch('uuid.uuid4', return_value=uuid.UUID(int=0)), \
         patch('tornado.auth._oauth10a_signature', return_value=b'test_signature'):
        url = oauth_mixin._oauth_access_token_url(request_token)
        assert url.startswith(oauth_mixin._OAUTH_ACCESS_TOKEN_URL)
        assert "oauth_signature=test_signature" in url

def test_oauth_access_token_url_oauth_version_1_0(oauth_mixin, mocker):
    request_token = {"key": "test_request_key", "secret": "test_request_secret"}
    mocker.patch.object(oauth_mixin.__class__, '_OAUTH_VERSION', '1.0')
    with patch('time.time', return_value=1234567890), \
         patch('uuid.uuid4', return_value=uuid.UUID(int=0)), \
         patch('tornado.auth._oauth_signature', return_value=b'test_signature'):
        url = oauth_mixin._oauth_access_token_url(request_token)
        assert url.startswith(oauth_mixin._OAUTH_ACCESS_TOKEN_URL)
        assert "oauth_signature=test_signature" in url
