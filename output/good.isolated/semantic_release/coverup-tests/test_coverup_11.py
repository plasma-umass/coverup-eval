# file semantic_release/hvcs.py:67-87
# lines [67, 68, 72, 73, 75, 76, 77, 78, 82, 83, 85, 86, 87]
# branches []

import pytest
from requests import Request
from semantic_release.hvcs import TokenAuth

def test_token_auth():
    token = 'test-token'
    auth = TokenAuth(token)

    # Test __call__
    request = Request()
    auth(request)
    assert request.headers['Authorization'] == f'token {token}'

    # Test __eq__
    assert auth == TokenAuth(token)
    assert not (auth == TokenAuth('different-token'))

    # Test __ne__
    assert not (auth != TokenAuth(token))
    assert auth != TokenAuth('different-token')

@pytest.fixture
def token_auth():
    return TokenAuth('test-token')

def test_token_auth_call(token_auth, mocker):
    mock_request = mocker.Mock()
    mock_request.headers = {}

    token_auth(mock_request)

    assert mock_request.headers['Authorization'] == 'token test-token'

def test_token_auth_eq(token_auth):
    same_token_auth = TokenAuth('test-token')
    different_token_auth = TokenAuth('different-token')

    assert token_auth == same_token_auth
    assert token_auth != different_token_auth

def test_token_auth_ne(token_auth):
    same_token_auth = TokenAuth('test-token')
    different_token_auth = TokenAuth('different-token')

    assert not (token_auth != same_token_auth)
    assert token_auth != different_token_auth
