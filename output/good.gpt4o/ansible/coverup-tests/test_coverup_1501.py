# file lib/ansible/module_utils/urls.py:885-891
# lines []
# branches ['886->exit']

import os
import pytest
from unittest import mock
from ansible.module_utils.urls import atexit_remove_file

def test_atexit_remove_file_exists(mocker):
    # Create a temporary file
    temp_filename = 'temp_test_file.txt'
    with open(temp_filename, 'w') as f:
        f.write('Temporary file content')

    # Ensure the file exists
    assert os.path.exists(temp_filename)

    # Mock os.unlink to simulate file deletion
    mock_unlink = mocker.patch('os.unlink', side_effect=None)

    # Call the function
    atexit_remove_file(temp_filename)

    # Assert that os.unlink was called
    mock_unlink.assert_called_once_with(temp_filename)

    # Clean up
    if os.path.exists(temp_filename):
        os.remove(temp_filename)

def test_atexit_remove_file_not_exists(mocker):
    # Define a filename that does not exist
    non_existent_filename = 'non_existent_file.txt'

    # Ensure the file does not exist
    assert not os.path.exists(non_existent_filename)

    # Mock os.unlink to ensure it is not called
    mock_unlink = mocker.patch('os.unlink', side_effect=None)

    # Call the function
    atexit_remove_file(non_existent_filename)

    # Assert that os.unlink was not called
    mock_unlink.assert_not_called()
