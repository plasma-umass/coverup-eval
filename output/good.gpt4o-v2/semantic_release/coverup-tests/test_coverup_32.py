# file: semantic_release/ci_checks.py:79-87
# asked: {"lines": [79, 80, 87], "branches": []}
# gained: {"lines": [79, 80, 87], "branches": []}

import os
import pytest
from semantic_release.ci_checks import gitlab
from semantic_release.errors import CiVerificationError

def test_gitlab_correct_branch(monkeypatch):
    # Set up the environment variable
    monkeypatch.setenv('CI_COMMIT_REF_NAME', 'main')
    
    # Call the function with the matching branch name
    gitlab('main')
    
    # Clean up the environment variable
    monkeypatch.delenv('CI_COMMIT_REF_NAME')

def test_gitlab_incorrect_branch(monkeypatch):
    # Set up the environment variable
    monkeypatch.setenv('CI_COMMIT_REF_NAME', 'develop')
    
    # Call the function with a different branch name and assert it raises a CiVerificationError
    with pytest.raises(CiVerificationError):
        gitlab('main')
    
    # Clean up the environment variable
    monkeypatch.delenv('CI_COMMIT_REF_NAME')
