# file: semantic_release/ci_checks.py:67-76
# asked: {"lines": [67, 68, 75, 76], "branches": []}
# gained: {"lines": [67, 68, 75, 76], "branches": []}

import os
import pytest
from semantic_release.ci_checks import circle, CiVerificationError

def test_circle_branch(monkeypatch):
    # Set up the environment variables
    monkeypatch.setenv("CIRCLE_BRANCH", "main")
    monkeypatch.delenv("CI_PULL_REQUEST", raising=False)

    # Call the function with the branch name
    circle("main")

    # Assertions are within the function, so no need for additional assertions here

def test_circle_branch_with_pull_request(monkeypatch):
    # Set up the environment variables
    monkeypatch.setenv("CIRCLE_BRANCH", "main")
    monkeypatch.setenv("CI_PULL_REQUEST", "1")

    # Call the function with the branch name and expect a CiVerificationError
    with pytest.raises(CiVerificationError):
        circle("main")
