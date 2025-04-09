# file: tornado/auth.py:739-812
# asked: {"lines": [739, 743, 787, 790, 792, 794, 795, 796, 797, 798, 799, 800, 802, 803, 804, 805, 806, 807, 808, 811, 812], "branches": [[787, 790], [787, 792], [794, 795], [794, 803], [803, 804], [803, 805], [806, 807], [806, 811]]}
# gained: {"lines": [739, 743], "branches": []}

import pytest
from tornado.auth import TwitterMixin
from tornado.httpclient import HTTPResponse, HTTPRequest, AsyncHTTPClient
from tornado.escape import json_encode
from unittest.mock import patch, MagicMock

class MockTwitterHandler(TwitterMixin):
    def get_auth_http_client(self):
        return AsyncHTTPClient()

@pytest.mark.asyncio
async def test_twitter_request_get(monkeypatch):
    handler = MockTwitterHandler()
    access_token = {"key": "test_key", "secret": "test_secret"}
    path = "statuses/user_timeline/btaylor"
    url = handler._TWITTER_BASE_URL + path + ".json"

    mock_response = MagicMock()
    mock_response.body = json_encode({"result": "success"}).encode()

    async def mock_fetch(request, **kwargs):
        assert request.url == url + "?oauth_consumer_key=test_key&oauth_token=test_secret"
        return mock_response

    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)

    response = await handler.twitter_request(path, access_token)
    assert response == {"result": "success"}

@pytest.mark.asyncio
async def test_twitter_request_post(monkeypatch):
    handler = MockTwitterHandler()
    access_token = {"key": "test_key", "secret": "test_secret"}
    path = "statuses/update"
    post_args = {"status": "Testing Tornado Web Server"}
    url = handler._TWITTER_BASE_URL + path + ".json"

    mock_response = MagicMock()
    mock_response.body = json_encode({"result": "success"}).encode()

    async def mock_fetch(request, **kwargs):
        assert request.url == url
        assert kwargs["method"] == "POST"
        assert kwargs["body"] == "status=Testing+Tornado+Web+Server"
        return mock_response

    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)

    response = await handler.twitter_request(path, access_token, post_args=post_args)
    assert response == {"result": "success"}

@pytest.mark.asyncio
async def test_twitter_request_full_url(monkeypatch):
    handler = MockTwitterHandler()
    access_token = {"key": "test_key", "secret": "test_secret"}
    path = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    url = path

    mock_response = MagicMock()
    mock_response.body = json_encode({"result": "success"}).encode()

    async def mock_fetch(request, **kwargs):
        assert request.url == url + "?oauth_consumer_key=test_key&oauth_token=test_secret"
        return mock_response

    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)

    response = await handler.twitter_request(path, access_token)
    assert response == {"result": "success"}
