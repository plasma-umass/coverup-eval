# file: tornado/auth.py:1102-1132
# asked: {"lines": [1113, 1114, 1115, 1117, 1118, 1119, 1120, 1121, 1122, 1125, 1127, 1128, 1129, 1131, 1132], "branches": []}
# gained: {"lines": [1113, 1114, 1115, 1117, 1118, 1119, 1120, 1121, 1122, 1125, 1127, 1128, 1129, 1131, 1132], "branches": []}

import pytest
from tornado.auth import _oauth_signature
from tornado.escape import utf8

def test_oauth_signature(monkeypatch):
    consumer_token = {"key": "test_consumer_key", "secret": "test_consumer_secret"}
    token = {"key": "test_token_key", "secret": "test_token_secret"}
    method = "POST"
    url = "https://api.example.com/resource"
    parameters = {"param1": "value1", "param2": "value2"}

    def mock_escape(val):
        return utf8(val)

    monkeypatch.setattr("tornado.escape.utf8", mock_escape)

    signature = _oauth_signature(consumer_token, method, url, parameters, token)
    
    assert signature is not None
    assert isinstance(signature, bytes)

    # Clean up
    monkeypatch.undo()
