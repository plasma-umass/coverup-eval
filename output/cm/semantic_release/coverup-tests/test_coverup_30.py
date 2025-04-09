# file semantic_release/ci_checks.py:30-39
# lines [30, 31, 38, 39]
# branches []

import os
import pytest
from semantic_release.ci_checks import travis, CiVerificationError
from unittest.mock import patch

def test_travis_success(mocker):
    mocker.patch.dict(os.environ, {"TRAVIS_BRANCH": "main", "TRAVIS_PULL_REQUEST": "false"})
    assert travis("main") is True

def test_travis_failure_branch(mocker):
    mocker.patch.dict(os.environ, {"TRAVIS_BRANCH": "other", "TRAVIS_PULL_REQUEST": "false"})
    with pytest.raises(CiVerificationError):
        travis("main")

def test_travis_failure_pull_request(mocker):
    mocker.patch.dict(os.environ, {"TRAVIS_BRANCH": "main", "TRAVIS_PULL_REQUEST": "true"})
    with pytest.raises(CiVerificationError):
        travis("main")
