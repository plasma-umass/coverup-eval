# file: apimd/loader.py:24-27
# asked: {"lines": [24, 26, 27], "branches": []}
# gained: {"lines": [24, 26, 27], "branches": []}

import pytest
import os
from apimd.loader import _read

def test_read_file(tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "test_script.py"
    content = "print('Hello, world!')"
    temp_file.write_text(content)

    # Test the _read function
    result = _read(str(temp_file))
    assert result == content

    # Clean up is handled by pytest's tmp_path fixture
