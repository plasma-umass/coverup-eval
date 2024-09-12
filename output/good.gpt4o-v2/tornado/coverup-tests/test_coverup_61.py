# file: tornado/auth.py:823-831
# asked: {"lines": [823, 826, 827, 829, 830, 831], "branches": [[829, 830], [829, 831]]}
# gained: {"lines": [823], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from tornado.auth import TwitterMixin

@pytest.mark.asyncio
async def test_oauth_get_user_future():
    access_token = {"key": "value"}
    user_data = {"screen_name": "testuser"}

    with patch.object(TwitterMixin, 'twitter_request', return_value=user_data) as mock_twitter_request:
        twitter_mixin = TwitterMixin()
        user = await twitter_mixin._oauth_get_user_future(access_token)

        mock_twitter_request.assert_called_once_with("/account/verify_credentials", access_token=access_token)
        assert user["username"] == "testuser"
        assert user["screen_name"] == "testuser"
