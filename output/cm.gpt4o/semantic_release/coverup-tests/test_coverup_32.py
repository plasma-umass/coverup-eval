# file semantic_release/ci_checks.py:79-87
# lines [79, 80, 87]
# branches []

import os
import pytest
from semantic_release.ci_checks import gitlab
from semantic_release.errors import CiVerificationError

def test_gitlab_checker(mocker):
    # Mock the environment variable
    mocker.patch.dict(os.environ, {"CI_COMMIT_REF_NAME": "main"})
    
    # Call the gitlab function with the expected branch name
    gitlab("main")
    
    # Assert that the function does not raise an assertion error
    try:
        gitlab("main")
    except CiVerificationError:
        pytest.fail("gitlab function raised CiVerificationError unexpectedly!")
    
    # Test with a different branch name to ensure the assertion fails
    with pytest.raises(CiVerificationError):
        gitlab("develop")
