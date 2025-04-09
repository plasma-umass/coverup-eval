# file: semantic_release/ci_checks.py:103-115
# asked: {"lines": [103, 104, 112, 113, 114, 115], "branches": []}
# gained: {"lines": [103, 104, 112, 113, 114, 115], "branches": []}

import os
import pytest
from semantic_release.ci_checks import jenkins
from semantic_release.errors import CiVerificationError

def test_jenkins_pass(monkeypatch):
    monkeypatch.setenv('JENKINS_URL', 'http://jenkins.example.com')
    monkeypatch.setenv('BRANCH_NAME', 'main')
    monkeypatch.delenv('CHANGE_ID', raising=False)
    
    assert jenkins('main') == True

def test_jenkins_fail_no_jenkins_url(monkeypatch):
    monkeypatch.delenv('JENKINS_URL', raising=False)
    monkeypatch.setenv('BRANCH_NAME', 'main')
    monkeypatch.delenv('CHANGE_ID', raising=False)
    
    with pytest.raises(CiVerificationError):
        jenkins('main')

def test_jenkins_fail_branch_name_mismatch(monkeypatch):
    monkeypatch.setenv('JENKINS_URL', 'http://jenkins.example.com')
    monkeypatch.setenv('BRANCH_NAME', 'develop')
    monkeypatch.delenv('CHANGE_ID', raising=False)
    
    with pytest.raises(CiVerificationError):
        jenkins('main')

def test_jenkins_fail_change_id_present(monkeypatch):
    monkeypatch.setenv('JENKINS_URL', 'http://jenkins.example.com')
    monkeypatch.setenv('BRANCH_NAME', 'main')
    monkeypatch.setenv('CHANGE_ID', '1234')
    
    with pytest.raises(CiVerificationError):
        jenkins('main')
