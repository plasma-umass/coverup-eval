# file tornado/auth.py:440-464
# lines [441, 442, 443, 444, 445, 446, 447, 448, 449, 451, 452, 454, 455, 456, 459, 460, 463, 464]
# branches ['451->452', '451->454', '454->455', '454->459']

import pytest
from unittest import mock
from tornado.auth import OAuthMixin
import time
import binascii
import uuid
import urllib.parse
from tornado import escape

class TestOAuthMixin(OAuthMixin):
    _OAUTH_ACCESS_TOKEN_URL = "http://example.com/access_token"
    
    def _oauth_consumer_token(self):
        return {"key": "consumer_key", "secret": "consumer_secret"}

@pytest.fixture
def oauth_mixin():
    return TestOAuthMixin()

def test_oauth_access_token_url_with_verifier(oauth_mixin, mocker):
    request_token = {"key": "request_key", "verifier": "verifier_value", "secret": "request_secret"}
    
    mocker.patch('time.time', return_value=1234567890)
    mocker.patch('uuid.uuid4', return_value=uuid.UUID(int=0))
    
    url = oauth_mixin._oauth_access_token_url(request_token)
    
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    
    assert query_params["oauth_consumer_key"] == ["consumer_key"]
    assert query_params["oauth_token"] == ["request_key"]
    assert query_params["oauth_signature_method"] == ["HMAC-SHA1"]
    assert query_params["oauth_timestamp"] == ["1234567890"]
    assert query_params["oauth_nonce"] == ["00000000000000000000000000000000"]
    assert query_params["oauth_version"] == ["1.0"]
    assert query_params["oauth_verifier"] == ["verifier_value"]
    assert "oauth_signature" in query_params

def test_oauth_access_token_url_without_verifier(oauth_mixin, mocker):
    request_token = {"key": "request_key", "secret": "request_secret"}
    
    mocker.patch('time.time', return_value=1234567890)
    mocker.patch('uuid.uuid4', return_value=uuid.UUID(int=0))
    
    url = oauth_mixin._oauth_access_token_url(request_token)
    
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    
    assert query_params["oauth_consumer_key"] == ["consumer_key"]
    assert query_params["oauth_token"] == ["request_key"]
    assert query_params["oauth_signature_method"] == ["HMAC-SHA1"]
    assert query_params["oauth_timestamp"] == ["1234567890"]
    assert query_params["oauth_nonce"] == ["00000000000000000000000000000000"]
    assert query_params["oauth_version"] == ["1.0"]
    assert "oauth_signature" in query_params
