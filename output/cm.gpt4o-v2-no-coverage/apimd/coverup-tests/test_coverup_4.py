# file: apimd/loader.py:30-33
# asked: {"lines": [30, 32, 33], "branches": []}
# gained: {"lines": [30, 32, 33], "branches": []}

import pytest
import os

from apimd.loader import _write

def test_write(tmp_path):
    test_file = tmp_path / "test.txt"
    test_content = "Hello, World!"

    # Call the function
    _write(str(test_file), test_content)

    # Assert the file was created and contains the correct content
    assert test_file.exists()
    with open(test_file, 'r', encoding='utf-8') as f:
        content = f.read()
        assert content == test_content

    # Clean up
    test_file.unlink()
