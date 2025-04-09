# file: semantic_release/ci_checks.py:30-39
# asked: {"lines": [30, 31, 38, 39], "branches": []}
# gained: {"lines": [30, 31, 38, 39], "branches": []}

import os
import pytest
from semantic_release.ci_checks import travis
from semantic_release.errors import CiVerificationError

def test_travis_correct_branch_and_not_pull_request(monkeypatch):
    monkeypatch.setenv('TRAVIS_BRANCH', 'main')
    monkeypatch.setenv('TRAVIS_PULL_REQUEST', 'false')
    assert travis('main') is True

def test_travis_incorrect_branch(monkeypatch):
    monkeypatch.setenv('TRAVIS_BRANCH', 'dev')
    monkeypatch.setenv('TRAVIS_PULL_REQUEST', 'false')
    with pytest.raises(CiVerificationError):
        travis('main')

def test_travis_pull_request(monkeypatch):
    monkeypatch.setenv('TRAVIS_BRANCH', 'main')
    monkeypatch.setenv('TRAVIS_PULL_REQUEST', 'true')
    with pytest.raises(CiVerificationError):
        travis('main')
