# file: semantic_release/ci_checks.py:30-39
# asked: {"lines": [30, 31, 38, 39], "branches": []}
# gained: {"lines": [30, 31, 38, 39], "branches": []}

import os
import pytest
from semantic_release.ci_checks import travis, CiVerificationError

def test_travis_pass(monkeypatch):
    # Set up the environment variables
    monkeypatch.setenv("TRAVIS_BRANCH", "main")
    monkeypatch.setenv("TRAVIS_PULL_REQUEST", "false")
    
    # Call the travis function with the correct branch
    assert travis("main") == True

def test_travis_fail_branch(monkeypatch):
    # Set up the environment variables
    monkeypatch.setenv("TRAVIS_BRANCH", "develop")
    monkeypatch.setenv("TRAVIS_PULL_REQUEST", "false")
    
    # Call the travis function with the incorrect branch
    with pytest.raises(CiVerificationError):
        travis("main")

def test_travis_fail_pull_request(monkeypatch):
    # Set up the environment variables
    monkeypatch.setenv("TRAVIS_BRANCH", "main")
    monkeypatch.setenv("TRAVIS_PULL_REQUEST", "true")
    
    # Call the travis function with the correct branch but as a pull request
    with pytest.raises(CiVerificationError):
        travis("main")
