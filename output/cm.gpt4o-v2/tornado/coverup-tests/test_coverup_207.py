# file: tornado/auth.py:814-821
# asked: {"lines": [815, 816, 817, 818, 819, 820], "branches": []}
# gained: {"lines": [815, 816, 817, 818, 819, 820], "branches": []}

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

def test_oauth_consumer_token(monkeypatch):
    handler = MockRequestHandler()

    def mock_require_setting(self, name: str, feature: str = 'this feature') -> None:
        if not self.application.settings.get(name):
            raise Exception(f"You must define the '{name}' setting in your application to use {feature}")

    monkeypatch.setattr(RequestHandler, "require_setting", mock_require_setting)

    result = handler._oauth_consumer_token()
    assert result == {
        "key": "test_key",
        "secret": "test_secret"
    }
