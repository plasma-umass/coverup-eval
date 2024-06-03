# file semantic_release/hvcs.py:118-124
# lines [118, 119, 124]
# branches []

import os
import pytest
from semantic_release.hvcs import Github

def test_github_token(mocker):
    # Mock the environment variable
    mocker.patch.dict(os.environ, {"GH_TOKEN": "test_token"})
    
    # Call the token method
    token = Github.token()
    
    # Assert that the token method returns the correct value
    assert token == "test_token"
    
    # Clean up by ensuring the environment variable is removed
    del os.environ["GH_TOKEN"]
