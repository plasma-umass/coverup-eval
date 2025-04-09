# file: lib/ansible/module_utils/urls.py:885-891
# asked: {"lines": [885, 886, 887, 888, 889, 891], "branches": [[886, 0], [886, 887]]}
# gained: {"lines": [885, 886, 887, 888], "branches": [[886, 0], [886, 887]]}

import os
import pytest
from unittest import mock

def test_atexit_remove_file_exists(monkeypatch):
    filename = "testfile"

    # Create a temporary file
    with open(filename, "w") as f:
        f.write("Temporary file content")

    # Ensure the file exists
    assert os.path.exists(filename)

    # Mock os.unlink to test the function without actually deleting the file
    with mock.patch("os.unlink") as mock_unlink:
        from ansible.module_utils.urls import atexit_remove_file
        atexit_remove_file(filename)
        mock_unlink.assert_called_once_with(filename)

    # Clean up
    if os.path.exists(filename):
        os.remove(filename)

def test_atexit_remove_file_not_exists(monkeypatch):
    filename = "nonexistentfile"

    # Ensure the file does not exist
    assert not os.path.exists(filename)

    # Mock os.unlink to ensure it is not called
    with mock.patch("os.unlink") as mock_unlink:
        from ansible.module_utils.urls import atexit_remove_file
        atexit_remove_file(filename)
        mock_unlink.assert_not_called()
