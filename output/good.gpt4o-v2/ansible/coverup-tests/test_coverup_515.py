# file: lib/ansible/module_utils/urls.py:885-891
# asked: {"lines": [885, 886, 887, 888, 889, 891], "branches": [[886, 0], [886, 887]]}
# gained: {"lines": [885, 886, 887, 888], "branches": [[886, 0], [886, 887]]}

import os
import pytest
from unittest import mock

from ansible.module_utils.urls import atexit_remove_file

def test_atexit_remove_file_exists(mocker):
    # Create a temporary file
    temp_file = 'temp_test_file.txt'
    with open(temp_file, 'w') as f:
        f.write('test')

    # Ensure the file exists
    assert os.path.exists(temp_file)

    # Mock os.unlink to ensure it gets called
    mocker.patch('os.unlink')

    # Call the function
    atexit_remove_file(temp_file)

    # Assert os.unlink was called
    os.unlink.assert_called_once_with(temp_file)

    # Clean up
    if os.path.exists(temp_file):
        os.remove(temp_file)

def test_atexit_remove_file_not_exists(mocker):
    # File that does not exist
    temp_file = 'non_existent_file.txt'

    # Ensure the file does not exist
    assert not os.path.exists(temp_file)

    # Mock os.unlink to ensure it does not get called
    mocker.patch('os.unlink')

    # Call the function
    atexit_remove_file(temp_file)

    # Assert os.unlink was not called
    os.unlink.assert_not_called()
