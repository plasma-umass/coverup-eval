# file: apimd/loader.py:30-33
# asked: {"lines": [30, 32, 33], "branches": []}
# gained: {"lines": [30, 32, 33], "branches": []}

import os
import pytest

from apimd.loader import _write

def test_write(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, World!"

    # Call the function
    _write(str(test_file), test_content)

    # Verify the file was written correctly
    with open(test_file, 'r', encoding='utf-8') as f:
        content = f.read()
        assert content == test_content

    # Clean up
    if test_file.exists():
        test_file.unlink()
