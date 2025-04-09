# file: apimd/loader.py:30-33
# asked: {"lines": [30, 32, 33], "branches": []}
# gained: {"lines": [30, 32, 33], "branches": []}

import pytest
import os
from apimd.loader import _write

def test_write(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, world!"

    # Call the function
    _write(str(test_file), test_content)

    # Verify the file was created and contains the correct content
    assert test_file.exists()
    with open(test_file, 'r', encoding='utf-8') as f:
        assert f.read() == test_content

    # Clean up
    if test_file.exists():
        os.remove(test_file)
