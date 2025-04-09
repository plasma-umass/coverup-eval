# file tornado/auth.py:823-831
# lines [823, 826, 827, 829, 830, 831]
# branches ['829->830', '829->831']

import pytest
from tornado.auth import TwitterMixin
from unittest.mock import create_autospec, AsyncMock

class DummyTwitterMixin(TwitterMixin):
    twitter_request = AsyncMock()

@pytest.fixture
def twitter_mixin():
    return DummyTwitterMixin()

@pytest.mark.asyncio
async def test_oauth_get_user_future_with_user(twitter_mixin):
    # Mock the twitter_request to return a user with a screen_name
    twitter_mixin.twitter_request.return_value = {
        "screen_name": "test_user"
    }
    access_token = {"key": "value"}
    user = await twitter_mixin._oauth_get_user_future(access_token)
    assert user["username"] == "test_user"
    twitter_mixin.twitter_request.assert_awaited_once_with(
        "/account/verify_credentials", access_token=access_token
    )

@pytest.mark.asyncio
async def test_oauth_get_user_future_without_user(twitter_mixin):
    # Mock the twitter_request to return None
    twitter_mixin.twitter_request.return_value = None
    access_token = {"key": "value"}
    user = await twitter_mixin._oauth_get_user_future(access_token)
    assert user is None
    twitter_mixin.twitter_request.assert_awaited_once_with(
        "/account/verify_credentials", access_token=access_token
    )
