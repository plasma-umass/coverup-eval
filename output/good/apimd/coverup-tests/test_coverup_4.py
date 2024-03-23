# file apimd/loader.py:24-27
# lines [24, 26, 27]
# branches []

import os
import pytest
from apimd.loader import _read

def test_read_file(tmp_path):
    # Create a temporary file and write some content to it
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, World!"
    test_file.write_text(test_content)

    # Ensure the _read function reads the content correctly
    assert _read(str(test_file)) == test_content

    # Clean up is handled by pytest's tmp_path fixture automatically
