# file: semantic_release/ci_checks.py:103-115
# asked: {"lines": [103, 104, 112, 113, 114, 115], "branches": []}
# gained: {"lines": [103, 104, 112, 113, 114, 115], "branches": []}

import os
import pytest
from semantic_release.ci_checks import jenkins, CiVerificationError

def test_jenkins(monkeypatch):
    # Set up the environment variables
    monkeypatch.setenv("JENKINS_URL", "http://example.com")
    monkeypatch.setenv("BRANCH_NAME", "main")
    monkeypatch.delenv("GIT_BRANCH", raising=False)
    monkeypatch.delenv("CHANGE_ID", raising=False)

    # Call the function with the expected branch name
    jenkins("main")

    # Clean up the environment variables
    monkeypatch.undo()

def test_jenkins_with_git_branch(monkeypatch):
    # Set up the environment variables
    monkeypatch.setenv("JENKINS_URL", "http://example.com")
    monkeypatch.delenv("BRANCH_NAME", raising=False)
    monkeypatch.setenv("GIT_BRANCH", "main")
    monkeypatch.delenv("CHANGE_ID", raising=False)

    # Call the function with the expected branch name
    jenkins("main")

    # Clean up the environment variables
    monkeypatch.undo()

def test_jenkins_with_change_id(monkeypatch):
    # Set up the environment variables
    monkeypatch.setenv("JENKINS_URL", "http://example.com")
    monkeypatch.setenv("BRANCH_NAME", "main")
    monkeypatch.setenv("CHANGE_ID", "123")

    # Call the function and expect a CiVerificationError
    with pytest.raises(CiVerificationError):
        jenkins("main")

    # Clean up the environment variables
    monkeypatch.undo()
