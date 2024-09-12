# file: semantic_release/ci_checks.py:55-64
# asked: {"lines": [55, 56, 63, 64], "branches": []}
# gained: {"lines": [55, 56, 63, 64], "branches": []}

import os
import pytest
from semantic_release.ci_checks import frigg
from semantic_release.errors import CiVerificationError

def test_frigg_correct_branch(monkeypatch):
    # Setup the environment variables
    monkeypatch.setenv('FRIGG_BUILD_BRANCH', 'main')
    monkeypatch.setenv('FRIGG_PULL_REQUEST', '')

    # Call the function with the correct branch
    frigg('main')

def test_frigg_incorrect_branch(monkeypatch):
    # Setup the environment variables
    monkeypatch.setenv('FRIGG_BUILD_BRANCH', 'develop')
    monkeypatch.setenv('FRIGG_PULL_REQUEST', '')

    # Call the function with the incorrect branch and expect a CiVerificationError
    with pytest.raises(CiVerificationError):
        frigg('main')

def test_frigg_pull_request(monkeypatch):
    # Setup the environment variables
    monkeypatch.setenv('FRIGG_BUILD_BRANCH', 'main')
    monkeypatch.setenv('FRIGG_PULL_REQUEST', '1')

    # Call the function and expect a CiVerificationError due to pull request
    with pytest.raises(CiVerificationError):
        frigg('main')
