# file apimd/loader.py:24-27
# lines [24, 26, 27]
# branches []

import pytest
import os

from apimd.loader import _read

def test_read_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_script.py"
    test_content = "print('Hello, world!')"
    test_file.write_text(test_content)

    # Read the file using the _read function
    result = _read(str(test_file))

    # Assert that the content read is as expected
    assert result == test_content

    # Clean up is handled by pytest's tmp_path fixture
