# file semantic_release/ci_checks.py:103-115
# lines [103, 104, 112, 113, 114, 115]
# branches []

import os
import pytest
from unittest import mock
from semantic_release.ci_checks import jenkins

def test_jenkins(mocker):
    # Set up the environment variables
    mocker.patch.dict(os.environ, {
        "JENKINS_URL": "http://example.com",
        "BRANCH_NAME": "main",
        "GIT_BRANCH": "main",
        "CHANGE_ID": ""
    })

    # Call the jenkins function with the expected branch name
    jenkins("main")

    # Assertions to verify the environment variables are set correctly
    assert os.environ["JENKINS_URL"] == "http://example.com"
    assert os.environ["BRANCH_NAME"] == "main" or os.environ["GIT_BRANCH"] == "main"
    assert os.environ["CHANGE_ID"] == ""

    # Clean up the environment variables
    mocker.stopall()
