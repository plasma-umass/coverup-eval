# file: lib/ansible/parsing/dataloader.py:112-114
# asked: {"lines": [112, 113, 114], "branches": []}
# gained: {"lines": [112, 113, 114], "branches": []}

import os
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_bytes

@pytest.fixture
def dataloader():
    return DataLoader()

def test_is_file_with_existing_file(monkeypatch, tmp_path, dataloader):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("content")

    def mock_path_dwim(path):
        return str(test_file)

    monkeypatch.setattr(dataloader, "path_dwim", mock_path_dwim)
    assert dataloader.is_file(str(test_file)) is True

def test_is_file_with_non_existing_file(monkeypatch, tmp_path, dataloader):
    test_file = tmp_path / "non_existing_file.txt"

    def mock_path_dwim(path):
        return str(test_file)

    monkeypatch.setattr(dataloader, "path_dwim", mock_path_dwim)
    assert dataloader.is_file(str(test_file)) is False

def test_is_file_with_devnull(monkeypatch, dataloader):
    def mock_path_dwim(path):
        return os.devnull

    monkeypatch.setattr(dataloader, "path_dwim", mock_path_dwim)
    assert dataloader.is_file(os.devnull) is True
