# file flutils/pathutils.py:504-560
# lines [554]
# branches ['553->554']

import os
import pytest
from pathlib import Path
from flutils.pathutils import normalize_path

@pytest.fixture
def mock_cwd(mocker):
    mocker.patch('os.getcwd', return_value='/mocked/dir')
    yield
    mocker.stopall()

def test_normalize_path_with_relative_path(mock_cwd):
    relative_path = 'relative/path'
    expected_path = Path('/mocked/dir/relative/path')
    normalized = normalize_path(relative_path)
    assert normalized == expected_path, f"Expected {expected_path}, got {normalized}"
