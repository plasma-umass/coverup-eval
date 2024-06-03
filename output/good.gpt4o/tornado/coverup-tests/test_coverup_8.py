# file tornado/auth.py:739-812
# lines [739, 743, 787, 790, 792, 794, 795, 796, 797, 798, 799, 800, 802, 803, 804, 805, 806, 807, 808, 811, 812]
# branches ['787->790', '787->792', '794->795', '794->803', '803->804', '803->805', '806->807', '806->811']

import pytest
from tornado.auth import TwitterMixin
from tornado.httpclient import AsyncHTTPClient, HTTPResponse, HTTPRequest
from tornado.escape import json_encode
from unittest.mock import patch, MagicMock
import urllib.parse

class MockHandler(TwitterMixin):
    def get_auth_http_client(self):
        return AsyncHTTPClient()

@pytest.mark.asyncio
async def test_twitter_request(mocker):
    handler = MockHandler()
    path = "statuses/user_timeline/btaylor"
    access_token = {"key": "test_key", "secret": "test_secret"}
    post_args = {"status": "Testing Tornado Web Server"}
    args = {"include_entities": "true"}

    mock_response = MagicMock(spec=HTTPResponse)
    mock_response.body = json_encode({"result": "success"}).encode("utf-8")
    mock_fetch = mocker.patch.object(AsyncHTTPClient, 'fetch', return_value=mock_response)

    # Test GET request
    response = await handler.twitter_request(path, access_token, **args)
    assert response == {"result": "success"}
    expected_url = handler._TWITTER_BASE_URL + path + ".json?" + urllib.parse.urlencode(args)
    mock_fetch.assert_called_with(expected_url)

    # Test POST request
    response = await handler.twitter_request(path, access_token, post_args=post_args, **args)
    assert response == {"result": "success"}
    expected_url = handler._TWITTER_BASE_URL + path + ".json?" + urllib.parse.urlencode(args)
    mock_fetch.assert_called_with(expected_url, method="POST", body=urllib.parse.urlencode(post_args))

    # Test raw URL
    raw_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    response = await handler.twitter_request(raw_url, access_token, **args)
    assert response == {"result": "success"}
    expected_url = raw_url + "?" + urllib.parse.urlencode(args)
    mock_fetch.assert_called_with(expected_url)

    # Test without access_token
    response = await handler.twitter_request(path, {}, **args)
    assert response == {"result": "success"}
    expected_url = handler._TWITTER_BASE_URL + path + ".json?" + urllib.parse.urlencode(args)
    mock_fetch.assert_called_with(expected_url)
