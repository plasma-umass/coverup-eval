# file: lib/ansible/parsing/dataloader.py:399-407
# asked: {"lines": [399, 405, 406, 407], "branches": [[405, 0], [405, 406]]}
# gained: {"lines": [399, 405, 406, 407], "branches": [[405, 0], [405, 406]]}

import pytest
import os
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_cleanup_tmp_file_removes_file(dataloader, tmp_path, monkeypatch):
    # Create a temporary file
    temp_file = tmp_path / "tempfile.txt"
    temp_file.write_text("Temporary file content")

    # Add the temporary file to the _tempfiles set
    dataloader._tempfiles.add(str(temp_file))

    # Ensure the file exists
    assert temp_file.exists()

    # Mock os.unlink to avoid actually deleting the file
    def mock_unlink(path):
        assert path == str(temp_file)
    monkeypatch.setattr(os, "unlink", mock_unlink)

    # Call cleanup_tmp_file
    dataloader.cleanup_tmp_file(str(temp_file))

    # Ensure the file was removed from _tempfiles
    assert str(temp_file) not in dataloader._tempfiles

def test_cleanup_tmp_file_no_action(dataloader, tmp_path, monkeypatch):
    # Create a temporary file
    temp_file = tmp_path / "tempfile.txt"
    temp_file.write_text("Temporary file content")

    # Ensure the file exists
    assert temp_file.exists()

    # Mock os.unlink to ensure it is not called
    def mock_unlink(path):
        raise AssertionError("os.unlink should not be called")
    monkeypatch.setattr(os, "unlink", mock_unlink)

    # Call cleanup_tmp_file with a file not in _tempfiles
    dataloader.cleanup_tmp_file(str(temp_file))

    # Ensure the file is still not in _tempfiles
    assert str(temp_file) not in dataloader._tempfiles
