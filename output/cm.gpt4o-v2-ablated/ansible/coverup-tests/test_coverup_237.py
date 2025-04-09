# file: lib/ansible/config/manager.py:162-167
# asked: {"lines": [162, 164, 165, 167], "branches": [[164, 165], [164, 167]]}
# gained: {"lines": [162, 164, 165, 167], "branches": [[164, 165], [164, 167]]}

import os
import pytest
from ansible.config.manager import resolve_path
from ansible.utils.path import unfrackpath

@pytest.fixture
def mock_unfrackpath(mocker):
    return mocker.patch('ansible.config.manager.unfrackpath', return_value='/mocked/path')

def test_resolve_path_with_cwd(monkeypatch, mock_unfrackpath):
    mock_cwd = '/mocked/cwd'
    monkeypatch.setattr(os, 'getcwd', lambda: mock_cwd)
    path = '{{CWD}}/some/path'
    result = resolve_path(path)
    assert result == '/mocked/path'
    mock_unfrackpath.assert_called_once_with('/mocked/cwd/some/path', follow=False, basedir=None)

def test_resolve_path_without_cwd(mock_unfrackpath):
    path = '/some/absolute/path'
    result = resolve_path(path)
    assert result == '/mocked/path'
    mock_unfrackpath.assert_called_once_with('/some/absolute/path', follow=False, basedir=None)

def test_resolve_path_with_basedir(mock_unfrackpath):
    path = 'relative/path'
    basedir = '/base/dir'
    result = resolve_path(path, basedir=basedir)
    assert result == '/mocked/path'
    mock_unfrackpath.assert_called_once_with('relative/path', follow=False, basedir=basedir)
