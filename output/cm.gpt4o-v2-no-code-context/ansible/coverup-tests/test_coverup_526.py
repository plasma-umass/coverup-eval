# file: lib/ansible/config/manager.py:162-167
# asked: {"lines": [162, 164, 165, 167], "branches": [[164, 165], [164, 167]]}
# gained: {"lines": [162, 164, 165, 167], "branches": [[164, 165], [164, 167]]}

import os
import pytest
from ansible.config.manager import resolve_path

def test_resolve_path_with_cwd(monkeypatch):
    test_path = '{{CWD}}/testdir'
    expected_path = os.path.join(os.getcwd(), 'testdir')

    def mock_unfrackpath(path, follow, basedir):
        return path

    monkeypatch.setattr('ansible.config.manager.unfrackpath', mock_unfrackpath)
    result = resolve_path(test_path)
    assert result == expected_path

def test_resolve_path_without_cwd(monkeypatch):
    test_path = '/testdir'
    expected_path = '/testdir'

    def mock_unfrackpath(path, follow, basedir):
        return path

    monkeypatch.setattr('ansible.config.manager.unfrackpath', mock_unfrackpath)
    result = resolve_path(test_path)
    assert result == expected_path
