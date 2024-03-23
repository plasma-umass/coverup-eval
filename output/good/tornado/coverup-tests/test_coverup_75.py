# file tornado/auth.py:497-530
# lines [497, 501, 502, 509, 510, 511, 512, 513, 514, 515, 516, 518, 519, 520, 521, 522, 523, 526, 527, 529, 530]
# branches ['521->522', '521->526']

import pytest
from tornado.auth import OAuthMixin
from tornado import escape
import time
import binascii
import uuid
from unittest.mock import patch

# Assuming _oauth_consumer_token and _oauth_signature are defined elsewhere in tornado.auth
# and need to be mocked for testing purposes.

class DummyOAuthMixin(OAuthMixin):
    def _oauth_consumer_token(self):
        return {"key": "dummy_consumer_key", "secret": "dummy_consumer_secret"}

# Mocking the _oauth_signature function
def mock_oauth_signature(consumer_token, method, url, args, access_token):
    return "dummy_signature"

# Mocking the _oauth10a_signature function
def mock_oauth10a_signature(consumer_token, method, url, args, access_token):
    return "dummy_10a_signature"

@pytest.fixture
def oauth_mixin():
    return DummyOAuthMixin()

@pytest.fixture
def access_token():
    return {"key": "dummy_access_token", "secret": "dummy_access_secret"}

@pytest.fixture
def parameters():
    return {"extra_param": "extra_value"}

# Test for OAuth version 1.0
def test_oauth_request_parameters_v1(oauth_mixin, access_token, parameters):
    with patch('tornado.auth._oauth_signature', mock_oauth_signature):
        oauth_mixin._OAUTH_VERSION = "1.0"
        params = oauth_mixin._oauth_request_parameters(
            "http://dummyurl.com", access_token, parameters, "POST"
        )
        assert params["oauth_consumer_key"] == "dummy_consumer_key"
        assert params["oauth_token"] == "dummy_access_token"
        assert params["oauth_signature"] == "dummy_signature"
        assert params["oauth_signature_method"] == "HMAC-SHA1"
        assert params["oauth_version"] == "1.0"
        assert "extra_param" not in params  # Corrected assertion

# Test for OAuth version 1.0a
def test_oauth_request_parameters_v1a(oauth_mixin, access_token, parameters):
    with patch('tornado.auth._oauth10a_signature', mock_oauth10a_signature):
        oauth_mixin._OAUTH_VERSION = "1.0a"
        params = oauth_mixin._oauth_request_parameters(
            "http://dummyurl.com", access_token, parameters, "POST"
        )
        assert params["oauth_consumer_key"] == "dummy_consumer_key"
        assert params["oauth_token"] == "dummy_access_token"
        assert params["oauth_signature"] == "dummy_10a_signature"
        assert params["oauth_signature_method"] == "HMAC-SHA1"
        assert params["oauth_version"] == "1.0"
        assert "extra_param" not in params  # Corrected assertion
