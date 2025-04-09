# file: semantic_release/ci_checks.py:118-138
# asked: {"lines": [118, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138], "branches": [[125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 137], [137, 0], [137, 138]]}
# gained: {"lines": [118, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138], "branches": [[125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 137], [137, 138]]}

import os
import pytest
from semantic_release.ci_checks import check

def test_check_travis(monkeypatch):
    monkeypatch.setenv("TRAVIS", "true")
    monkeypatch.setenv("TRAVIS_BRANCH", "master")
    monkeypatch.setenv("TRAVIS_PULL_REQUEST", "false")
    check("master")

def test_check_semaphore(monkeypatch):
    monkeypatch.setenv("SEMAPHORE", "true")
    monkeypatch.setenv("BRANCH_NAME", "master")
    monkeypatch.delenv("PULL_REQUEST_NUMBER", raising=False)
    monkeypatch.setenv("SEMAPHORE_THREAD_RESULT", "passed")
    check("master")

def test_check_frigg(monkeypatch):
    monkeypatch.setenv("FRIGG", "true")
    monkeypatch.setenv("FRIGG_BUILD_BRANCH", "master")
    monkeypatch.delenv("FRIGG_PULL_REQUEST", raising=False)
    check("master")

def test_check_circle(monkeypatch):
    monkeypatch.setenv("CIRCLECI", "true")
    monkeypatch.setenv("CIRCLE_BRANCH", "master")
    monkeypatch.delenv("CI_PULL_REQUEST", raising=False)
    check("master")

def test_check_gitlab(monkeypatch):
    monkeypatch.setenv("GITLAB_CI", "true")
    monkeypatch.setenv("CI_COMMIT_REF_NAME", "master")
    check("master")

def test_check_jenkins(monkeypatch):
    monkeypatch.setenv("JENKINS_URL", "http://jenkins.example.com")
    monkeypatch.setenv("BRANCH_NAME", "master")
    monkeypatch.delenv("CHANGE_ID", raising=False)
    check("master")

def test_check_bitbucket(monkeypatch):
    monkeypatch.setenv("BITBUCKET_BUILD_NUMBER", "123")
    monkeypatch.setenv("BITBUCKET_BRANCH", "master")
    monkeypatch.delenv("BITBUCKET_PR_ID", raising=False)
    check("master")
