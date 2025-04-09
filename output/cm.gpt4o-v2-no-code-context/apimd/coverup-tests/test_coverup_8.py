# file: apimd/loader.py:24-27
# asked: {"lines": [24, 26, 27], "branches": []}
# gained: {"lines": [24, 26, 27], "branches": []}

import pytest
from unittest import mock
import os

# Assuming the function _read is imported from apimd.loader
from apimd.loader import _read

def test_read_file(monkeypatch):
    test_content = "test content"
    test_path = "test_file.txt"

    # Mock the open function to return a mock file object
    mock_open = mock.mock_open(read_data=test_content)
    monkeypatch.setattr("builtins.open", mock_open)

    # Call the function and assert the result
    result = _read(test_path)
    assert result == test_content

    # Ensure the file was opened with the correct path and mode
    mock_open.assert_called_once_with(test_path, 'r')

def test_read_file_cleanup(monkeypatch):
    test_content = "test content"
    test_path = "test_file.txt"

    # Create a temporary file with the test content
    with open(test_path, 'w') as f:
        f.write(test_content)

    try:
        # Call the function and assert the result
        result = _read(test_path)
        assert result == test_content
    finally:
        # Clean up the temporary file
        os.remove(test_path)
