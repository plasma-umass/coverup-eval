# file tornado/auth.py:814-821
# lines [815, 816, 817, 818, 819, 820]
# branches []

import pytest
from tornado.web import RequestHandler, Application
from tornado.auth import OAuthMixin, TwitterMixin
from tornado.util import ObjectDict

class MockHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self._settings = {
            "twitter_consumer_key": "test_key",
            "twitter_consumer_secret": "test_secret"
        }

    @property
    def settings(self):
        return self._settings

    def require_setting(self, name, context):
        if name not in self.settings:
            raise Exception(f"Missing setting: {name}")

@pytest.fixture
def mock_handler(mocker):
    application = Application()
    application.ui_methods = {}
    request = mocker.Mock()
    return MockHandler(application, request)

def test_oauth_consumer_token(mock_handler):
    class TestTwitterMixin(TwitterMixin, MockHandler):
        pass

    mixin = TestTwitterMixin(mock_handler.application, mock_handler.request)
    token = mixin._oauth_consumer_token()
    
    assert token["key"] == "test_key"
    assert token["secret"] == "test_secret"
