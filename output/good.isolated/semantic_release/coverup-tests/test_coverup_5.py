# file semantic_release/hvcs.py:118-124
# lines [118, 119, 124]
# branches []

import os
import pytest
from semantic_release.hvcs import Github

@pytest.fixture
def clean_env(mocker):
    # Use pytest-mock to isolate environment changes
    mocker.patch.dict(os.environ, {}, clear=True)

def test_github_token_present(clean_env):
    # Set the GH_TOKEN environment variable
    os.environ["GH_TOKEN"] = "test_token"
    # Assert that the token method returns the correct value
    assert Github.token() == "test_token"
    # Cleanup is handled by the clean_env fixture

def test_github_token_absent(clean_env):
    # Ensure GH_TOKEN is not set
    assert "GH_TOKEN" not in os.environ
    # Assert that the token method returns None when the token is not set
    assert Github.token() is None
    # Cleanup is handled by the clean_env fixture
