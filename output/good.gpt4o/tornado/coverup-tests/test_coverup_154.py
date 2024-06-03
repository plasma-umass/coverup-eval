# file tornado/auth.py:924-931
# lines [924, 925, 927, 928, 929, 930]
# branches []

import pytest
from tornado.auth import FacebookGraphMixin
from tornado.web import RequestHandler, Application
from unittest.mock import patch, MagicMock
from tornado.httputil import HTTPServerRequest

class MockHandler(RequestHandler, FacebookGraphMixin):
    def initialize(self, *args, **kwargs):
        pass

@pytest.fixture
def mock_handler():
    application = Application()
    request = HTTPServerRequest(uri='/')
    request.connection = MagicMock()
    return MockHandler(application=application, request=request)

def test_facebook_graph_mixin_oauth_urls(mock_handler):
    assert mock_handler._OAUTH_ACCESS_TOKEN_URL == "https://graph.facebook.com/oauth/access_token?"
    assert mock_handler._OAUTH_AUTHORIZE_URL == "https://www.facebook.com/dialog/oauth?"
    assert not mock_handler._OAUTH_NO_CALLBACKS
    assert mock_handler._FACEBOOK_BASE_URL == "https://graph.facebook.com"

@patch('tornado.auth.FacebookGraphMixin._OAUTH_ACCESS_TOKEN_URL', "https://mock.url/oauth/access_token?")
@patch('tornado.auth.FacebookGraphMixin._OAUTH_AUTHORIZE_URL', "https://mock.url/dialog/oauth?")
@patch('tornado.auth.FacebookGraphMixin._FACEBOOK_BASE_URL', "https://mock.url")
def test_facebook_graph_mixin_oauth_urls_mocked(mock_handler):
    assert mock_handler._OAUTH_ACCESS_TOKEN_URL == "https://mock.url/oauth/access_token?"
    assert mock_handler._OAUTH_AUTHORIZE_URL == "https://mock.url/dialog/oauth?"
    assert mock_handler._FACEBOOK_BASE_URL == "https://mock.url"
