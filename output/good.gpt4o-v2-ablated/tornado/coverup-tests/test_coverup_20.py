# file: tornado/auth.py:1102-1132
# asked: {"lines": [1102, 1106, 1107, 1113, 1114, 1115, 1117, 1118, 1119, 1120, 1121, 1122, 1125, 1127, 1128, 1129, 1131, 1132], "branches": []}
# gained: {"lines": [1102, 1106, 1107, 1113, 1114, 1115, 1117, 1118, 1119, 1120, 1121, 1122, 1125, 1127, 1128, 1129, 1131, 1132], "branches": []}

import pytest
import urllib.parse
import hmac
import hashlib
import binascii
from tornado.escape import utf8

# Assuming _oauth_escape is defined somewhere in the module
def _oauth_escape(value: str) -> str:
    return urllib.parse.quote(value, safe='~')

# Assuming escape.utf8 is defined somewhere in the module
class escape:
    @staticmethod
    def utf8(value: str) -> bytes:
        if isinstance(value, bytes):
            return value
        return value.encode('utf-8')

# Import the function to be tested
from tornado.auth import _oauth_signature

@pytest.fixture
def consumer_token():
    return {"key": "test_consumer_key", "secret": "test_consumer_secret"}

@pytest.fixture
def token():
    return {"key": "test_token_key", "secret": "test_token_secret"}

def test_oauth_signature_no_token(consumer_token):
    method = "GET"
    url = "https://api.example.com/resource"
    parameters = {"param1": "value1", "param2": "value2"}

    signature = _oauth_signature(consumer_token, method, url, parameters)
    
    assert isinstance(signature, bytes)
    assert len(signature) > 0

def test_oauth_signature_with_token(consumer_token, token):
    method = "POST"
    url = "https://api.example.com/resource"
    parameters = {"param1": "value1", "param2": "value2"}

    signature = _oauth_signature(consumer_token, method, url, parameters, token)
    
    assert isinstance(signature, bytes)
    assert len(signature) > 0

def test_oauth_signature_empty_parameters(consumer_token):
    method = "PUT"
    url = "https://api.example.com/resource"
    parameters = {}

    signature = _oauth_signature(consumer_token, method, url, parameters)
    
    assert isinstance(signature, bytes)
    assert len(signature) > 0

def test_oauth_signature_special_characters(consumer_token):
    method = "DELETE"
    url = "https://api.example.com/resource"
    parameters = {"param1": "value1", "param2": "value with spaces & special characters!"}

    signature = _oauth_signature(consumer_token, method, url, parameters)
    
    assert isinstance(signature, bytes)
    assert len(signature) > 0
