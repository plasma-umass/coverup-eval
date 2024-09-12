# file: tornado/auth.py:739-812
# asked: {"lines": [739, 743, 787, 790, 792, 794, 795, 796, 797, 798, 799, 800, 802, 803, 804, 805, 806, 807, 808, 811, 812], "branches": [[787, 790], [787, 792], [794, 795], [794, 803], [803, 804], [803, 805], [806, 807], [806, 811]]}
# gained: {"lines": [739, 743], "branches": []}

import pytest
from tornado.auth import TwitterMixin
from tornado.httpclient import AsyncHTTPClient, HTTPResponse, HTTPRequest
from tornado.escape import json_encode
from unittest.mock import patch, MagicMock
import urllib.parse

class MockTwitterMixin(TwitterMixin):
    _TWITTER_BASE_URL = "https://api.twitter.com/1.1/"

    def get_auth_http_client(self):
        return AsyncHTTPClient()

@pytest.mark.asyncio
async def test_twitter_request_get(monkeypatch):
    async def mock_fetch(request, **kwargs):
        assert request.url == "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=testuser"
        return HTTPResponse(request, 200, buffer=json_encode({"result": "success"}).encode())

    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)

    mixin = MockTwitterMixin()
    access_token = {"key": "test_key", "secret": "test_secret"}
    response = await mixin.twitter_request("statuses/user_timeline", access_token, screen_name="testuser")
    assert response == {"result": "success"}

@pytest.mark.asyncio
async def test_twitter_request_post(monkeypatch):
    async def mock_fetch(request, **kwargs):
        assert request.url == "https://api.twitter.com/1.1/statuses/update.json"
        assert request.method == "POST"
        assert request.body == urllib.parse.urlencode({"status": "Testing Tornado Web Server"}).encode()
        return HTTPResponse(request, 200, buffer=json_encode({"result": "success"}).encode())

    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)

    mixin = MockTwitterMixin()
    access_token = {"key": "test_key", "secret": "test_secret"}
    response = await mixin.twitter_request("statuses/update", access_token, post_args={"status": "Testing Tornado Web Server"})
    assert response == {"result": "success"}

@pytest.mark.asyncio
async def test_twitter_request_raw_url(monkeypatch):
    async def mock_fetch(request, **kwargs):
        assert request.url == "http://search.twitter.com/search.json?q=test"
        return HTTPResponse(request, 200, buffer=json_encode({"result": "success"}).encode())

    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)

    mixin = MockTwitterMixin()
    access_token = {"key": "test_key", "secret": "test_secret"}
    response = await mixin.twitter_request("http://search.twitter.com/search", access_token, q="test")
    assert response == {"result": "success"}
