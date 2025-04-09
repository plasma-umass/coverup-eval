# file: semantic_release/ci_checks.py:42-52
# asked: {"lines": [42, 43, 50, 51, 52], "branches": []}
# gained: {"lines": [42, 43, 50, 51, 52], "branches": []}

import os
import pytest
from semantic_release.ci_checks import semaphore
from semantic_release.errors import CiVerificationError

def test_semaphore_success(monkeypatch):
    # Setup environment variables
    monkeypatch.setenv("BRANCH_NAME", "main")
    monkeypatch.delenv("PULL_REQUEST_NUMBER", raising=False)
    monkeypatch.setenv("SEMAPHORE_THREAD_RESULT", "passed")

    # Call the function with the expected branch
    semaphore("main")

def test_semaphore_wrong_branch(monkeypatch):
    # Setup environment variables
    monkeypatch.setenv("BRANCH_NAME", "develop")
    monkeypatch.delenv("PULL_REQUEST_NUMBER", raising=False)
    monkeypatch.setenv("SEMAPHORE_THREAD_RESULT", "passed")

    # Call the function with a different branch and expect a CiVerificationError
    with pytest.raises(CiVerificationError):
        semaphore("main")

def test_semaphore_pull_request(monkeypatch):
    # Setup environment variables
    monkeypatch.setenv("BRANCH_NAME", "main")
    monkeypatch.setenv("PULL_REQUEST_NUMBER", "123")
    monkeypatch.setenv("SEMAPHORE_THREAD_RESULT", "passed")

    # Call the function and expect a CiVerificationError due to pull request number being set
    with pytest.raises(CiVerificationError):
        semaphore("main")

def test_semaphore_failed_result(monkeypatch):
    # Setup environment variables
    monkeypatch.setenv("BRANCH_NAME", "main")
    monkeypatch.delenv("PULL_REQUEST_NUMBER", raising=False)
    monkeypatch.setenv("SEMAPHORE_THREAD_RESULT", "failed")

    # Call the function and expect a CiVerificationError due to failed result
    with pytest.raises(CiVerificationError):
        semaphore("main")
