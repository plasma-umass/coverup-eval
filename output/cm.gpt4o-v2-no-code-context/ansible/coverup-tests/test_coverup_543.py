# file: lib/ansible/parsing/dataloader.py:399-407
# asked: {"lines": [399, 405, 406, 407], "branches": [[405, 0], [405, 406]]}
# gained: {"lines": [399, 405, 406, 407], "branches": [[405, 0], [405, 406]]}

import os
import pytest
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader._tempfiles = set()
    return loader

def test_cleanup_tmp_file_removes_file(dataloader, tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "tempfile.txt"
    temp_file.touch()
    
    # Add the temporary file to the _tempfiles set
    dataloader._tempfiles.add(str(temp_file))
    
    # Ensure the file exists
    assert temp_file.exists()
    
    # Call the cleanup_tmp_file method
    dataloader.cleanup_tmp_file(str(temp_file))
    
    # Ensure the file is removed
    assert not temp_file.exists()
    
    # Ensure the file is removed from the _tempfiles set
    assert str(temp_file) not in dataloader._tempfiles

def test_cleanup_tmp_file_no_action(dataloader, tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "tempfile.txt"
    temp_file.touch()
    
    # Ensure the file exists
    assert temp_file.exists()
    
    # Call the cleanup_tmp_file method with a file not in _tempfiles
    dataloader.cleanup_tmp_file(str(temp_file))
    
    # Ensure the file still exists
    assert temp_file.exists()
    
    # Ensure the file is not in the _tempfiles set
    assert str(temp_file) not in dataloader._tempfiles
