# file: flutils/pathutils.py:574-621
# asked: {"lines": [613, 614, 615, 617], "branches": [[603, 0], [610, 608], [612, 613], [614, 615], [614, 617], [618, 0]]}
# gained: {"lines": [613, 614, 617], "branches": [[612, 613], [614, 617]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from flutils.pathutils import path_absent

@pytest.fixture
def mock_normalize_path(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr('flutils.pathutils.normalize_path', mock)
    return mock

def test_path_absent_file(mock_normalize_path, tmp_path):
    # Create a temporary file
    file_path = tmp_path / "test_file"
    file_path.touch()
    
    # Mock normalize_path to return the file path
    mock_normalize_path.return_value = file_path
    
    # Ensure the file exists
    assert file_path.exists()
    
    # Call path_absent
    path_absent(file_path)
    
    # Ensure the file is deleted
    assert not file_path.exists()

def test_path_absent_symlink(mock_normalize_path, tmp_path):
    # Create a temporary file and a symlink to it
    file_path = tmp_path / "test_file"
    file_path.touch()
    symlink_path = tmp_path / "test_symlink"
    symlink_path.symlink_to(file_path)
    
    # Mock normalize_path to return the symlink path
    mock_normalize_path.return_value = symlink_path
    
    # Ensure the symlink exists
    assert symlink_path.exists()
    
    # Call path_absent
    path_absent(symlink_path)
    
    # Ensure the symlink is deleted but the file still exists
    assert not symlink_path.exists()
    assert file_path.exists()

def test_path_absent_directory(mock_normalize_path, tmp_path):
    # Create a temporary directory with files and subdirectories
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    sub_dir_path = dir_path / "sub_dir"
    sub_dir_path.mkdir()
    file_path = dir_path / "test_file"
    file_path.touch()
    sub_file_path = sub_dir_path / "sub_test_file"
    sub_file_path.touch()
    
    # Mock normalize_path to return the directory path
    mock_normalize_path.return_value = dir_path
    
    # Ensure the directory and its contents exist
    assert dir_path.exists()
    assert sub_dir_path.exists()
    assert file_path.exists()
    assert sub_file_path.exists()
    
    # Call path_absent
    path_absent(dir_path)
    
    # Ensure the directory and its contents are deleted
    assert not dir_path.exists()
    assert not sub_dir_path.exists()
    assert not file_path.exists()
    assert not sub_file_path.exists()
