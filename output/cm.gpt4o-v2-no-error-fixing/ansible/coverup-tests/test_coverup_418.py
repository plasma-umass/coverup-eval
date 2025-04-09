# file: lib/ansible/parsing/dataloader.py:399-407
# asked: {"lines": [399, 405, 406, 407], "branches": [[405, 0], [405, 406]]}
# gained: {"lines": [399, 405, 406, 407], "branches": [[405, 0], [405, 406]]}

import pytest
import os
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_cleanup_tmp_file_removes_file(dataloader, tmp_path, mocker):
    # Create a temporary file
    temp_file = tmp_path / "tempfile.txt"
    temp_file.touch()
    
    # Add the temporary file to the _tempfiles set
    dataloader._tempfiles.add(str(temp_file))
    
    # Mock os.unlink to avoid actually deleting the file
    mocker.patch("os.unlink")
    
    # Call the method
    dataloader.cleanup_tmp_file(str(temp_file))
    
    # Assert the file was unlinked and removed from _tempfiles
    os.unlink.assert_called_once_with(str(temp_file))
    assert str(temp_file) not in dataloader._tempfiles

def test_cleanup_tmp_file_no_action(dataloader, tmp_path, mocker):
    # Create a temporary file path
    temp_file = tmp_path / "tempfile.txt"
    
    # Ensure the file is not in the _tempfiles set
    assert str(temp_file) not in dataloader._tempfiles
    
    # Mock os.unlink to ensure it is not called
    mocker.patch("os.unlink")
    
    # Call the method
    dataloader.cleanup_tmp_file(str(temp_file))
    
    # Assert os.unlink was not called
    os.unlink.assert_not_called()
