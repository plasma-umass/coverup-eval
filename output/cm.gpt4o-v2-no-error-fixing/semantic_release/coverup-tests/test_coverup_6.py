# file: semantic_release/ci_checks.py:91-100
# asked: {"lines": [91, 92, 99, 100], "branches": []}
# gained: {"lines": [91, 92, 99, 100], "branches": []}

import os
import pytest
from semantic_release.ci_checks import bitbucket
from semantic_release.errors import CiVerificationError

def test_bitbucket_pass(monkeypatch):
    monkeypatch.setenv('BITBUCKET_BRANCH', 'main')
    monkeypatch.delenv('BITBUCKET_PR_ID', raising=False)
    
    assert bitbucket('main') == True

def test_bitbucket_fail_branch(monkeypatch):
    monkeypatch.setenv('BITBUCKET_BRANCH', 'dev')
    monkeypatch.delenv('BITBUCKET_PR_ID', raising=False)
    
    with pytest.raises(CiVerificationError):
        bitbucket('main')

def test_bitbucket_fail_pr_id(monkeypatch):
    monkeypatch.setenv('BITBUCKET_BRANCH', 'main')
    monkeypatch.setenv('BITBUCKET_PR_ID', '123')
    
    with pytest.raises(CiVerificationError):
        bitbucket('main')
