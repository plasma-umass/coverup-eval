# file: semantic_release/ci_checks.py:55-64
# asked: {"lines": [55, 56, 63, 64], "branches": []}
# gained: {"lines": [55, 56, 63, 64], "branches": []}

import os
import pytest
from semantic_release.ci_checks import frigg, CiVerificationError

def test_frigg_pass(monkeypatch):
    monkeypatch.setenv("FRIGG_BUILD_BRANCH", "main")
    monkeypatch.delenv("FRIGG_PULL_REQUEST", raising=False)
    assert frigg("main") is True

def test_frigg_fail_branch(monkeypatch):
    monkeypatch.setenv("FRIGG_BUILD_BRANCH", "dev")
    monkeypatch.delenv("FRIGG_PULL_REQUEST", raising=False)
    with pytest.raises(CiVerificationError):
        frigg("main")

def test_frigg_fail_pull_request(monkeypatch):
    monkeypatch.setenv("FRIGG_BUILD_BRANCH", "main")
    monkeypatch.setenv("FRIGG_PULL_REQUEST", "1")
    with pytest.raises(CiVerificationError):
        frigg("main")
