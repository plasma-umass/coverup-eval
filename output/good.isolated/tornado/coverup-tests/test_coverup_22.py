# file tornado/auth.py:932-1037
# lines [932, 938, 985, 986, 987, 988, 989, 990, 993, 994, 996, 997, 999, 1000, 1002, 1003, 1004, 1005, 1007, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1020, 1021, 1023, 1024, 1025, 1031, 1032, 1033, 1034, 1037]
# branches ['996->997', '996->999', '1020->1021', '1020->1023', '1024->1025', '1024->1031']

import pytest
from tornado.auth import FacebookGraphMixin
from tornado.httpclient import AsyncHTTPClient, HTTPResponse
from unittest.mock import Mock
import json
import hmac
import hashlib

class TestFacebookGraphMixin:
    @pytest.mark.asyncio
    async def test_get_authenticated_user(self, mocker):
        # Mocking the necessary parts of FacebookGraphMixin
        mixin = FacebookGraphMixin()
        mixin.get_auth_http_client = Mock(return_value=AsyncHTTPClient())
        mixin.facebook_request = Mock()

        # Mocking the HTTP client response
        token_response = {
            "access_token": "mock_access_token",
            "expires_in": "3600"
        }
        http_response = HTTPResponse(Mock(), 200, buffer=Mock())
        http_response.buffer.read = Mock(return_value=json.dumps(token_response).encode())
        mocker.patch.object(AsyncHTTPClient, 'fetch', return_value=http_response)

        # Mocking the facebook_request method
        user_info = {
            "id": "12345",
            "name": "Test User",
            "first_name": "Test",
            "last_name": "User",
            "locale": "en_US",
            "picture": "http://example.com/picture",
            "link": "http://example.com/profile"
        }
        mixin.facebook_request.return_value = user_info

        # Call the method under test
        user = await mixin.get_authenticated_user(
            redirect_uri='http://example.com/auth/facebookgraph/',
            client_id='mock_client_id',
            client_secret='mock_client_secret',
            code='mock_code'
        )

        # Assertions to ensure the method behaves as expected
        assert user is not None
        assert user['access_token'] == 'mock_access_token'
        assert user['session_expires'] == '3600'
        assert user['id'] == '12345'
        assert user['name'] == 'Test User'
        assert user['first_name'] == 'Test'
        assert user['last_name'] == 'User'
        assert user['locale'] == 'en_US'
        assert user['picture'] == 'http://example.com/picture'
        assert user['link'] == 'http://example.com/profile'

        # Verify that the appsecret_proof was generated correctly
        appsecret_proof = hmac.new(
            key='mock_client_secret'.encode("utf8"),
            msg='mock_access_token'.encode("utf8"),
            digestmod=hashlib.sha256
        ).hexdigest()
        mixin.facebook_request.assert_called_with(
            path="/me",
            access_token='mock_access_token',
            appsecret_proof=appsecret_proof,
            fields="id,name,first_name,last_name,locale,picture,link"
        )
