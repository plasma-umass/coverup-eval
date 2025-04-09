# file semantic_release/ci_checks.py:67-76
# lines [67, 68, 75, 76]
# branches []

import os
from unittest.mock import patch
import pytest
from semantic_release.ci_checks import circle
from semantic_release.errors import CiVerificationError

@pytest.fixture
def clean_env():
    # Backup original environment variables
    original_circle_branch = os.environ.get("CIRCLE_BRANCH")
    original_ci_pull_request = os.environ.get("CI_PULL_REQUEST")

    # Cleanup environment variables after test
    yield
    if original_circle_branch is not None:
        os.environ["CIRCLE_BRANCH"] = original_circle_branch
    else:
        os.environ.pop("CIRCLE_BRANCH", None)

    if original_ci_pull_request is not None:
        os.environ["CI_PULL_REQUEST"] = original_ci_pull_request
    else:
        os.environ.pop("CI_PULL_REQUEST", None)

def test_circle_check_passes_with_correct_env(clean_env):
    test_branch = 'main'
    with patch.dict(os.environ, {"CIRCLE_BRANCH": test_branch, "CI_PULL_REQUEST": ""}):
        circle(test_branch)  # Should not raise an assertion error

def test_circle_check_fails_with_incorrect_branch(clean_env):
    test_branch = 'main'
    incorrect_branch = 'develop'
    with patch.dict(os.environ, {"CIRCLE_BRANCH": incorrect_branch, "CI_PULL_REQUEST": ""}):
        with pytest.raises(CiVerificationError):
            circle(test_branch)

def test_circle_check_fails_with_pull_request(clean_env):
    test_branch = 'main'
    with patch.dict(os.environ, {"CIRCLE_BRANCH": test_branch, "CI_PULL_REQUEST": "123"}):
        with pytest.raises(CiVerificationError):
            circle(test_branch)
