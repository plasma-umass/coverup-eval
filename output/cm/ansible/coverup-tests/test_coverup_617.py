# file lib/ansible/parsing/dataloader.py:399-407
# lines [399, 405, 406, 407]
# branches ['405->exit', '405->406']

import os
import pytest
from ansible.parsing.dataloader import DataLoader

# Test function to improve coverage for DataLoader.cleanup_tmp_file
def test_cleanup_tmp_file(mocker):
    # Setup
    dataloader = DataLoader()
    dataloader._tempfiles = set()

    # Create a temporary file and add it to the DataLoader's _tempfiles
    temp_file = 'temp_file_for_testing'
    with open(temp_file, 'w') as f:
        f.write('temporary content')

    dataloader._tempfiles.add(temp_file)

    # Ensure the file exists before cleanup
    assert os.path.exists(temp_file)
    assert temp_file in dataloader._tempfiles

    # Mock os.unlink to prevent actual file deletion for test isolation
    unlink_mock = mocker.patch('os.unlink')

    # Call the method under test
    dataloader.cleanup_tmp_file(temp_file)

    # Assertions to verify postconditions
    unlink_mock.assert_called_once_with(temp_file)
    assert temp_file not in dataloader._tempfiles

    # Cleanup: remove the temporary file if it still exists
    if os.path.exists(temp_file):
        os.unlink(temp_file)
