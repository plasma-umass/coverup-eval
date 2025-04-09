# file: tornado/auth.py:814-821
# asked: {"lines": [814, 815, 816, 817, 818, 819, 820], "branches": []}
# gained: {"lines": [814, 815, 816, 817, 818, 819, 820], "branches": []}

import pytest
from tornado.web import RequestHandler
from tornado.auth import TwitterMixin
from typing import Dict, Any

class MockApplication:
    settings = {
        "twitter_consumer_key": "test_key",
        "twitter_consumer_secret": "test_secret"
    }

class MockRequestHandler(RequestHandler, TwitterMixin):
    def __init__(self):
        self.application = MockApplication()

def test_oauth_consumer_token():
    handler = MockRequestHandler()
    token = handler._oauth_consumer_token()
    assert token == {
        "key": "test_key",
        "secret": "test_secret"
    }

def test_oauth_consumer_token_missing_key(monkeypatch):
    handler = MockRequestHandler()
    monkeypatch.delitem(handler.application.settings, "twitter_consumer_key", raising=False)
    with pytest.raises(Exception) as excinfo:
        handler._oauth_consumer_token()
    assert "You must define the 'twitter_consumer_key' setting in your application to use Twitter OAuth" in str(excinfo.value)

def test_oauth_consumer_token_missing_secret(monkeypatch):
    handler = MockRequestHandler()
    monkeypatch.delitem(handler.application.settings, "twitter_consumer_secret", raising=False)
    with pytest.raises(Exception) as excinfo:
        handler._oauth_consumer_token()
    assert "You must define the 'twitter_consumer_secret' setting in your application to use Twitter OAuth" in str(excinfo.value)
