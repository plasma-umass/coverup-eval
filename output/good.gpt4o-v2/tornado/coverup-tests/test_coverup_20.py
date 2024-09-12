# file: tornado/auth.py:1135-1167
# asked: {"lines": [1135, 1139, 1140, 1146, 1147, 1148, 1150, 1151, 1152, 1153, 1154, 1155, 1159, 1160, 1161, 1162, 1164, 1166, 1167], "branches": []}
# gained: {"lines": [1135, 1139, 1140, 1146, 1147, 1148, 1150, 1151, 1152, 1153, 1154, 1155, 1159, 1160, 1161, 1162, 1164, 1166, 1167], "branches": []}

import pytest
from tornado.auth import _oauth10a_signature

def test_oauth10a_signature_with_token():
    consumer_token = {"key": "consumer_key", "secret": "consumer_secret"}
    token = {"key": "token_key", "secret": "token_secret"}
    method = "POST"
    url = "https://api.example.com/resource"
    parameters = {"param1": "value1", "param2": "value2"}

    signature = _oauth10a_signature(consumer_token, method, url, parameters, token)
    
    assert isinstance(signature, bytes)
    assert signature  # Check that the signature is not empty

def test_oauth10a_signature_without_token():
    consumer_token = {"key": "consumer_key", "secret": "consumer_secret"}
    method = "GET"
    url = "https://api.example.com/resource"
    parameters = {"param1": "value1", "param2": "value2"}

    signature = _oauth10a_signature(consumer_token, method, url, parameters)
    
    assert isinstance(signature, bytes)
    assert signature  # Check that the signature is not empty
