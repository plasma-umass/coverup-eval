# file: lib/ansible/module_utils/urls.py:885-891
# asked: {"lines": [885, 886, 887, 888, 889, 891], "branches": [[886, 0], [886, 887]]}
# gained: {"lines": [885, 886, 887, 888, 889, 891], "branches": [[886, 0], [886, 887]]}

import os
import pytest
from unittest import mock

from ansible.module_utils.urls import atexit_remove_file

def test_atexit_remove_file_exists(mocker):
    # Setup
    filename = 'testfile'
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.unlink')

    # Execute
    atexit_remove_file(filename)

    # Verify
    os.path.exists.assert_called_once_with(filename)
    os.unlink.assert_called_once_with(filename)

def test_atexit_remove_file_not_exists(mocker):
    # Setup
    filename = 'testfile'
    mocker.patch('os.path.exists', return_value=False)
    mocker.patch('os.unlink')

    # Execute
    atexit_remove_file(filename)

    # Verify
    os.path.exists.assert_called_once_with(filename)
    os.unlink.assert_not_called()

def test_atexit_remove_file_unlink_exception(mocker):
    # Setup
    filename = 'testfile'
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.unlink', side_effect=Exception)

    # Execute
    atexit_remove_file(filename)

    # Verify
    os.path.exists.assert_called_once_with(filename)
    os.unlink.assert_called_once_with(filename)
