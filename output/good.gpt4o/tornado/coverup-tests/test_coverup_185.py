# file tornado/auth.py:473-495
# lines [473, 495]
# branches []

import pytest
from tornado.auth import OAuthMixin

class TestOAuthMixin(OAuthMixin):
    async def _oauth_get_user_future(self, access_token):
        return {"user_id": "12345", "access_token": access_token}

@pytest.mark.asyncio
async def test_oauth_get_user_future():
    mixin = TestOAuthMixin()
    access_token = {"token": "abc123"}
    result = await mixin._oauth_get_user_future(access_token)
    assert result["user_id"] == "12345"
    assert result["access_token"] == access_token

@pytest.mark.asyncio
async def test_oauth_get_user_future_not_implemented():
    mixin = OAuthMixin()
    with pytest.raises(NotImplementedError):
        await mixin._oauth_get_user_future({"token": "abc123"})
