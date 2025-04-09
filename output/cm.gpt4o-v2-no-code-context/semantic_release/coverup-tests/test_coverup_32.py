# file: semantic_release/ci_checks.py:30-39
# asked: {"lines": [30, 31, 38, 39], "branches": []}
# gained: {"lines": [30, 31, 38, 39], "branches": []}

import os
import pytest
from semantic_release.ci_checks import travis, CiVerificationError

def test_travis_branch(monkeypatch):
    # Set up the environment variables
    monkeypatch.setenv("TRAVIS_BRANCH", "main")
    monkeypatch.setenv("TRAVIS_PULL_REQUEST", "false")
    
    # Call the travis function with the branch name
    travis("main")
    
    # Assertions are within the travis function, so if no assertion error is raised, the test passes

def test_travis_branch_fail_branch(monkeypatch):
    # Set up the environment variables with a different branch
    monkeypatch.setenv("TRAVIS_BRANCH", "develop")
    monkeypatch.setenv("TRAVIS_PULL_REQUEST", "false")
    
    # Call the travis function with a different branch name to trigger CiVerificationError
    with pytest.raises(CiVerificationError):
        travis("main")

def test_travis_pull_request(monkeypatch):
    # Set up the environment variables with a pull request
    monkeypatch.setenv("TRAVIS_BRANCH", "main")
    monkeypatch.setenv("TRAVIS_PULL_REQUEST", "true")
    
    # Call the travis function to trigger CiVerificationError
    with pytest.raises(CiVerificationError):
        travis("main")
