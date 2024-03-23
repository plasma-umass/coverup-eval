# file lib/ansible/module_utils/urls.py:885-891
# lines [885, 886, 887, 888, 889, 891]
# branches ['886->exit', '886->887']

import os
import pytest
from ansible.module_utils.urls import atexit_remove_file

def test_atexit_remove_file_existing_file(mocker):
    # Setup: create a temporary file
    temp_file = 'temp_test_file.txt'
    with open(temp_file, 'w') as f:
        f.write('temporary file content')

    # Ensure the file exists before we try to remove it
    assert os.path.exists(temp_file)

    # Mock os.unlink to raise an exception to test the exception handling
    mocker.patch('os.unlink', side_effect=Exception('Mocked exception'))

    # Call the function that should handle the exception
    atexit_remove_file(temp_file)

    # The file should still exist because the exception was caught
    assert os.path.exists(temp_file)

    # Cleanup: remove the temporary file
    # Stop the mock to ensure the actual os.unlink is called
    mocker.stopall()
    os.unlink(temp_file)
    assert not os.path.exists(temp_file)

def test_atexit_remove_file_non_existing_file():
    # Setup: ensure the file does not exist
    temp_file = 'non_existing_temp_file.txt'
    assert not os.path.exists(temp_file)

    # Call the function with a non-existing file, which should be a no-op
    atexit_remove_file(temp_file)

    # No assertion needed, as the function should handle non-existing files gracefully
