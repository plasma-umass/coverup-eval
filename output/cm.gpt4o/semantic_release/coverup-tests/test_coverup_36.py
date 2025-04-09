# file semantic_release/hvcs.py:126-135
# lines [126, 127, 132, 133, 134, 135]
# branches ['133->134', '133->135']

import os
import pytest
from semantic_release.hvcs import Github
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = f'token {self.token}'
        return r

class Base:
    @staticmethod
    def token():
        return os.getenv('GH_TOKEN')

def test_github_auth_with_token(mocker):
    mocker.patch('semantic_release.hvcs.Github.token', return_value='test_token')
    auth = Github.auth()
    assert auth is not None
    assert auth.token == 'test_token'

def test_github_auth_without_token(mocker):
    mocker.patch('semantic_release.hvcs.Github.token', return_value=None)
    auth = Github.auth()
    assert auth is None
