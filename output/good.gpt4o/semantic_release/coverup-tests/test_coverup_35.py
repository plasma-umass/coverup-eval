# file semantic_release/ci_checks.py:67-76
# lines [67, 68, 75, 76]
# branches []

import os
import pytest
from unittest import mock
from semantic_release.ci_checks import circle
from semantic_release.errors import CiVerificationError

def test_circle_branch(mocker):
    # Set up the environment variables
    mocker.patch.dict(os.environ, {"CIRCLE_BRANCH": "main", "CI_PULL_REQUEST": ""})
    
    # Call the function with the expected branch
    circle("main")
    
    # Assertions are within the function, so if no assertion error is raised, the test passes

def test_circle_branch_fail_branch(mocker):
    # Set up the environment variables with a different branch
    mocker.patch.dict(os.environ, {"CIRCLE_BRANCH": "develop", "CI_PULL_REQUEST": ""})
    
    # Call the function with a different branch, expecting a CiVerificationError
    with pytest.raises(CiVerificationError):
        circle("main")

def test_circle_branch_fail_pull_request(mocker):
    # Set up the environment variables with a pull request
    mocker.patch.dict(os.environ, {"CIRCLE_BRANCH": "main", "CI_PULL_REQUEST": "1"})
    
    # Call the function, expecting a CiVerificationError
    with pytest.raises(CiVerificationError):
        circle("main")
