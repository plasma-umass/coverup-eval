# file: flutils/pathutils.py:569-571
# asked: {"lines": [569, 570, 571], "branches": []}
# gained: {"lines": [569, 570, 571], "branches": []}

import pytest
from pathlib import Path
from flutils.pathutils import normalize_path

def test_normalize_path_pathlib(monkeypatch):
    # Mock the normalize_path function to avoid side effects
    def mock_normalize_path(path):
        return Path(path)

    monkeypatch.setattr('flutils.pathutils.normalize_path', mock_normalize_path)

    # Test with a Path object
    input_path = Path('/some/path')
    result = normalize_path(input_path)
    
    assert isinstance(result, Path)
    assert result == input_path

    # Test with a different Path object
    input_path = Path('/another/path')
    result = normalize_path(input_path)
    
    assert isinstance(result, Path)
    assert result == input_path
