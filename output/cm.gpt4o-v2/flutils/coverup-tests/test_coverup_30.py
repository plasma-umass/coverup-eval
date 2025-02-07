# file: flutils/pathutils.py:563-566
# asked: {"lines": [563, 564, 565, 566], "branches": []}
# gained: {"lines": [563, 564, 565, 566], "branches": []}

import pytest
import sys
from pathlib import Path
from flutils.pathutils import normalize_path

def test_normalize_path_bytes():
    # Create a bytes path
    bytes_path = b'/tmp/test_path'

    # Normalize the bytes path
    result = normalize_path(bytes_path)

    # Assert the result is a Path object
    assert isinstance(result, Path)

    # Assert the result is the expected path
    expected_path = Path('/tmp/test_path')
    assert result == expected_path
