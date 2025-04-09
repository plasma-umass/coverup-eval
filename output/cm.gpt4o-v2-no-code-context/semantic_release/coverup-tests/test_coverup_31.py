# file: semantic_release/ci_checks.py:55-64
# asked: {"lines": [55, 56, 63, 64], "branches": []}
# gained: {"lines": [55, 56, 63, 64], "branches": []}

import os
import pytest
from semantic_release.ci_checks import frigg, CiVerificationError

def test_frigg_correct_branch(monkeypatch):
    branch = "main"
    monkeypatch.setenv("FRIGG_BUILD_BRANCH", branch)
    monkeypatch.setenv("FRIGG_PULL_REQUEST", "")
    
    frigg(branch)
    
    assert os.environ.get("FRIGG_BUILD_BRANCH") == branch
    assert not os.environ.get("FRIGG_PULL_REQUEST")

def test_frigg_incorrect_branch(monkeypatch):
    branch = "main"
    monkeypatch.setenv("FRIGG_BUILD_BRANCH", "develop")
    monkeypatch.setenv("FRIGG_PULL_REQUEST", "")
    
    with pytest.raises(CiVerificationError):
        frigg(branch)

def test_frigg_pull_request(monkeypatch):
    branch = "main"
    monkeypatch.setenv("FRIGG_BUILD_BRANCH", branch)
    monkeypatch.setenv("FRIGG_PULL_REQUEST", "1")
    
    with pytest.raises(CiVerificationError):
        frigg(branch)
