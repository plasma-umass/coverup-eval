# file: tornado/auth.py:1102-1132
# asked: {"lines": [1113, 1114, 1115, 1117, 1118, 1119, 1120, 1121, 1122, 1125, 1127, 1128, 1129, 1131, 1132], "branches": []}
# gained: {"lines": [1113, 1114, 1115, 1117, 1118, 1119, 1120, 1121, 1122, 1125, 1127, 1128, 1129, 1131, 1132], "branches": []}

import pytest
from tornado.auth import _oauth_signature
from tornado.util import unicode_type
from typing import Dict, Any, Optional, Union
import urllib.parse

def _oauth_escape(val: Union[str, bytes]) -> str:
    if isinstance(val, unicode_type):
        val = val.encode('utf-8')
    return urllib.parse.quote(val, safe='~')

def test_oauth_signature_no_token():
    consumer_token = {"key": "test_consumer_key", "secret": "test_consumer_secret"}
    method = "GET"
    url = "https://api.test.com/resource"
    parameters = {"param1": "value1", "param2": "value2"}

    signature = _oauth_signature(consumer_token, method, url, parameters)
    
    assert isinstance(signature, bytes)
    assert signature != b""

def test_oauth_signature_with_token():
    consumer_token = {"key": "test_consumer_key", "secret": "test_consumer_secret"}
    token = {"key": "test_token_key", "secret": "test_token_secret"}
    method = "POST"
    url = "https://api.test.com/resource"
    parameters = {"param1": "value1", "param2": "value2"}

    signature = _oauth_signature(consumer_token, method, url, parameters, token)
    
    assert isinstance(signature, bytes)
    assert signature != b""

def test_oauth_escape():
    assert _oauth_escape("abcABC123") == "abcABC123"
    assert _oauth_escape("abc ABC 123") == "abc%20ABC%20123"
    assert _oauth_escape("!*'();:@&=+$,/?#[]") == "%21%2A%27%28%29%3B%3A%40%26%3D%2B%24%2C%2F%3F%23%5B%5D"
    assert _oauth_escape("~") == "~"
