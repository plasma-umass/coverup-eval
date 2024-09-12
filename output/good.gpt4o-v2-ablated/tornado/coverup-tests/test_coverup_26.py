# file: tornado/auth.py:610-664
# asked: {"lines": [610, 613, 614, 650, 651, 652, 653, 655, 656, 657, 658, 659, 660, 663, 664], "branches": [[651, 652], [651, 655], [655, 656], [655, 657], [658, 659], [658, 663]]}
# gained: {"lines": [610, 613, 614], "branches": []}

import pytest
from unittest.mock import AsyncMock, patch
from tornado.escape import json_decode
from tornado.auth import OAuth2Mixin
import urllib.parse

class TestOAuth2Mixin:
    @pytest.fixture
    def mixin(self):
        class TestHandler(OAuth2Mixin):
            def get_auth_http_client(self):
                return AsyncMock()
        return TestHandler()

    @pytest.mark.asyncio
    async def test_oauth2_request_with_access_token_and_post_args(self, mixin):
        url = "http://example.com"
        access_token = "test_token"
        post_args = {"key": "value"}
        response_body = '{"result": "success"}'
        
        http_client = mixin.get_auth_http_client()
        http_client.fetch.return_value.body = response_body
        
        with patch.object(mixin, 'get_auth_http_client', return_value=http_client):
            response = await mixin.oauth2_request(url, access_token=access_token, post_args=post_args)
        
        expected_url = url + "?" + urllib.parse.urlencode({"access_token": access_token})
        http_client.fetch.assert_called_once_with(expected_url, method="POST", body=urllib.parse.urlencode(post_args))
        assert response == json_decode(response_body)

    @pytest.mark.asyncio
    async def test_oauth2_request_with_access_token_no_post_args(self, mixin):
        url = "http://example.com"
        access_token = "test_token"
        response_body = '{"result": "success"}'
        
        http_client = mixin.get_auth_http_client()
        http_client.fetch.return_value.body = response_body
        
        with patch.object(mixin, 'get_auth_http_client', return_value=http_client):
            response = await mixin.oauth2_request(url, access_token=access_token)
        
        expected_url = url + "?" + urllib.parse.urlencode({"access_token": access_token})
        http_client.fetch.assert_called_once_with(expected_url)
        assert response == json_decode(response_body)

    @pytest.mark.asyncio
    async def test_oauth2_request_no_access_token_with_post_args(self, mixin):
        url = "http://example.com"
        post_args = {"key": "value"}
        response_body = '{"result": "success"}'
        
        http_client = mixin.get_auth_http_client()
        http_client.fetch.return_value.body = response_body
        
        with patch.object(mixin, 'get_auth_http_client', return_value=http_client):
            response = await mixin.oauth2_request(url, post_args=post_args)
        
        http_client.fetch.assert_called_once_with(url, method="POST", body=urllib.parse.urlencode(post_args))
        assert response == json_decode(response_body)

    @pytest.mark.asyncio
    async def test_oauth2_request_no_access_token_no_post_args(self, mixin):
        url = "http://example.com"
        response_body = '{"result": "success"}'
        
        http_client = mixin.get_auth_http_client()
        http_client.fetch.return_value.body = response_body
        
        with patch.object(mixin, 'get_auth_http_client', return_value=http_client):
            response = await mixin.oauth2_request(url)
        
        http_client.fetch.assert_called_once_with(url)
        assert response == json_decode(response_body)
