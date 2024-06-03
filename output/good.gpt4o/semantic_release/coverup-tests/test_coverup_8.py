# file semantic_release/ci_checks.py:30-39
# lines [30, 31, 38, 39]
# branches []

import os
import pytest
from unittest import mock
from semantic_release.ci_checks import travis

def test_travis(mocker):
    # Set up the environment variables
    mocker.patch.dict(os.environ, {
        "TRAVIS_BRANCH": "main",
        "TRAVIS_PULL_REQUEST": "false"
    })

    # Call the travis function with the expected branch
    travis("main")

    # Assertions are within the travis function itself, so no need for additional assertions here

    # Clean up the environment variables
    mocker.stopall()
