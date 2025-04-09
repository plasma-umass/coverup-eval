# file tornado/auth.py:1039-1099
# lines [1039, 1042, 1043, 1096, 1097, 1098]
# branches []

import pytest
from tornado.auth import FacebookGraphMixin, OAuth2Mixin
from tornado.web import RequestHandler
from unittest.mock import patch, AsyncMock

class MockHandler(RequestHandler, FacebookGraphMixin):
    def initialize(self, access_token):
        self._access_token = access_token

    def get_current_user(self):
        return {"access_token": self._access_token}

@pytest.mark.asyncio
async def test_facebook_request(mocker):
    mock_access_token = "mock_access_token"
    mock_path = "/me/feed"
    mock_post_args = {"message": "I am posting from my Tornado application!"}
    mock_response = {"id": "12345"}

    handler = MockHandler(mocker.Mock(), mocker.Mock(), access_token=mock_access_token)
    handler._FACEBOOK_BASE_URL = "https://graph.facebook.com"

    mock_oauth2_request = mocker.patch.object(
        OAuth2Mixin, 'oauth2_request', new_callable=AsyncMock, return_value=mock_response
    )

    response = await handler.facebook_request(
        mock_path, access_token=mock_access_token, post_args=mock_post_args
    )

    mock_oauth2_request.assert_called_once_with(
        "https://graph.facebook.com/me/feed",
        access_token=mock_access_token,
        post_args=mock_post_args
    )

    assert response == mock_response
