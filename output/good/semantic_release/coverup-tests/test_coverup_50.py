# file semantic_release/ci_checks.py:118-138
# lines []
# branches ['137->exit']

import os
from unittest.mock import patch
import pytest

from semantic_release.ci_checks import check

@pytest.fixture
def clean_env():
    # Backup original environment variables
    original_environ = os.environ.copy()
    yield
    # Restore original environment variables after the test
    os.environ = original_environ

def test_check_no_ci_environment(clean_env):
    # Ensure no CI environment variables are set
    keys_to_delete = ["TRAVIS", "SEMAPHORE", "FRIGG", "CIRCLECI", "GITLAB_CI", "JENKINS_URL", "BITBUCKET_BUILD_NUMBER"]
    for key in keys_to_delete:
        os.environ.pop(key, None)

    with patch('semantic_release.ci_checks.travis') as mock_travis, \
         patch('semantic_release.ci_checks.semaphore') as mock_semaphore, \
         patch('semantic_release.ci_checks.frigg') as mock_frigg, \
         patch('semantic_release.ci_checks.circle') as mock_circle, \
         patch('semantic_release.ci_checks.gitlab') as mock_gitlab, \
         patch('semantic_release.ci_checks.jenkins') as mock_jenkins, \
         patch('semantic_release.ci_checks.bitbucket') as mock_bitbucket:

        check('master')

        mock_travis.assert_not_called()
        mock_semaphore.assert_not_called()
        mock_frigg.assert_not_called()
        mock_circle.assert_not_called()
        mock_gitlab.assert_not_called()
        mock_jenkins.assert_not_called()
        mock_bitbucket.assert_not_called()
