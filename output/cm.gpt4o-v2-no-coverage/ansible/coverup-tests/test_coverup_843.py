# file: lib/ansible/parsing/dataloader.py:116-118
# asked: {"lines": [116, 117, 118], "branches": []}
# gained: {"lines": [116, 117, 118], "branches": []}

import os
import pytest
from ansible.module_utils._text import to_bytes, to_text
from ansible.parsing.quoting import unquote
from ansible.utils.path import unfrackpath
from ansible.parsing.dataloader import DataLoader

class MockDataLoader(DataLoader):
    def __init__(self, basedir):
        self._basedir = basedir

@pytest.fixture
def dataloader(tmp_path):
    basedir = tmp_path / "basedir"
    basedir.mkdir()
    return MockDataLoader(basedir)

def test_is_directory_with_absolute_path(dataloader, tmp_path):
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    assert dataloader.is_directory(str(test_dir)) is True

def test_is_directory_with_relative_path(dataloader, tmp_path):
    test_dir = tmp_path / "basedir" / "test_dir"
    test_dir.mkdir()
    assert dataloader.is_directory("test_dir") is True

def test_is_directory_with_nonexistent_path(dataloader):
    assert dataloader.is_directory("nonexistent_dir") is False

def test_is_directory_with_home_path(monkeypatch, dataloader, tmp_path):
    home_dir = tmp_path / "home"
    home_dir.mkdir()
    monkeypatch.setenv("HOME", str(home_dir))
    home_test_dir = home_dir / "test_dir"
    home_test_dir.mkdir()
    assert dataloader.is_directory("~/test_dir") is True
