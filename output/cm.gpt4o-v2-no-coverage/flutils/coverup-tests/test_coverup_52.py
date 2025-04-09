# file: flutils/pathutils.py:219-333
# asked: {"lines": [219, 221, 222, 223, 274, 276, 277, 278, 279, 281, 282, 283, 286, 290, 292, 293, 294, 295, 296, 297, 298, 301, 302, 306, 307, 308, 309, 310, 311, 312, 313, 315, 316, 318, 321, 322, 324, 325, 326, 327, 330, 331, 333], "branches": [[276, 277], [276, 281], [281, 282], [281, 290], [293, 294], [293, 295], [295, 296], [295, 301], [306, 307], [306, 321], [308, 309], [308, 312], [312, 313], [312, 315], [321, 322], [321, 324], [324, 325], [324, 330], [325, 326], [325, 333]]}
# gained: {"lines": [219, 221, 222, 223, 274, 276, 277, 278, 279, 281, 282, 283, 286, 290, 292, 293, 294, 295, 296, 297, 298, 301, 302, 306, 307, 308, 309, 310, 311, 312, 313, 321, 322, 324, 325, 326, 327, 330, 331, 333], "branches": [[276, 277], [276, 281], [281, 282], [281, 290], [293, 294], [293, 295], [295, 296], [295, 301], [306, 307], [308, 309], [308, 312], [312, 313], [321, 322], [324, 325], [324, 330], [325, 326], [325, 333]]}

import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from flutils.pathutils import directory_present

@pytest.fixture
def mock_normalize_path():
    with patch('flutils.pathutils.normalize_path') as mock:
        yield mock

@pytest.fixture
def mock_exists_as():
    with patch('flutils.pathutils.exists_as') as mock:
        yield mock

@pytest.fixture
def mock_chown():
    with patch('flutils.pathutils.chown') as mock:
        yield mock

@pytest.fixture
def mock_chmod():
    with patch('flutils.pathutils.chmod') as mock:
        yield mock

@pytest.fixture
def mock_mkdir():
    with patch('pathlib.Path.mkdir') as mock:
        yield mock

def test_directory_present_creates_directory(mock_normalize_path, mock_exists_as, mock_chown, mock_chmod, mock_mkdir):
    path = Path('/tmp/test_path')
    mock_normalize_path.return_value = path
    mock_exists_as.side_effect = ['', 'directory']

    result = directory_present(path)

    assert result == path
    mock_normalize_path.assert_called_once_with(path)
    mock_exists_as.assert_any_call(path)
    mock_chown.assert_called()
    mock_chmod.assert_not_called()
    mock_mkdir.assert_called_once_with(mode=0o700)

def test_directory_present_raises_value_error_on_glob(mock_normalize_path):
    path = Path('/tmp/test*path')
    mock_normalize_path.return_value = path

    with pytest.raises(ValueError, match='must NOT contain any glob patterns'):
        directory_present(path)

def test_directory_present_raises_value_error_on_non_absolute_path(mock_normalize_path):
    path = Path('relative/path')
    mock_normalize_path.return_value = path

    with pytest.raises(ValueError, match='must be an absolute path'):
        directory_present(path)

def test_directory_present_raises_file_exists_error_on_existing_non_directory(mock_normalize_path, mock_exists_as):
    path = Path('/tmp/test_path')
    mock_normalize_path.return_value = path
    mock_exists_as.return_value = 'file'

    with pytest.raises(FileExistsError, match='can NOT be created as a directory'):
        directory_present(path)

def test_directory_present_creates_parent_directories(mock_normalize_path, mock_exists_as, mock_chown, mock_chmod, mock_mkdir):
    path = Path('/tmp/parent/test_path')
    mock_normalize_path.return_value = path
    mock_exists_as.side_effect = ['', '', 'directory']

    result = directory_present(path)

    assert result == path
    mock_normalize_path.assert_called_once_with(path)
    mock_exists_as.assert_any_call(path)
    mock_chown.assert_called()
    mock_chmod.assert_not_called()
    mock_mkdir.assert_called()

def test_directory_present_chown_existing_directory(mock_normalize_path, mock_exists_as, mock_chown, mock_chmod):
    path = Path('/tmp/test_path')
    mock_normalize_path.return_value = path
    mock_exists_as.return_value = 'directory'

    result = directory_present(path)

    assert result == path
    mock_normalize_path.assert_called_once_with(path)
    mock_exists_as.assert_any_call(path)
    mock_chown.assert_called()
    mock_chmod.assert_called()
