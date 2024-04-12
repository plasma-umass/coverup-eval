# file flutils/pathutils.py:563-566
# lines [563, 564, 565, 566]
# branches []

import pytest
import sys
from pathlib import Path
from flutils.pathutils import normalize_path

def test_normalize_path_bytes(tmp_path):
    # Create a temporary bytes path
    bytes_path = str(tmp_path / "testfile").encode(sys.getfilesystemencoding())

    # Call the function with the bytes path
    result = normalize_path(bytes_path)

    # Check that the result is a Path object and the path is correct
    assert isinstance(result, Path)
    assert result == Path(bytes_path.decode(sys.getfilesystemencoding()))

    # No need to mock or cleanup since we're not altering any state
