# file lib/ansible/parsing/dataloader.py:399-407
# lines []
# branches ['405->exit']

import os
import pytest
from ansible.parsing.dataloader import DataLoader

# Test function to cover the missing branch 405->exit
def test_cleanup_tmp_file_not_in_tempfiles(mocker):
    # Setup
    data_loader = DataLoader()
    data_loader._tempfiles = set()

    # Create a temporary file but do not add it to the DataLoader's _tempfiles
    temp_file = 'temp_file_for_testing.dat'
    with open(temp_file, 'w') as f:
        f.write('temporary content')

    assert os.path.exists(temp_file)
    assert temp_file not in data_loader._tempfiles

    # Mock os.unlink to ensure it is not called
    mocked_unlink = mocker.patch('os.unlink')

    # Execute the method to be tested
    data_loader.cleanup_tmp_file(temp_file)

    # Assert postconditions
    mocked_unlink.assert_not_called()
    assert temp_file not in data_loader._tempfiles

    # Cleanup
    if os.path.exists(temp_file):
        os.unlink(temp_file)
