# file tornado/auth.py:497-530
# lines [509, 510, 511, 512, 513, 514, 515, 516, 518, 519, 520, 521, 522, 523, 526, 527, 529, 530]
# branches ['521->522', '521->526']

import pytest
from unittest.mock import patch, MagicMock
import time
import binascii
import uuid
from tornado.auth import OAuthMixin
from tornado.escape import to_basestring

class TestOAuthMixin(OAuthMixin):
    def _oauth_consumer_token(self):
        return {"key": "consumer_key", "secret": "consumer_secret"}

@pytest.fixture
def oauth_mixin():
    return TestOAuthMixin()

@patch('tornado.auth._oauth10a_signature')
@patch('tornado.auth._oauth_signature')
@patch('time.time', return_value=1234567890)
@patch('uuid.uuid4', return_value=uuid.UUID('12345678123456781234567812345678'))
def test_oauth_request_parameters(mock_uuid, mock_time, mock_oauth_signature, mock_oauth10a_signature, oauth_mixin):
    url = "http://example.com/resource"
    access_token = {"key": "access_key", "secret": "access_secret"}
    parameters = {"param1": "value1"}
    method = "POST"

    # Mock the signatures
    mock_oauth10a_signature.return_value = b"signature10a"
    mock_oauth_signature.return_value = b"signature"

    # Test for OAuth 1.0a
    oauth_mixin._OAUTH_VERSION = "1.0a"
    result = oauth_mixin._oauth_request_parameters(url, access_token, parameters, method)
    assert result["oauth_signature"] == to_basestring(b"signature10a")
    mock_oauth10a_signature.assert_called_once()

    # Test for OAuth 1.0
    oauth_mixin._OAUTH_VERSION = "1.0"
    result = oauth_mixin._oauth_request_parameters(url, access_token, parameters, method)
    assert result["oauth_signature"] == to_basestring(b"signature")
    mock_oauth_signature.assert_called_once()

    # Clean up
    del oauth_mixin._OAUTH_VERSION
