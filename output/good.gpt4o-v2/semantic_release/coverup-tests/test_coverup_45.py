# file: semantic_release/ci_checks.py:118-138
# asked: {"lines": [], "branches": [[137, 0]]}
# gained: {"lines": [], "branches": [[137, 0]]}

import os
import pytest
from semantic_release.ci_checks import check

def test_check_bitbucket(monkeypatch):
    # Set up the environment variables for Bitbucket
    monkeypatch.setenv("BITBUCKET_BUILD_NUMBER", "123")
    monkeypatch.setenv("BITBUCKET_BRANCH", "master")
    monkeypatch.delenv("TRAVIS", raising=False)
    monkeypatch.delenv("SEMAPHORE", raising=False)
    monkeypatch.delenv("FRIGG", raising=False)
    monkeypatch.delenv("CIRCLECI", raising=False)
    monkeypatch.delenv("GITLAB_CI", raising=False)
    monkeypatch.delenv("JENKINS_URL", raising=False)
    
    # Call the check function
    check("master")
    
    # Clean up
    monkeypatch.delenv("BITBUCKET_BUILD_NUMBER")
    monkeypatch.delenv("BITBUCKET_BRANCH")

def test_check_travis(monkeypatch):
    # Set up the environment variables for Travis
    monkeypatch.setenv("TRAVIS", "true")
    monkeypatch.setenv("TRAVIS_BRANCH", "master")
    monkeypatch.setenv("TRAVIS_PULL_REQUEST", "false")
    monkeypatch.delenv("BITBUCKET_BUILD_NUMBER", raising=False)
    monkeypatch.delenv("SEMAPHORE", raising=False)
    monkeypatch.delenv("FRIGG", raising=False)
    monkeypatch.delenv("CIRCLECI", raising=False)
    monkeypatch.delenv("GITLAB_CI", raising=False)
    monkeypatch.delenv("JENKINS_URL", raising=False)
    
    # Call the check function
    check("master")
    
    # Clean up
    monkeypatch.delenv("TRAVIS")
    monkeypatch.delenv("TRAVIS_BRANCH")
    monkeypatch.delenv("TRAVIS_PULL_REQUEST")

def test_check_semaphore(monkeypatch):
    # Set up the environment variables for Semaphore
    monkeypatch.setenv("SEMAPHORE", "true")
    monkeypatch.setenv("BRANCH_NAME", "master")
    monkeypatch.delenv("PULL_REQUEST_NUMBER", raising=False)
    monkeypatch.setenv("SEMAPHORE_THREAD_RESULT", "passed")
    monkeypatch.delenv("BITBUCKET_BUILD_NUMBER", raising=False)
    monkeypatch.delenv("TRAVIS", raising=False)
    monkeypatch.delenv("FRIGG", raising=False)
    monkeypatch.delenv("CIRCLECI", raising=False)
    monkeypatch.delenv("GITLAB_CI", raising=False)
    monkeypatch.delenv("JENKINS_URL", raising=False)
    
    # Call the check function
    check("master")
    
    # Clean up
    monkeypatch.delenv("SEMAPHORE")
    monkeypatch.delenv("BRANCH_NAME")
    monkeypatch.delenv("SEMAPHORE_THREAD_RESULT")

def test_check_frigg(monkeypatch):
    # Set up the environment variables for Frigg
    monkeypatch.setenv("FRIGG", "true")
    monkeypatch.setenv("FRIGG_BUILD_BRANCH", "master")
    monkeypatch.delenv("FRIGG_PULL_REQUEST", raising=False)
    monkeypatch.delenv("BITBUCKET_BUILD_NUMBER", raising=False)
    monkeypatch.delenv("TRAVIS", raising=False)
    monkeypatch.delenv("SEMAPHORE", raising=False)
    monkeypatch.delenv("CIRCLECI", raising=False)
    monkeypatch.delenv("GITLAB_CI", raising=False)
    monkeypatch.delenv("JENKINS_URL", raising=False)
    
    # Call the check function
    check("master")
    
    # Clean up
    monkeypatch.delenv("FRIGG")
    monkeypatch.delenv("FRIGG_BUILD_BRANCH")

def test_check_circle(monkeypatch):
    # Set up the environment variables for CircleCI
    monkeypatch.setenv("CIRCLECI", "true")
    monkeypatch.setenv("CIRCLE_BRANCH", "master")
    monkeypatch.delenv("CI_PULL_REQUEST", raising=False)
    monkeypatch.delenv("BITBUCKET_BUILD_NUMBER", raising=False)
    monkeypatch.delenv("TRAVIS", raising=False)
    monkeypatch.delenv("SEMAPHORE", raising=False)
    monkeypatch.delenv("FRIGG", raising=False)
    monkeypatch.delenv("GITLAB_CI", raising=False)
    monkeypatch.delenv("JENKINS_URL", raising=False)
    
    # Call the check function
    check("master")
    
    # Clean up
    monkeypatch.delenv("CIRCLECI")
    monkeypatch.delenv("CIRCLE_BRANCH")

def test_check_gitlab(monkeypatch):
    # Set up the environment variables for GitLab
    monkeypatch.setenv("GITLAB_CI", "true")
    monkeypatch.setenv("CI_COMMIT_REF_NAME", "master")
    monkeypatch.delenv("BITBUCKET_BUILD_NUMBER", raising=False)
    monkeypatch.delenv("TRAVIS", raising=False)
    monkeypatch.delenv("SEMAPHORE", raising=False)
    monkeypatch.delenv("FRIGG", raising=False)
    monkeypatch.delenv("CIRCLECI", raising=False)
    monkeypatch.delenv("JENKINS_URL", raising=False)
    
    # Call the check function
    check("master")
    
    # Clean up
    monkeypatch.delenv("GITLAB_CI")
    monkeypatch.delenv("CI_COMMIT_REF_NAME")

def test_check_jenkins(monkeypatch):
    # Set up the environment variables for Jenkins
    monkeypatch.setenv("JENKINS_URL", "http://jenkins.example.com")
    monkeypatch.setenv("BRANCH_NAME", "master")
    monkeypatch.delenv("CHANGE_ID", raising=False)
    monkeypatch.delenv("BITBUCKET_BUILD_NUMBER", raising=False)
    monkeypatch.delenv("TRAVIS", raising=False)
    monkeypatch.delenv("SEMAPHORE", raising=False)
    monkeypatch.delenv("FRIGG", raising=False)
    monkeypatch.delenv("CIRCLECI", raising=False)
    monkeypatch.delenv("GITLAB_CI", raising=False)
    
    # Call the check function
    check("master")
    
    # Clean up
    monkeypatch.delenv("JENKINS_URL")
    monkeypatch.delenv("BRANCH_NAME")

def test_check_no_ci(monkeypatch):
    # Ensure no CI environment variables are set
    monkeypatch.delenv("TRAVIS", raising=False)
    monkeypatch.delenv("SEMAPHORE", raising=False)
    monkeypatch.delenv("FRIGG", raising=False)
    monkeypatch.delenv("CIRCLECI", raising=False)
    monkeypatch.delenv("GITLAB_CI", raising=False)
    monkeypatch.delenv("JENKINS_URL", raising=False)
    monkeypatch.delenv("BITBUCKET_BUILD_NUMBER", raising=False)
    
    # Call the check function
    check("master")
