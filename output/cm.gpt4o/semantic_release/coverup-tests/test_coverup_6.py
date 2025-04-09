# file semantic_release/hvcs.py:365-371
# lines [365, 366, 371]
# branches []

import os
import pytest
from semantic_release.hvcs import Gitlab

def test_gitlab_token(mocker):
    # Mock the environment variable
    mocker.patch.dict(os.environ, {"GL_TOKEN": "test_token"})
    
    # Test if the token method returns the correct value
    assert Gitlab.token() == "test_token"
    
    # Clean up by removing the environment variable
    del os.environ["GL_TOKEN"]

def test_gitlab_token_absent(mocker):
    # Ensure the environment variable is not set
    mocker.patch.dict(os.environ, {}, clear=True)
    
    # Test if the token method returns None when the environment variable is not set
    assert Gitlab.token() is None
