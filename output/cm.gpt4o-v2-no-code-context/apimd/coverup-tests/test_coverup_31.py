# file: apimd/loader.py:79-106
# asked: {"lines": [81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98, 99, 100, 101, 102, 103, 105, 106], "branches": [[82, 84], [82, 106], [85, 86], [85, 93], [87, 88], [87, 89], [91, 85], [91, 92], [93, 94], [93, 95], [97, 98], [97, 105], [99, 100], [99, 101], [102, 97], [102, 103]]}
# gained: {"lines": [81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98, 99, 100, 101, 102, 103, 105, 106], "branches": [[82, 84], [82, 106], [85, 86], [85, 93], [87, 88], [87, 89], [91, 92], [93, 94], [93, 95], [97, 98], [97, 105], [99, 100], [99, 101], [102, 103]]}

import pytest
from unittest.mock import patch, mock_open, MagicMock
from apimd.loader import loader, EXTENSION_SUFFIXES

@pytest.fixture
def mock_parser():
    with patch('apimd.loader.Parser.new') as mock_parser_new:
        mock_parser_instance = MagicMock()
        mock_parser_new.return_value = mock_parser_instance
        yield mock_parser_instance

@pytest.fixture
def mock_walk_packages():
    with patch('apimd.loader.walk_packages') as mock_walk:
        yield mock_walk

@pytest.fixture
def mock_isfile():
    with patch('apimd.loader.isfile') as mock_isfile:
        yield mock_isfile

@pytest.fixture
def mock_read():
    with patch('apimd.loader._read', return_value="data") as mock_read:
        yield mock_read

@pytest.fixture
def mock_load_module():
    with patch('apimd.loader._load_module') as mock_load:
        yield mock_load

@pytest.fixture
def mock_logger():
    with patch('apimd.loader.logger') as mock_logger:
        yield mock_logger

def test_loader_pure_python(mock_parser, mock_walk_packages, mock_isfile, mock_read, mock_logger):
    mock_walk_packages.return_value = [("module_name", "module_path")]
    mock_isfile.side_effect = lambda x: x.endswith(".py")

    result = loader("root", "pwd", link=True, level=1, toc=True)

    mock_parser.parse.assert_called_once_with("module_name", "data")
    mock_logger.debug.assert_any_call("module_name <= module_path.py")
    assert result == mock_parser.compile()

def test_loader_extension_module(mock_parser, mock_walk_packages, mock_isfile, mock_read, mock_load_module, mock_logger):
    mock_walk_packages.return_value = [("module_name", "module_path")]
    mock_isfile.side_effect = lambda x: x.endswith(".so")
    mock_load_module.return_value = True

    result = loader("root", "pwd", link=True, level=1, toc=True)

    expected_extension = next(ext for ext in EXTENSION_SUFFIXES if ext.endswith(".so"))
    mock_logger.debug.assert_any_call(f"module_name <= module_path{expected_extension}")
    mock_load_module.assert_called_once_with("module_name", f"module_path{expected_extension}", mock_parser)
    assert result == mock_parser.compile()

def test_loader_no_module_found(mock_parser, mock_walk_packages, mock_isfile, mock_read, mock_load_module, mock_logger):
    mock_walk_packages.return_value = [("module_name", "module_path")]
    mock_isfile.side_effect = lambda x: False
    mock_load_module.return_value = False

    result = loader("root", "pwd", link=True, level=1, toc=True)

    mock_logger.warning.assert_called_once_with("no module for module_name in this platform")
    assert result == mock_parser.compile()
