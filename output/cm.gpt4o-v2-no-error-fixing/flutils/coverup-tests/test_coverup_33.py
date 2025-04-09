# file: flutils/pathutils.py:569-571
# asked: {"lines": [569, 570, 571], "branches": []}
# gained: {"lines": [569, 570, 571], "branches": []}

import pytest
from pathlib import Path
from flutils.pathutils import normalize_path

def test_normalize_path_pathlib():
    path = Path('~/tmp/foo/../bar')
    normalized_path = normalize_path(path)
    expected_path = normalize_path(path.as_posix())
    assert normalized_path == expected_path
