# file semantic_release/ci_checks.py:118-138
# lines [118, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138]
# branches ['125->126', '125->127', '127->128', '127->129', '129->130', '129->131', '131->132', '131->133', '133->134', '133->135', '135->136', '135->137', '137->exit', '137->138']

import os
from unittest.mock import patch
import pytest

from semantic_release.ci_checks import check

@pytest.fixture
def clean_env():
    # Backup original environment variables
    original_environ = os.environ.copy()
    # Clear environment variables that might affect tests
    keys_to_clear = ["TRAVIS", "SEMAPHORE", "FRIGG", "CIRCLECI", "GITLAB_CI", "JENKINS_URL", "BITBUCKET_BUILD_NUMBER"]
    for key in keys_to_clear:
        os.environ.pop(key, None)
    yield
    # Restore original environment variables after test
    os.environ.clear()
    os.environ.update(original_environ)

def test_check_travis(clean_env):
    with patch('semantic_release.ci_checks.travis') as mock_travis:
        os.environ["TRAVIS"] = "true"
        check()
        mock_travis.assert_called_once_with("master")

def test_check_semaphore(clean_env):
    with patch('semantic_release.ci_checks.semaphore') as mock_semaphore:
        os.environ["SEMAPHORE"] = "true"
        check()
        mock_semaphore.assert_called_once_with("master")

def test_check_frigg(clean_env):
    with patch('semantic_release.ci_checks.frigg') as mock_frigg:
        os.environ["FRIGG"] = "true"
        check()
        mock_frigg.assert_called_once_with("master")

def test_check_circle(clean_env):
    with patch('semantic_release.ci_checks.circle') as mock_circle:
        os.environ["CIRCLECI"] = "true"
        check()
        mock_circle.assert_called_once_with("master")

def test_check_gitlab(clean_env):
    with patch('semantic_release.ci_checks.gitlab') as mock_gitlab:
        os.environ["GITLAB_CI"] = "true"
        check()
        mock_gitlab.assert_called_once_with("master")

def test_check_jenkins(clean_env):
    with patch('semantic_release.ci_checks.jenkins') as mock_jenkins:
        os.environ["JENKINS_URL"] = "http://jenkins.example.com"
        check()
        mock_jenkins.assert_called_once_with("master")

def test_check_bitbucket(clean_env):
    with patch('semantic_release.ci_checks.bitbucket') as mock_bitbucket:
        os.environ["BITBUCKET_BUILD_NUMBER"] = "1234"
        check()
        mock_bitbucket.assert_called_once_with("master")
