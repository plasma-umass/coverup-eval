# file semantic_release/ci_checks.py:91-100
# lines [91, 92, 99, 100]
# branches []

import os
import pytest
from semantic_release.ci_checks import bitbucket

def test_bitbucket(mocker):
    # Set up the environment variables
    mocker.patch.dict(os.environ, {"BITBUCKET_BRANCH": "main", "BITBUCKET_PR_ID": ""})
    
    # Call the bitbucket function with the expected branch
    bitbucket("main")
    
    # Assertions are within the bitbucket function, so if no assertion error is raised, the test passes

    # Clean up the environment variables
    mocker.patch.dict(os.environ, {}, clear=True)
