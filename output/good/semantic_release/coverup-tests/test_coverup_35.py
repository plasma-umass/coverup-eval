# file semantic_release/ci_checks.py:42-52
# lines [42, 43, 50, 51, 52]
# branches []

import os
import pytest
from semantic_release.ci_checks import semaphore
from semantic_release.errors import CiVerificationError

@pytest.fixture
def mock_environment(monkeypatch):
    monkeypatch.setenv("BRANCH_NAME", "main")
    monkeypatch.delenv("PULL_REQUEST_NUMBER", raising=False)
    monkeypatch.setenv("SEMAPHORE_THREAD_RESULT", "passed")

def test_semaphore_success(mock_environment):
    assert semaphore("main") is True

def test_semaphore_wrong_branch(mock_environment, monkeypatch):
    monkeypatch.setenv("BRANCH_NAME", "feature")
    with pytest.raises(CiVerificationError):
        semaphore("main")

def test_semaphore_pull_request(mock_environment, monkeypatch):
    monkeypatch.setenv("PULL_REQUEST_NUMBER", "123")
    with pytest.raises(CiVerificationError):
        semaphore("main")

def test_semaphore_build_failed(mock_environment, monkeypatch):
    monkeypatch.setenv("SEMAPHORE_THREAD_RESULT", "failed")
    with pytest.raises(CiVerificationError):
        semaphore("main")
