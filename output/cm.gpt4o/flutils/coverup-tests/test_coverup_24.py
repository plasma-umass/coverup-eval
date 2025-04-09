# file flutils/pathutils.py:563-566
# lines [563, 564, 565, 566]
# branches []

import pytest
from flutils.pathutils import normalize_path
from pathlib import Path
import sys

def test_normalize_path_bytes():
    # Create a bytes path
    bytes_path = b'/tmp/testpath'
    
    # Call the normalize_path function with bytes input
    result = normalize_path(bytes_path)
    
    # Assert that the result is a Path object
    assert isinstance(result, Path)
    
    # Assert that the result is the expected path
    expected_path = Path(bytes_path.decode(sys.getfilesystemencoding()))
    assert result == expected_path
