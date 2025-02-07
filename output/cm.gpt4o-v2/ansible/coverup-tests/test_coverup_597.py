# file: lib/ansible/config/manager.py:162-167
# asked: {"lines": [162, 164, 165, 167], "branches": [[164, 165], [164, 167]]}
# gained: {"lines": [162, 164, 165, 167], "branches": [[164, 165], [164, 167]]}

import os
import pytest
from ansible.config.manager import resolve_path
from ansible.utils.path import unfrackpath

def test_resolve_path_with_cwd(monkeypatch):
    test_path = "{{CWD}}/test"
    expected_path = os.path.join(os.getcwd(), "test")

    def mock_unfrackpath(path, follow, basedir):
        assert path == expected_path
        assert follow is False
        assert basedir is None
        return path

    monkeypatch.setattr('ansible.utils.path.unfrackpath', mock_unfrackpath)
    result = resolve_path(test_path)
    assert result == expected_path

def test_resolve_path_without_cwd(monkeypatch):
    test_path = "/test"
    expected_path = test_path

    def mock_unfrackpath(path, follow, basedir):
        assert path == expected_path
        assert follow is False
        assert basedir is None
        return path

    monkeypatch.setattr('ansible.utils.path.unfrackpath', mock_unfrackpath)
    result = resolve_path(test_path)
    assert result == expected_path
