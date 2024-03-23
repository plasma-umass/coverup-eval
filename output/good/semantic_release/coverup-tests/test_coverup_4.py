# file semantic_release/hvcs.py:365-371
# lines [365, 366, 371]
# branches []

import os
import pytest
from semantic_release.hvcs import Gitlab

@pytest.fixture
def clean_env(mocker):
    # Ensure the environment variable is clean before and after the test
    mocker.patch.dict(os.environ, {}, clear=True)

def test_gitlab_token(clean_env):
    # Test when GL_TOKEN is not set
    assert Gitlab.token() is None

    # Set the GL_TOKEN environment variable and test again
    os.environ["GL_TOKEN"] = "test_token"
    assert Gitlab.token() == "test_token"

    # Clean up by deleting the GL_TOKEN environment variable
    del os.environ["GL_TOKEN"]
    assert Gitlab.token() is None
