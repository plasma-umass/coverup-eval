# file semantic_release/ci_checks.py:55-64
# lines [55, 56, 63, 64]
# branches []

import os
import pytest
from semantic_release.ci_checks import frigg
from semantic_release.errors import CiVerificationError
from unittest.mock import patch

# Test function to cover missing lines in frigg checker
def test_frigg_success(mocker):
    # Set up environment variables to match the expected values
    mocker.patch.dict(os.environ, {
        "FRIGG_BUILD_BRANCH": "main",
        "FRIGG_PULL_REQUEST": ""
    })

    # Call the frigg function with the correct branch
    frigg("main")

    # Assert that the environment variables are as expected
    assert os.environ["FRIGG_BUILD_BRANCH"] == "main"
    assert os.environ.get("FRIGG_PULL_REQUEST") == ""

def test_frigg_wrong_branch(mocker):
    # Set up environment variables with a different branch
    mocker.patch.dict(os.environ, {
        "FRIGG_BUILD_BRANCH": "develop",
        "FRIGG_PULL_REQUEST": ""
    })

    # Assert that a CiVerificationError is raised when the branch does not match
    with pytest.raises(CiVerificationError):
        frigg("main")

def test_frigg_pull_request(mocker):
    # Set up environment variables indicating a pull request
    mocker.patch.dict(os.environ, {
        "FRIGG_BUILD_BRANCH": "main",
        "FRIGG_PULL_REQUEST": "true"
    })

    # Assert that a CiVerificationError is raised when it's a pull request
    with pytest.raises(CiVerificationError):
        frigg("main")
