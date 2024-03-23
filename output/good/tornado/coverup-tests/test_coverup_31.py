# file tornado/auth.py:610-664
# lines [610, 613, 614, 650, 651, 652, 653, 655, 656, 657, 658, 659, 660, 663, 664]
# branches ['651->652', '651->655', '655->656', '655->657', '658->659', '658->663']

import pytest
from tornado.auth import OAuth2Mixin
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPResponse
from tornado import escape
import urllib.parse

class DummyOAuth2Mixin(OAuth2Mixin):
    def get_auth_http_client(self):
        return AsyncHTTPClient()

@pytest.fixture
def mock_http_client(mocker):
    client = mocker.Mock(spec=AsyncHTTPClient)
    response = HTTPResponse(HTTPRequest(url='http://example.com'), 200, buffer=escape.utf8('{"name": "test"}'))
    client.fetch = mocker.AsyncMock(return_value=response)
    return client

@pytest.fixture
def mock_oauth_mixin(mock_http_client, mocker):
    mixin = DummyOAuth2Mixin()
    mixin.get_auth_http_client = mocker.Mock(return_value=mock_http_client)
    return mixin

@pytest.mark.asyncio
async def test_oauth2_request_get(mock_oauth_mixin):
    response = await mock_oauth_mixin.oauth2_request(
        'http://example.com',
        access_token='fake_token',
        extra_param='value'
    )
    assert response == {"name": "test"}
    mock_oauth_mixin.get_auth_http_client().fetch.assert_called_once_with('http://example.com?access_token=fake_token&extra_param=value')

@pytest.mark.asyncio
async def test_oauth2_request_post(mock_oauth_mixin):
    response = await mock_oauth_mixin.oauth2_request(
        'http://example.com',
        access_token='fake_token',
        post_args={'key': 'value'},
        extra_param='value'
    )
    assert response == {"name": "test"}
    encoded_body = urllib.parse.urlencode({'key': 'value'})
    mock_oauth_mixin.get_auth_http_client().fetch.assert_called_once_with(
        'http://example.com?access_token=fake_token&extra_param=value',
        method="POST",
        body=encoded_body
    )
