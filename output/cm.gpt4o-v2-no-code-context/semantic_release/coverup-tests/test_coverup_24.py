# file: semantic_release/ci_checks.py:79-87
# asked: {"lines": [79, 80, 87], "branches": []}
# gained: {"lines": [79, 80, 87], "branches": []}

import os
import pytest
from semantic_release.ci_checks import gitlab
from semantic_release.errors import CiVerificationError

def test_gitlab_branch_match(monkeypatch):
    branch_name = "main"
    monkeypatch.setenv("CI_COMMIT_REF_NAME", branch_name)
    assert gitlab(branch_name) is True

def test_gitlab_branch_mismatch(monkeypatch):
    branch_name = "main"
    monkeypatch.setenv("CI_COMMIT_REF_NAME", "develop")
    with pytest.raises(CiVerificationError):
        gitlab(branch_name)
