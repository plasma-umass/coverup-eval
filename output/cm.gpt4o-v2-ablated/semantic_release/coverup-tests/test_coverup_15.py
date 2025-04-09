# file: semantic_release/hvcs.py:67-87
# asked: {"lines": [67, 68, 72, 73, 75, 76, 77, 78, 82, 83, 85, 86, 87], "branches": []}
# gained: {"lines": [67, 68, 72, 73, 75, 76, 77, 78, 82, 83, 85, 86, 87], "branches": []}

import pytest
from requests.auth import AuthBase
from semantic_release.hvcs import TokenAuth

def test_token_auth_init():
    token = "test_token"
    auth = TokenAuth(token)
    assert auth.token == token

def test_token_auth_eq():
    token1 = "test_token_1"
    token2 = "test_token_2"
    auth1 = TokenAuth(token1)
    auth2 = TokenAuth(token1)
    auth3 = TokenAuth(token2)
    assert auth1 == auth2
    assert auth1 != auth3

def test_token_auth_ne():
    token1 = "test_token_1"
    token2 = "test_token_2"
    auth1 = TokenAuth(token1)
    auth2 = TokenAuth(token2)
    assert auth1 != auth2

def test_token_auth_call(mocker):
    token = "test_token"
    auth = TokenAuth(token)
    request = mocker.Mock()
    request.headers = {}
    auth(request)
    assert request.headers["Authorization"] == f"token {token}"
