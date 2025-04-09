# file: tornado/auth.py:497-530
# asked: {"lines": [509, 510, 511, 512, 513, 514, 515, 516, 518, 519, 520, 521, 522, 523, 526, 527, 529, 530], "branches": [[521, 522], [521, 526]]}
# gained: {"lines": [509, 510, 511, 512, 513, 514, 515, 516, 518, 519, 520, 521, 522, 523, 526, 527, 529, 530], "branches": [[521, 522], [521, 526]]}

import pytest
import time
import binascii
import uuid
from tornado.auth import OAuthMixin
from tornado.escape import to_basestring

class MockOAuthMixin(OAuthMixin):
    def _oauth_consumer_token(self):
        return {"key": "consumer_key", "secret": "consumer_secret"}

def mock_oauth10a_signature(consumer_token, method, url, args, access_token):
    return "mock_signature_10a"

def mock_oauth_signature(consumer_token, method, url, args, access_token):
    return "mock_signature"

@pytest.fixture
def mock_oauth_mixin(monkeypatch):
    mixin = MockOAuthMixin()
    monkeypatch.setattr("tornado.auth._oauth10a_signature", mock_oauth10a_signature)
    monkeypatch.setattr("tornado.auth._oauth_signature", mock_oauth_signature)
    return mixin

def test_oauth_request_parameters_10a(mock_oauth_mixin):
    url = "http://example.com"
    access_token = {"key": "access_key", "secret": "access_secret"}
    parameters = {"param1": "value1"}
    method = "POST"
    
    result = mock_oauth_mixin._oauth_request_parameters(url, access_token, parameters, method)
    
    assert result["oauth_consumer_key"] == "consumer_key"
    assert result["oauth_token"] == "access_key"
    assert result["oauth_signature_method"] == "HMAC-SHA1"
    assert "oauth_timestamp" in result
    assert "oauth_nonce" in result
    assert result["oauth_version"] == "1.0"
    assert result["oauth_signature"] == "mock_signature_10a"

def test_oauth_request_parameters_1_0(mock_oauth_mixin, monkeypatch):
    # Ensure the mixin has the _OAUTH_VERSION attribute
    mock_oauth_mixin._OAUTH_VERSION = "1.0"
    
    url = "http://example.com"
    access_token = {"key": "access_key", "secret": "access_secret"}
    parameters = {"param1": "value1"}
    method = "POST"
    
    result = mock_oauth_mixin._oauth_request_parameters(url, access_token, parameters, method)
    
    assert result["oauth_consumer_key"] == "consumer_key"
    assert result["oauth_token"] == "access_key"
    assert result["oauth_signature_method"] == "HMAC-SHA1"
    assert "oauth_timestamp" in result
    assert "oauth_nonce" in result
    assert result["oauth_version"] == "1.0"
    assert result["oauth_signature"] == "mock_signature"
