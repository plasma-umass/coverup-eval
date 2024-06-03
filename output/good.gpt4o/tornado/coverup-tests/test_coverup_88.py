# file tornado/auth.py:834-858
# lines [834, 835, 853, 854, 855, 856, 857]
# branches []

import pytest
from tornado.auth import GoogleOAuth2Mixin
from tornado.web import RequestHandler, Application
from tornado.testing import AsyncHTTPTestCase
from unittest.mock import patch

class TestGoogleOAuth2Mixin(AsyncHTTPTestCase):
    def get_app(self):
        class TestHandler(RequestHandler, GoogleOAuth2Mixin):
            async def get(self):
                self.write("Hello, world")

        return Application([("/", TestHandler)])

    @patch.object(GoogleOAuth2Mixin, '_OAUTH_AUTHORIZE_URL', "https://accounts.google.com/o/oauth2/v2/auth")
    @patch.object(GoogleOAuth2Mixin, '_OAUTH_ACCESS_TOKEN_URL', "https://www.googleapis.com/oauth2/v4/token")
    @patch.object(GoogleOAuth2Mixin, '_OAUTH_USERINFO_URL', "https://www.googleapis.com/oauth2/v1/userinfo")
    @patch.object(GoogleOAuth2Mixin, '_OAUTH_NO_CALLBACKS', False)
    @patch.object(GoogleOAuth2Mixin, '_OAUTH_SETTINGS_KEY', "google_oauth")
    def test_google_oauth2_mixin(self):
        response = self.fetch('/')
        assert response.code == 200
        assert response.body == b"Hello, world"

    def test_oauth_settings_key(self):
        mixin = GoogleOAuth2Mixin()
        assert mixin._OAUTH_SETTINGS_KEY == "google_oauth"

    def test_oauth_authorize_url(self):
        mixin = GoogleOAuth2Mixin()
        assert mixin._OAUTH_AUTHORIZE_URL == "https://accounts.google.com/o/oauth2/v2/auth"

    def test_oauth_access_token_url(self):
        mixin = GoogleOAuth2Mixin()
        assert mixin._OAUTH_ACCESS_TOKEN_URL == "https://www.googleapis.com/oauth2/v4/token"

    def test_oauth_userinfo_url(self):
        mixin = GoogleOAuth2Mixin()
        assert mixin._OAUTH_USERINFO_URL == "https://www.googleapis.com/oauth2/v1/userinfo"

    def test_oauth_no_callbacks(self):
        mixin = GoogleOAuth2Mixin()
        assert mixin._OAUTH_NO_CALLBACKS == False
