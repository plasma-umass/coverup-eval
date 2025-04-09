# file: semantic_release/ci_checks.py:42-52
# asked: {"lines": [42, 43, 50, 51, 52], "branches": []}
# gained: {"lines": [42, 43, 50, 51, 52], "branches": []}

import os
import pytest
from semantic_release.ci_checks import semaphore
from semantic_release.errors import CiVerificationError

def test_semaphore_success(monkeypatch):
    monkeypatch.setenv('BRANCH_NAME', 'main')
    monkeypatch.delenv('PULL_REQUEST_NUMBER', raising=False)
    monkeypatch.setenv('SEMAPHORE_THREAD_RESULT', 'passed')
    
    assert semaphore('main') == True

def test_semaphore_wrong_branch(monkeypatch):
    monkeypatch.setenv('BRANCH_NAME', 'dev')
    monkeypatch.delenv('PULL_REQUEST_NUMBER', raising=False)
    monkeypatch.setenv('SEMAPHORE_THREAD_RESULT', 'passed')
    
    with pytest.raises(CiVerificationError):
        semaphore('main')

def test_semaphore_pull_request(monkeypatch):
    monkeypatch.setenv('BRANCH_NAME', 'main')
    monkeypatch.setenv('PULL_REQUEST_NUMBER', '123')
    monkeypatch.setenv('SEMAPHORE_THREAD_RESULT', 'passed')
    
    with pytest.raises(CiVerificationError):
        semaphore('main')

def test_semaphore_failed_result(monkeypatch):
    monkeypatch.setenv('BRANCH_NAME', 'main')
    monkeypatch.delenv('PULL_REQUEST_NUMBER', raising=False)
    monkeypatch.setenv('SEMAPHORE_THREAD_RESULT', 'failed')
    
    with pytest.raises(CiVerificationError):
        semaphore('main')
