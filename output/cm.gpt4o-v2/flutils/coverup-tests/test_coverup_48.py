# file: flutils/pathutils.py:569-571
# asked: {"lines": [569, 570, 571], "branches": []}
# gained: {"lines": [569, 570, 571], "branches": []}

import pytest
from pathlib import Path
from flutils.pathutils import normalize_path

def test_normalize_path_pathlib(monkeypatch):
    # Mock the home directory to ensure consistent test results
    monkeypatch.setenv('HOME', '/home/test_user')
    
    # Create a Path object
    path = Path('~/tmp/foo/../bar')
    
    # Call the _normalize_path_pathlib function indirectly via normalize_path
    normalized_path = normalize_path(path)
    
    # Assert the result is as expected
    assert normalized_path == Path('/home/test_user/tmp/bar')
