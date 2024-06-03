# file lib/ansible/module_utils/urls.py:885-891
# lines [886, 887, 888, 889, 891]
# branches ['886->exit', '886->887']

import os
import pytest
from unittest import mock
from ansible.module_utils.urls import atexit_remove_file

def test_atexit_remove_file(mocker):
    filename = 'testfile.tmp'

    # Create a temporary file
    with open(filename, 'w') as f:
        f.write('temporary file content')

    # Ensure the file exists
    assert os.path.exists(filename)

    # Mock os.unlink to simulate the file deletion
    mock_unlink = mocker.patch('os.unlink', side_effect=None)

    # Call the function
    atexit_remove_file(filename)

    # Assert that os.unlink was called
    mock_unlink.assert_called_once_with(filename)

    # Clean up: Ensure the file is deleted
    if os.path.exists(filename):
        os.remove(filename)

def test_atexit_remove_file_exception(mocker):
    filename = 'testfile.tmp'

    # Create a temporary file
    with open(filename, 'w') as f:
        f.write('temporary file content')

    # Ensure the file exists
    assert os.path.exists(filename)

    # Mock os.unlink to raise an exception
    mock_unlink = mocker.patch('os.unlink', side_effect=Exception('mocked exception'))

    # Call the function
    atexit_remove_file(filename)

    # Assert that os.unlink was called and exception was handled
    mock_unlink.assert_called_once_with(filename)

    # Clean up: Ensure the file is deleted
    if os.path.exists(filename):
        os.remove(filename)
