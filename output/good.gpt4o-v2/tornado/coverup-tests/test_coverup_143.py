# file: tornado/auth.py:717-737
# asked: {"lines": [717, 733, 734, 735, 737], "branches": []}
# gained: {"lines": [717], "branches": []}

import pytest
from tornado import httpclient
from tornado.web import RequestHandler, Application
from unittest.mock import patch, MagicMock
from tornado.concurrent import Future
from tornado.escape import utf8
import base64
from tornado.auth import TwitterMixin

class MockTwitterHandler(RequestHandler, TwitterMixin):
    def _oauth_consumer_token(self):
        return {'key': 'test_key', 'secret': 'test_secret'}

@pytest.mark.gen_test
async def test_authenticate_redirect(monkeypatch):
    async def mock_fetch(request):
        response = MagicMock()
        response.body = b'oauth_token=test_token&oauth_token_secret=test_secret'
        future = Future()
        future.set_result(response)
        return future

    def mock_set_cookie(name, value):
        assert name == '_oauth_request_token'
        expected_value = base64.b64encode(utf8('test_token')) + b'|' + base64.b64encode(utf8('test_secret'))
        assert value == expected_value

    def mock_redirect(url):
        assert url.startswith("http://example.com/authenticate?oauth_token=test_token")

    app = Application()
    request = MagicMock()
    handler = MockTwitterHandler(app, request)

    monkeypatch.setattr(handler, 'get_auth_http_client', lambda: MagicMock(fetch=mock_fetch))
    monkeypatch.setattr(handler, 'set_cookie', mock_set_cookie)
    monkeypatch.setattr(handler, 'redirect', mock_redirect)

    await handler.authenticate_redirect(callback_uri="http://example.com/callback")
