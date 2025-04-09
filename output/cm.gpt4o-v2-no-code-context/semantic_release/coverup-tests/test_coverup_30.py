# file: semantic_release/ci_checks.py:91-100
# asked: {"lines": [91, 92, 99, 100], "branches": []}
# gained: {"lines": [91, 92, 99, 100], "branches": []}

import os
import pytest
from semantic_release.ci_checks import bitbucket, CiVerificationError

def test_bitbucket_branch(monkeypatch):
    # Set up the environment variables
    monkeypatch.setenv("BITBUCKET_BRANCH", "main")
    monkeypatch.delenv("BITBUCKET_PR_ID", raising=False)

    # Call the function with the expected branch
    bitbucket("main")

    # Assertions are within the function, so if no assertion error is raised, the test passes

def test_bitbucket_pr_id(monkeypatch):
    # Set up the environment variables
    monkeypatch.setenv("BITBUCKET_BRANCH", "main")
    monkeypatch.setenv("BITBUCKET_PR_ID", "123")

    # Call the function with the expected branch and expect a CiVerificationError
    with pytest.raises(CiVerificationError):
        bitbucket("main")
