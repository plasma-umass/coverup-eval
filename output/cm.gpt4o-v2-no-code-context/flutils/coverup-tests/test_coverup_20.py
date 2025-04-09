# file: flutils/pathutils.py:563-566
# asked: {"lines": [563, 564, 565, 566], "branches": []}
# gained: {"lines": [563, 564, 565, 566], "branches": []}

import pytest
import sys
from pathlib import Path
from flutils.pathutils import normalize_path

def test_normalize_path_bytes(monkeypatch):
    # Mock the sys.getfilesystemencoding to return a specific encoding
    monkeypatch.setattr(sys, 'getfilesystemencoding', lambda: 'utf-8')
    
    # Create a bytes path
    bytes_path = b'/some/bytes/path'
    
    # Call the normalize_path function with the bytes path
    result = normalize_path(bytes_path)
    
    # Assert that the result is a Path object and the path is correctly decoded
    assert isinstance(result, Path)
    assert str(result) == '/some/bytes/path'
