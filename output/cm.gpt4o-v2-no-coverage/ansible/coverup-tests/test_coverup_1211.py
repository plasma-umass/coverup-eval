# file: lib/ansible/config/manager.py:162-167
# asked: {"lines": [165], "branches": [[164, 165]]}
# gained: {"lines": [165], "branches": [[164, 165]]}

import os
import pytest
from ansible.utils.path import unfrackpath
from ansible.config.manager import resolve_path

def test_resolve_path_with_cwd(monkeypatch):
    test_path = "{{CWD}}/test"
    fake_cwd = "/fake/cwd"
    
    def mock_getcwd():
        return fake_cwd
    
    monkeypatch.setattr(os, "getcwd", mock_getcwd)
    
    resolved_path = resolve_path(test_path)
    expected_path = unfrackpath(f"{fake_cwd}/test", follow=False)
    
    assert resolved_path == expected_path

def test_resolve_path_without_cwd(monkeypatch):
    test_path = "/test/path"
    
    resolved_path = resolve_path(test_path)
    expected_path = unfrackpath(test_path, follow=False)
    
    assert resolved_path == expected_path

def test_resolve_path_with_basedir(monkeypatch):
    test_path = "relative/path"
    basedir = "/base/dir"
    
    resolved_path = resolve_path(test_path, basedir=basedir)
    expected_path = unfrackpath(test_path, follow=False, basedir=basedir)
    
    assert resolved_path == expected_path
