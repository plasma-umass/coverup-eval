# file: lib/ansible/module_utils/urls.py:885-891
# asked: {"lines": [889, 891], "branches": []}
# gained: {"lines": [889, 891], "branches": []}

import os
import pytest
from unittest import mock

# Assuming the function atexit_remove_file is defined in a module named urls
from ansible.module_utils.urls import atexit_remove_file

def test_atexit_remove_file_exists(mocker):
    # Create a temporary file
    temp_file = 'temp_test_file.txt'
    with open(temp_file, 'w') as f:
        f.write('test')

    # Ensure the file exists
    assert os.path.exists(temp_file)

    # Mock os.unlink to raise an exception
    mocker.patch('os.unlink', side_effect=Exception)

    # Call the function
    atexit_remove_file(temp_file)

    # Ensure the file still exists because unlink raised an exception
    assert os.path.exists(temp_file)

    # Clean up
    os.remove(temp_file)

def test_atexit_remove_file_not_exists(mocker):
    # Ensure the file does not exist
    temp_file = 'non_existent_file.txt'
    if os.path.exists(temp_file):
        os.remove(temp_file)
    assert not os.path.exists(temp_file)

    # Mock os.unlink to ensure it is not called
    mock_unlink = mocker.patch('os.unlink')

    # Call the function
    atexit_remove_file(temp_file)

    # Ensure os.unlink was not called
    mock_unlink.assert_not_called()
