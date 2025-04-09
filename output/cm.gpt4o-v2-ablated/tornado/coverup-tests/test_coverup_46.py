# file: tornado/auth.py:823-831
# asked: {"lines": [823, 826, 827, 829, 830, 831], "branches": [[829, 830], [829, 831]]}
# gained: {"lines": [823], "branches": []}

import pytest
from tornado.auth import TwitterMixin
from unittest.mock import patch, AsyncMock

@pytest.mark.asyncio
async def test_oauth_get_user_future(monkeypatch):
    access_token = {"key": "value"}
    twitter_mixin = TwitterMixin()

    async def mock_twitter_request(url, access_token):
        if url == "/account/verify_credentials" and access_token == {"key": "value"}:
            return {"screen_name": "testuser"}
        return None

    monkeypatch.setattr(twitter_mixin, "twitter_request", mock_twitter_request)

    user = await twitter_mixin._oauth_get_user_future(access_token)
    assert user == {"screen_name": "testuser", "username": "testuser"}

    async def mock_twitter_request_none(url, access_token):
        return None

    monkeypatch.setattr(twitter_mixin, "twitter_request", mock_twitter_request_none)

    user = await twitter_mixin._oauth_get_user_future(access_token)
    assert user is None
