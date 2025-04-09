# file: apimd/loader.py:24-27
# asked: {"lines": [24, 26, 27], "branches": []}
# gained: {"lines": [24, 26, 27], "branches": []}

import pytest
import os

from apimd.loader import _read

def test_read(monkeypatch):
    test_content = "test content"
    test_path = "test_script.py"

    # Create a temporary file with test content
    with open(test_path, 'w') as f:
        f.write(test_content)

    try:
        # Test the _read function
        result = _read(test_path)
        assert result == test_content
    finally:
        # Clean up the temporary file
        os.remove(test_path)
