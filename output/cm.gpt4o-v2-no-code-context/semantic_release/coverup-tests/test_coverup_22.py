# file: semantic_release/ci_checks.py:118-138
# asked: {"lines": [118, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138], "branches": [[125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 137], [137, 0], [137, 138]]}
# gained: {"lines": [118, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138], "branches": [[125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 137], [137, 138]]}

import os
import pytest
from semantic_release.ci_checks import check

def test_check_travis(monkeypatch, mocker):
    monkeypatch.setenv("TRAVIS", "true")
    travis_mock = mocker.patch("semantic_release.ci_checks.travis")
    check("master")
    travis_mock.assert_called_once_with("master")
    monkeypatch.delenv("TRAVIS")

def test_check_semaphore(monkeypatch, mocker):
    monkeypatch.setenv("SEMAPHORE", "true")
    semaphore_mock = mocker.patch("semantic_release.ci_checks.semaphore")
    check("master")
    semaphore_mock.assert_called_once_with("master")
    monkeypatch.delenv("SEMAPHORE")

def test_check_frigg(monkeypatch, mocker):
    monkeypatch.setenv("FRIGG", "true")
    frigg_mock = mocker.patch("semantic_release.ci_checks.frigg")
    check("master")
    frigg_mock.assert_called_once_with("master")
    monkeypatch.delenv("FRIGG")

def test_check_circleci(monkeypatch, mocker):
    monkeypatch.setenv("CIRCLECI", "true")
    circle_mock = mocker.patch("semantic_release.ci_checks.circle")
    check("master")
    circle_mock.assert_called_once_with("master")
    monkeypatch.delenv("CIRCLECI")

def test_check_gitlab(monkeypatch, mocker):
    monkeypatch.setenv("GITLAB_CI", "true")
    gitlab_mock = mocker.patch("semantic_release.ci_checks.gitlab")
    check("master")
    gitlab_mock.assert_called_once_with("master")
    monkeypatch.delenv("GITLAB_CI")

def test_check_jenkins(monkeypatch, mocker):
    monkeypatch.setenv("JENKINS_URL", "http://jenkins.example.com")
    jenkins_mock = mocker.patch("semantic_release.ci_checks.jenkins")
    check("master")
    jenkins_mock.assert_called_once_with("master")
    monkeypatch.delenv("JENKINS_URL")

def test_check_bitbucket(monkeypatch, mocker):
    monkeypatch.setenv("BITBUCKET_BUILD_NUMBER", "123")
    bitbucket_mock = mocker.patch("semantic_release.ci_checks.bitbucket")
    check("master")
    bitbucket_mock.assert_called_once_with("master")
    monkeypatch.delenv("BITBUCKET_BUILD_NUMBER")
