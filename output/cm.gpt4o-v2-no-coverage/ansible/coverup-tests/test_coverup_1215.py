# file: lib/ansible/parsing/dataloader.py:108-110
# asked: {"lines": [109, 110], "branches": []}
# gained: {"lines": [109, 110], "branches": []}

import os
import pytest
from ansible.module_utils._text import to_bytes
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_path_exists_with_existing_path(monkeypatch, dataloader):
    def mock_path_dwim(path):
        return path

    def mock_exists(path):
        return True

    monkeypatch.setattr(dataloader, 'path_dwim', mock_path_dwim)
    monkeypatch.setattr(os.path, 'exists', mock_exists)

    assert dataloader.path_exists('/existing/path') is True

def test_path_exists_with_non_existing_path(monkeypatch, dataloader):
    def mock_path_dwim(path):
        return path

    def mock_exists(path):
        return False

    monkeypatch.setattr(dataloader, 'path_dwim', mock_path_dwim)
    monkeypatch.setattr(os.path, 'exists', mock_exists)

    assert dataloader.path_exists('/non/existing/path') is False

def test_path_dwim_with_absolute_path(dataloader):
    path = '/absolute/path'
    result = dataloader.path_dwim(path)
    assert result == path

def test_path_dwim_with_relative_path(monkeypatch, dataloader):
    def mock_unfrackpath(path, follow):
        return path

    monkeypatch.setattr('ansible.parsing.dataloader.unfrackpath', mock_unfrackpath)
    dataloader._basedir = '/base/dir'
    path = 'relative/path'
    result = dataloader.path_dwim(path)
    assert result == '/base/dir/relative/path'
