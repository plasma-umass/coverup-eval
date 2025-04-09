# file: lib/ansible/parsing/dataloader.py:399-407
# asked: {"lines": [399, 405, 406, 407], "branches": [[405, 0], [405, 406]]}
# gained: {"lines": [399, 405, 406, 407], "branches": [[405, 0], [405, 406]]}

import os
import pytest
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_cleanup_tmp_file_removes_file(mocker, dataloader):
    # Setup
    mocker.patch('os.unlink')
    temp_file = '/tmp/testfile'
    dataloader._tempfiles.add(temp_file)
    
    # Exercise
    dataloader.cleanup_tmp_file(temp_file)
    
    # Verify
    os.unlink.assert_called_once_with(temp_file)
    assert temp_file not in dataloader._tempfiles

def test_cleanup_tmp_file_noop(dataloader):
    # Setup
    temp_file = '/tmp/nonexistentfile'
    
    # Exercise
    dataloader.cleanup_tmp_file(temp_file)
    
    # Verify
    assert temp_file not in dataloader._tempfiles
