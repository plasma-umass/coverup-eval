# file semantic_release/ci_checks.py:118-138
# lines [118, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138]
# branches ['125->126', '125->127', '127->128', '127->129', '129->130', '129->131', '131->132', '131->133', '133->134', '133->135', '135->136', '135->137', '137->exit', '137->138']

import os
import pytest
from semantic_release.ci_checks import check

def test_check_travis(mocker):
    mocker.patch.dict(os.environ, {"TRAVIS": "true"})
    mock_travis = mocker.patch("semantic_release.ci_checks.travis")
    check("master")
    mock_travis.assert_called_once_with("master")

def test_check_semaphore(mocker):
    mocker.patch.dict(os.environ, {"SEMAPHORE": "true"})
    mock_semaphore = mocker.patch("semantic_release.ci_checks.semaphore")
    check("master")
    mock_semaphore.assert_called_once_with("master")

def test_check_frigg(mocker):
    mocker.patch.dict(os.environ, {"FRIGG": "true"})
    mock_frigg = mocker.patch("semantic_release.ci_checks.frigg")
    check("master")
    mock_frigg.assert_called_once_with("master")

def test_check_circleci(mocker):
    mocker.patch.dict(os.environ, {"CIRCLECI": "true"})
    mock_circle = mocker.patch("semantic_release.ci_checks.circle")
    check("master")
    mock_circle.assert_called_once_with("master")

def test_check_gitlab(mocker):
    mocker.patch.dict(os.environ, {"GITLAB_CI": "true"})
    mock_gitlab = mocker.patch("semantic_release.ci_checks.gitlab")
    check("master")
    mock_gitlab.assert_called_once_with("master")

def test_check_jenkins(mocker):
    mocker.patch.dict(os.environ, {"JENKINS_URL": "http://jenkins.example.com"})
    mock_jenkins = mocker.patch("semantic_release.ci_checks.jenkins")
    check("master")
    mock_jenkins.assert_called_once_with("master")

def test_check_bitbucket(mocker):
    mocker.patch.dict(os.environ, {"BITBUCKET_BUILD_NUMBER": "123"})
    mock_bitbucket = mocker.patch("semantic_release.ci_checks.bitbucket")
    check("master")
    mock_bitbucket.assert_called_once_with("master")
