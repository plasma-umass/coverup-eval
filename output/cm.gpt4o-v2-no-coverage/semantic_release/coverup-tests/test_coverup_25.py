# file: semantic_release/ci_checks.py:67-76
# asked: {"lines": [67, 68, 75, 76], "branches": []}
# gained: {"lines": [67, 68, 75, 76], "branches": []}

import os
import pytest
from semantic_release.ci_checks import circle
from semantic_release.errors import CiVerificationError

def test_circle_pass(monkeypatch):
    monkeypatch.setenv('CIRCLE_BRANCH', 'main')
    monkeypatch.setenv('CI_PULL_REQUEST', '')

    assert circle('main') == True

def test_circle_fail_branch(monkeypatch):
    monkeypatch.setenv('CIRCLE_BRANCH', 'dev')
    monkeypatch.setenv('CI_PULL_REQUEST', '')

    with pytest.raises(CiVerificationError):
        circle('main')

def test_circle_fail_pull_request(monkeypatch):
    monkeypatch.setenv('CIRCLE_BRANCH', 'main')
    monkeypatch.setenv('CI_PULL_REQUEST', '1')

    with pytest.raises(CiVerificationError):
        circle('main')
