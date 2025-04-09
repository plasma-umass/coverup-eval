# file: apimd/loader.py:24-27
# asked: {"lines": [24, 26, 27], "branches": []}
# gained: {"lines": [24, 26, 27], "branches": []}

import pytest
from unittest import mock
from apimd.loader import _read

def test_read_file(monkeypatch):
    # Mock the open function to simulate file reading
    mock_open = mock.mock_open(read_data="test content")
    monkeypatch.setattr("builtins.open", mock_open)

    # Call the function with a test path
    result = _read("test_path")

    # Assert that the content read is as expected
    assert result == "test content"

    # Ensure the file was opened with the correct path and mode
    mock_open.assert_called_once_with("test_path", 'r')
