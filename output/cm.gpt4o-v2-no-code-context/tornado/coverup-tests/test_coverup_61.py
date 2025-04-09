# file: tornado/auth.py:823-831
# asked: {"lines": [823, 826, 827, 829, 830, 831], "branches": [[829, 830], [829, 831]]}
# gained: {"lines": [823], "branches": []}

import pytest
from tornado.auth import TwitterMixin
from unittest.mock import patch, MagicMock

@pytest.mark.asyncio
async def test_oauth_get_user_future(monkeypatch):
    class MockTwitterMixin(TwitterMixin):
        def twitter_request(self, path, access_token):
            return MagicMock()

    mock_mixin = MockTwitterMixin()

    async def mock_twitter_request(path, access_token):
        if path == "/account/verify_credentials":
            return {"screen_name": "testuser"}
        return None

    monkeypatch.setattr(mock_mixin, "twitter_request", mock_twitter_request)

    access_token = {"key": "value"}
    user = await mock_mixin._oauth_get_user_future(access_token)

    assert user is not None
    assert user["username"] == "testuser"
    assert user["screen_name"] == "testuser"

@pytest.mark.asyncio
async def test_oauth_get_user_future_no_user(monkeypatch):
    class MockTwitterMixin(TwitterMixin):
        def twitter_request(self, path, access_token):
            return MagicMock()

    mock_mixin = MockTwitterMixin()

    async def mock_twitter_request(path, access_token):
        return None

    monkeypatch.setattr(mock_mixin, "twitter_request", mock_twitter_request)

    access_token = {"key": "value"}
    user = await mock_mixin._oauth_get_user_future(access_token)

    assert user is None
