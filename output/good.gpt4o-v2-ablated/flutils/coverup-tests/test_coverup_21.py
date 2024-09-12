# file: flutils/pathutils.py:563-566
# asked: {"lines": [563, 564, 565, 566], "branches": []}
# gained: {"lines": [563, 564, 565, 566], "branches": []}

import pytest
import sys
from pathlib import Path
from flutils.pathutils import normalize_path

def test_normalize_path_bytes(monkeypatch):
    # Mock the normalize_path function to avoid side effects
    def mock_normalize_path(path):
        return Path(path)
    
    monkeypatch.setattr('flutils.pathutils.normalize_path', mock_normalize_path)
    
    # Test with a bytes path
    bytes_path = b'/some/path'
    expected_path = Path('/some/path')
    
    result = normalize_path(bytes_path)
    
    assert result == expected_path
