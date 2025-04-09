# file: tornado/auth.py:473-495
# asked: {"lines": [473, 495], "branches": []}
# gained: {"lines": [473], "branches": []}

import pytest
from tornado.auth import OAuthMixin

class TestOAuthMixin(OAuthMixin):
    async def _oauth_get_user_future(self, access_token):
        return await super()._oauth_get_user_future(access_token)

@pytest.mark.asyncio
async def test_oauth_get_user_future_not_implemented():
    mixin = TestOAuthMixin()
    access_token = {"token": "dummy_token"}
    
    with pytest.raises(NotImplementedError):
        await mixin._oauth_get_user_future(access_token)
