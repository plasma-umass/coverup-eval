# file semantic_release/ci_checks.py:103-115
# lines [103, 104, 112, 113, 114, 115]
# branches []

import os
import pytest
from semantic_release.ci_checks import jenkins
from semantic_release.errors import CiVerificationError
from unittest.mock import patch

def test_jenkins_success(mocker):
    mocker.patch.dict(os.environ, {
        "JENKINS_URL": "http://example.com",
        "BRANCH_NAME": "main",
    })
    jenkins("main")

def test_jenkins_failure_wrong_branch(mocker):
    mocker.patch.dict(os.environ, {
        "JENKINS_URL": "http://example.com",
        "BRANCH_NAME": "feature",
    })
    with pytest.raises(CiVerificationError):
        jenkins("main")

def test_jenkins_failure_no_jenkins_url(mocker):
    mocker.patch.dict(os.environ, {
        "BRANCH_NAME": "main",
    }, clear=True)
    with pytest.raises(CiVerificationError):
        jenkins("main")

def test_jenkins_failure_pull_request(mocker):
    mocker.patch.dict(os.environ, {
        "JENKINS_URL": "http://example.com",
        "BRANCH_NAME": "main",
        "CHANGE_ID": "123",
    })
    with pytest.raises(CiVerificationError):
        jenkins("main")

def test_jenkins_git_branch(mocker):
    mocker.patch.dict(os.environ, {
        "JENKINS_URL": "http://example.com",
        "GIT_BRANCH": "main",
    })
    jenkins("main")

# Ensure that the environment is clean after tests
@pytest.fixture(autouse=True)
def clean_environment():
    original_environ = os.environ.copy()
    yield
    os.environ.clear()
    os.environ.update(original_environ)
