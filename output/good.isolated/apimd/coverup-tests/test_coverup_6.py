# file apimd/loader.py:30-33
# lines [30, 32, 33]
# branches []

import os
from apimd.loader import _write
import pytest

def test_write_function(tmp_path):
    # Create a temporary file path
    temp_file = tmp_path / "temp_doc.txt"
    temp_file_path = str(temp_file)

    # Content to be written
    content = "Test content for _write function."

    # Call the _write function
    _write(temp_file_path, content)

    # Check if the file exists
    assert os.path.exists(temp_file_path)

    # Read the content and verify it's correct
    with open(temp_file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
    assert file_content == content

    # Clean up is handled by the tmp_path fixture automatically
