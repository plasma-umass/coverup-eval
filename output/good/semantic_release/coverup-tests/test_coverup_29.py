# file semantic_release/ci_checks.py:79-87
# lines [79, 80, 87]
# branches []

import os
from unittest.mock import patch
import pytest
from semantic_release.ci_checks import gitlab
from semantic_release.errors import CiVerificationError

@pytest.fixture
def clean_env():
    # Backup original environment variables
    original_env = os.environ.copy()
    yield
    # Restore original environment after test
    os.environ.clear()
    os.environ.update(original_env)

def test_gitlab_ci_check_passes_with_correct_branch(clean_env):
    test_branch = 'main'
    with patch.dict(os.environ, {'CI_COMMIT_REF_NAME': test_branch}):
        # No assertion needed, as the function itself asserts the condition
        gitlab(test_branch)

def test_gitlab_ci_check_fails_with_incorrect_branch(clean_env):
    test_branch = 'main'
    incorrect_branch = 'develop'
    with patch.dict(os.environ, {'CI_COMMIT_REF_NAME': incorrect_branch}):
        with pytest.raises(CiVerificationError):
            gitlab(test_branch)
