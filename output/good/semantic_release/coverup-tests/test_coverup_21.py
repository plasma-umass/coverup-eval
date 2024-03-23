# file semantic_release/hvcs.py:126-135
# lines [126, 127, 132, 133, 134, 135]
# branches ['133->134', '133->135']

import os
from unittest.mock import patch
from semantic_release.hvcs import Github, TokenAuth
import pytest

@pytest.fixture
def clean_env():
    # Fixture to clean up environment variables after the test
    original_token = os.environ.get('GH_TOKEN')
    yield
    if original_token is not None:
        os.environ['GH_TOKEN'] = original_token
    else:
        os.environ.pop('GH_TOKEN', None)

def test_github_auth_with_token(clean_env):
    test_token = 'test_token'
    with patch.dict(os.environ, {'GH_TOKEN': test_token}):
        auth = Github.auth()
        assert isinstance(auth, TokenAuth)
        assert auth.token == test_token

def test_github_auth_without_token(clean_env):
    if 'GH_TOKEN' in os.environ:
        del os.environ['GH_TOKEN']
    auth = Github.auth()
    assert auth is None
