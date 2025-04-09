# file: lib/ansible/module_utils/urls.py:885-891
# asked: {"lines": [885, 886, 887, 888, 889, 891], "branches": [[886, 0], [886, 887]]}
# gained: {"lines": [885, 886, 887, 888, 889, 891], "branches": [[886, 0], [886, 887]]}

import os
import pytest
from ansible.module_utils.urls import atexit_remove_file

def test_atexit_remove_file_exists(monkeypatch):
    test_file = 'test_file.txt'
    
    # Create a test file
    with open(test_file, 'w') as f:
        f.write('test')

    assert os.path.exists(test_file)

    # Test the function
    atexit_remove_file(test_file)

    # Assert the file has been removed
    assert not os.path.exists(test_file)

def test_atexit_remove_file_not_exists():
    test_file = 'non_existent_file.txt'
    
    # Ensure the file does not exist
    if os.path.exists(test_file):
        os.unlink(test_file)

    assert not os.path.exists(test_file)

    # Test the function
    atexit_remove_file(test_file)

    # Assert the file still does not exist
    assert not os.path.exists(test_file)

def test_atexit_remove_file_unlink_exception(monkeypatch):
    test_file = 'test_file.txt'
    
    # Create a test file
    with open(test_file, 'w') as f:
        f.write('test')

    assert os.path.exists(test_file)

    # Mock os.unlink to raise an exception
    def mock_unlink(filename):
        raise Exception("Mocked exception")

    monkeypatch.setattr(os, 'unlink', mock_unlink)

    # Test the function
    atexit_remove_file(test_file)

    # Assert the file still exists since unlink raised an exception
    assert os.path.exists(test_file)

    # Clean up
    monkeypatch.undo()
    os.unlink(test_file)
