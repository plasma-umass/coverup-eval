# file semantic_release/ci_checks.py:55-64
# lines [55, 56, 63, 64]
# branches []

import os
import pytest
from semantic_release.ci_checks import frigg

def test_frigg(mocker):
    # Set up the environment variables
    mocker.patch.dict(os.environ, {
        "FRIGG_BUILD_BRANCH": "main",
        "FRIGG_PULL_REQUEST": ""
    })

    # Call the frigg function with the expected branch
    frigg("main")

    # Assertions are within the frigg function, so no need for additional assertions here
