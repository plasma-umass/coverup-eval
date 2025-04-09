# file apimd/loader.py:30-33
# lines [30, 32, 33]
# branches []

import os
import pytest

from apimd.loader import _write

def test_write_function(tmp_path):
    test_path = tmp_path / "test_file.txt"
    test_content = "This is a test."

    # Call the _write function
    _write(str(test_path), test_content)

    # Verify the file was created and contains the correct content
    assert test_path.exists()
    with open(test_path, 'r', encoding='utf-8') as f:
        content = f.read()
        assert content == test_content
