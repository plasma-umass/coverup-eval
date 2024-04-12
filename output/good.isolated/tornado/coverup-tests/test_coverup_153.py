# file tornado/auth.py:473-495
# lines [473, 495]
# branches []

import pytest
from tornado.auth import OAuthMixin

class DummyOAuthMixin(OAuthMixin):
    async def _oauth_get_user_future(self, access_token):
        return {'access_token': access_token, 'user_info': 'dummy_user_info'}

@pytest.mark.asyncio
async def test_oauth_get_user_future():
    dummy_mixin = DummyOAuthMixin()
    access_token = {'token': '12345'}
    user_info = await dummy_mixin._oauth_get_user_future(access_token)
    assert user_info['access_token'] == access_token
    assert user_info['user_info'] == 'dummy_user_info'

@pytest.mark.asyncio
async def test_oauth_get_user_future_not_implemented():
    mixin = OAuthMixin()
    with pytest.raises(NotImplementedError):
        await mixin._oauth_get_user_future({'token': '12345'})
