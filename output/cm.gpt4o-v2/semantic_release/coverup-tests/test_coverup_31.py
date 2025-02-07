# file: semantic_release/ci_checks.py:91-100
# asked: {"lines": [91, 92, 99, 100], "branches": []}
# gained: {"lines": [91, 92, 99, 100], "branches": []}

import os
import pytest
from semantic_release.ci_checks import bitbucket
from semantic_release.errors import CiVerificationError

def test_bitbucket_correct_branch(monkeypatch):
    # Setup the environment variables
    monkeypatch.setenv('BITBUCKET_BRANCH', 'main')
    monkeypatch.delenv('BITBUCKET_PR_ID', raising=False)
    
    # Call the function with the correct branch
    bitbucket('main')
    
    # Assertions are within the function, so if no assertion error is raised, the test passes

def test_bitbucket_incorrect_branch(monkeypatch):
    # Setup the environment variables
    monkeypatch.setenv('BITBUCKET_BRANCH', 'develop')
    monkeypatch.delenv('BITBUCKET_PR_ID', raising=False)
    
    # Call the function with the incorrect branch and check for CiVerificationError
    with pytest.raises(CiVerificationError):
        bitbucket('main')

def test_bitbucket_with_pr_id(monkeypatch):
    # Setup the environment variables
    monkeypatch.setenv('BITBUCKET_BRANCH', 'main')
    monkeypatch.setenv('BITBUCKET_PR_ID', '123')
    
    # Call the function and check for CiVerificationError due to PR ID being set
    with pytest.raises(CiVerificationError):
        bitbucket('main')
