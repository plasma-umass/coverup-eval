# file: semantic_release/ci_checks.py:118-138
# asked: {"lines": [118, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138], "branches": [[125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 137], [137, 0], [137, 138]]}
# gained: {"lines": [118, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138], "branches": [[125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 137], [137, 138]]}

import os
import pytest
from semantic_release.ci_checks import check

def mock_travis(branch):
    assert branch == "master"

def mock_semaphore(branch):
    assert branch == "master"

def mock_frigg(branch):
    assert branch == "master"

def mock_circle(branch):
    assert branch == "master"

def mock_gitlab(branch):
    assert branch == "master"

def mock_jenkins(branch):
    assert branch == "master"

def mock_bitbucket(branch):
    assert branch == "master"

@pytest.fixture(autouse=True)
def mock_ci_functions(monkeypatch):
    monkeypatch.setattr('semantic_release.ci_checks.travis', mock_travis)
    monkeypatch.setattr('semantic_release.ci_checks.semaphore', mock_semaphore)
    monkeypatch.setattr('semantic_release.ci_checks.frigg', mock_frigg)
    monkeypatch.setattr('semantic_release.ci_checks.circle', mock_circle)
    monkeypatch.setattr('semantic_release.ci_checks.gitlab', mock_gitlab)
    monkeypatch.setattr('semantic_release.ci_checks.jenkins', mock_jenkins)
    monkeypatch.setattr('semantic_release.ci_checks.bitbucket', mock_bitbucket)

def test_check_travis(monkeypatch):
    monkeypatch.setenv("TRAVIS", "true")
    check()
    monkeypatch.delenv("TRAVIS")

def test_check_semaphore(monkeypatch):
    monkeypatch.setenv("SEMAPHORE", "true")
    check()
    monkeypatch.delenv("SEMAPHORE")

def test_check_frigg(monkeypatch):
    monkeypatch.setenv("FRIGG", "true")
    check()
    monkeypatch.delenv("FRIGG")

def test_check_circle(monkeypatch):
    monkeypatch.setenv("CIRCLECI", "true")
    check()
    monkeypatch.delenv("CIRCLECI")

def test_check_gitlab(monkeypatch):
    monkeypatch.setenv("GITLAB_CI", "true")
    check()
    monkeypatch.delenv("GITLAB_CI")

def test_check_jenkins(monkeypatch):
    monkeypatch.setenv("JENKINS_URL", "http://jenkins.example.com")
    check()
    monkeypatch.delenv("JENKINS_URL")

def test_check_bitbucket(monkeypatch):
    monkeypatch.setenv("BITBUCKET_BUILD_NUMBER", "123")
    check()
    monkeypatch.delenv("BITBUCKET_BUILD_NUMBER")
