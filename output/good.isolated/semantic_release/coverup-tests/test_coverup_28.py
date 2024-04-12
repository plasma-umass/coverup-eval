# file semantic_release/ci_checks.py:91-100
# lines [91, 92, 99, 100]
# branches []

import os
import pytest
from semantic_release.ci_checks import bitbucket
from semantic_release.errors import CiVerificationError

def test_bitbucket_success(mocker):
    # Setup the environment variables to match the expected values
    mocker.patch.dict(os.environ, {
        "BITBUCKET_BRANCH": "main",
    })

    # Call the bitbucket function to check if it passes with the correct environment variables
    bitbucket("main")

def test_bitbucket_failure_due_to_branch_mismatch(mocker):
    # Setup the environment variables with a different branch
    mocker.patch.dict(os.environ, {
        "BITBUCKET_BRANCH": "feature",
    })

    # Assert that a CiVerificationError is raised due to branch mismatch
    with pytest.raises(CiVerificationError):
        bitbucket("main")

def test_bitbucket_failure_due_to_pr_id(mocker):
    # Setup the environment variables with a PR ID
    mocker.patch.dict(os.environ, {
        "BITBUCKET_BRANCH": "main",
        "BITBUCKET_PR_ID": "123"
    })

    # Assert that a CiVerificationError is raised due to the presence of a PR ID
    with pytest.raises(CiVerificationError):
        bitbucket("main")
