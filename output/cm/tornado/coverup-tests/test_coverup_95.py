# file tornado/auth.py:1039-1099
# lines [1039, 1042, 1043, 1096, 1097, 1098]
# branches []

import pytest
from tornado.auth import FacebookGraphMixin
from unittest.mock import AsyncMock

@pytest.fixture
def facebook_graph_mixin(mocker):
    mixin = FacebookGraphMixin()
    mixin._FACEBOOK_BASE_URL = "https://graph.facebook.com"
    mixin.oauth2_request = AsyncMock()
    return mixin

@pytest.mark.asyncio
async def test_facebook_request_get(facebook_graph_mixin):
    # Mock the oauth2_request to return a specific value
    facebook_graph_mixin.oauth2_request.return_value = {"data": "test_data"}

    # Perform a GET request
    response = await facebook_graph_mixin.facebook_request(
        "/me/picture",
        access_token="dummy_access_token"
    )

    # Assert that the oauth2_request was called with the correct URL
    facebook_graph_mixin.oauth2_request.assert_called_once_with(
        "https://graph.facebook.com/me/picture",
        access_token="dummy_access_token",
        post_args=None
    )

    # Assert that the response is as expected
    assert response == {"data": "test_data"}

@pytest.mark.asyncio
async def test_facebook_request_post(facebook_graph_mixin):
    # Mock the oauth2_request to return a specific value
    facebook_graph_mixin.oauth2_request.return_value = {"id": "post_id"}

    # Perform a POST request
    response = await facebook_graph_mixin.facebook_request(
        "/me/feed",
        access_token="dummy_access_token",
        post_args={"message": "Test message"}
    )

    # Assert that the oauth2_request was called with the correct URL and POST arguments
    facebook_graph_mixin.oauth2_request.assert_called_once_with(
        "https://graph.facebook.com/me/feed",
        access_token="dummy_access_token",
        post_args={"message": "Test message"}
    )

    # Assert that the response is as expected
    assert response == {"id": "post_id"}
