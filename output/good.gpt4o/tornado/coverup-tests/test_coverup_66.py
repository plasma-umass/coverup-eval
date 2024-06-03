# file tornado/auth.py:823-831
# lines [823, 826, 827, 829, 830, 831]
# branches ['829->830', '829->831']

import pytest
from tornado.auth import TwitterMixin
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_oauth_get_user_future(mocker):
    # Create an instance of the TwitterMixin
    twitter_mixin = TwitterMixin()

    # Mock the twitter_request method
    mock_twitter_request = mocker.patch.object(
        twitter_mixin, 'twitter_request', new_callable=AsyncMock
    )

    # Define the access token and the expected user data
    access_token = {"key": "value"}
    user_data = {"screen_name": "testuser"}

    # Set the return value of the mocked twitter_request method
    mock_twitter_request.return_value = user_data

    # Call the _oauth_get_user_future method
    result = await twitter_mixin._oauth_get_user_future(access_token)

    # Assert that the twitter_request method was called with the correct parameters
    mock_twitter_request.assert_called_once_with(
        "/account/verify_credentials", access_token=access_token
    )

    # Assert that the result contains the expected user data with the username key
    assert result == {"screen_name": "testuser", "username": "testuser"}

    # Test the case where twitter_request returns None
    mock_twitter_request.return_value = None
    result = await twitter_mixin._oauth_get_user_future(access_token)
    assert result is None
