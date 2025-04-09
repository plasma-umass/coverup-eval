# file: semantic_release/ci_checks.py:118-138
# asked: {"lines": [], "branches": [[137, 0]]}
# gained: {"lines": [], "branches": [[137, 0]]}

import os
import pytest
from semantic_release.ci_checks import check

def test_check_bitbucket(monkeypatch, mocker):
    # Set up the environment variable for Bitbucket
    monkeypatch.setenv("BITBUCKET_BUILD_NUMBER", "123")
    
    # Mock the bitbucket function to verify it gets called
    mock_bitbucket = mocker.patch("semantic_release.ci_checks.bitbucket")
    
    # Call the check function
    check("master")
    
    # Assert that the bitbucket function was called with the correct branch
    mock_bitbucket.assert_called_once_with("master")
    
    # Clean up the environment variable
    monkeypatch.delenv("BITBUCKET_BUILD_NUMBER")

def test_check_no_ci(monkeypatch, mocker):
    # Ensure no CI environment variables are set
    ci_vars = ["TRAVIS", "SEMAPHORE", "FRIGG", "CIRCLECI", "GITLAB_CI", "JENKINS_URL", "BITBUCKET_BUILD_NUMBER"]
    for var in ci_vars:
        monkeypatch.delenv(var, raising=False)
    
    # Mock all CI functions to verify none get called
    mock_travis = mocker.patch("semantic_release.ci_checks.travis")
    mock_semaphore = mocker.patch("semantic_release.ci_checks.semaphore")
    mock_frigg = mocker.patch("semantic_release.ci_checks.frigg")
    mock_circle = mocker.patch("semantic_release.ci_checks.circle")
    mock_gitlab = mocker.patch("semantic_release.ci_checks.gitlab")
    mock_jenkins = mocker.patch("semantic_release.ci_checks.jenkins")
    mock_bitbucket = mocker.patch("semantic_release.ci_checks.bitbucket")
    
    # Call the check function
    check("master")
    
    # Assert that none of the CI functions were called
    mock_travis.assert_not_called()
    mock_semaphore.assert_not_called()
    mock_frigg.assert_not_called()
    mock_circle.assert_not_called()
    mock_gitlab.assert_not_called()
    mock_jenkins.assert_not_called()
    mock_bitbucket.assert_not_called()
