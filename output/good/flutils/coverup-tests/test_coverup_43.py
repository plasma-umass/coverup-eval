# file flutils/pathutils.py:387-414
# lines [387, 412, 413, 414]
# branches []

import pytest
from pathlib import Path
from flutils.pathutils import find_paths
from unittest.mock import MagicMock

@pytest.fixture
def mock_normalize_path(mocker):
    mock = mocker.patch('flutils.pathutils.normalize_path')
    mock.return_value = Path('/fake/dir/*')
    return mock

@pytest.fixture
def mock_path_glob(mocker):
    mock = mocker.patch('pathlib.Path.glob')
    mock.return_value = iter([Path('/fake/dir/file1.txt'), Path('/fake/dir/file2.txt')])
    return mock

def test_find_paths(mock_normalize_path, mock_path_glob):
    pattern = '~/fake/dir/*'
    expected_paths = [Path('/fake/dir/file1.txt'), Path('/fake/dir/file2.txt')]
    
    result = list(find_paths(pattern))
    
    mock_normalize_path.assert_called_once_with(pattern)
    mock_path_glob.assert_called_once_with('fake/dir/*')
    
    assert result == expected_paths, "The result paths do not match the expected paths"
