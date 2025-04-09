# file: tornado/auth.py:473-495
# asked: {"lines": [473, 495], "branches": []}
# gained: {"lines": [473], "branches": []}

import pytest
from tornado.auth import OAuthMixin

class TestOAuthMixin:
    @pytest.mark.asyncio
    async def test_oauth_get_user_future_not_implemented(self):
        class TestOAuth(OAuthMixin):
            pass

        test_oauth = TestOAuth()
        with pytest.raises(NotImplementedError):
            await test_oauth._oauth_get_user_future({"access_token": "dummy_token"})
