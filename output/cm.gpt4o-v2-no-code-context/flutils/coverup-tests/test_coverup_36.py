# file: flutils/pathutils.py:569-571
# asked: {"lines": [569, 570, 571], "branches": []}
# gained: {"lines": [569, 570, 571], "branches": []}

import pytest
from pathlib import Path
from flutils.pathutils import normalize_path

def test_normalize_path_pathlib(monkeypatch):
    # Mock the normalize_path function to track its calls
    def mock_normalize_path(path):
        return path

    monkeypatch.setattr('flutils.pathutils.normalize_path', mock_normalize_path)

    # Create a Path object
    path_obj = Path('/some/path')

    # Call the _normalize_path_pathlib function indirectly via normalize_path
    result = normalize_path(path_obj)

    # Assert that the result is the expected normalized path
    assert result == path_obj.as_posix()
