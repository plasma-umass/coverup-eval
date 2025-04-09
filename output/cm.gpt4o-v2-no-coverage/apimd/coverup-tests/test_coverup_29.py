# file: apimd/loader.py:79-106
# asked: {"lines": [81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98, 99, 100, 101, 102, 103, 105, 106], "branches": [[82, 84], [82, 106], [85, 86], [85, 93], [87, 88], [87, 89], [91, 85], [91, 92], [93, 94], [93, 95], [97, 98], [97, 105], [99, 100], [99, 101], [102, 97], [102, 103]]}
# gained: {"lines": [81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98, 99, 100, 101, 102, 103, 105, 106], "branches": [[82, 84], [82, 106], [85, 86], [85, 93], [87, 88], [87, 89], [91, 92], [93, 94], [93, 95], [97, 98], [97, 105], [99, 100], [99, 101], [102, 103]]}

import pytest
from unittest.mock import patch, mock_open, MagicMock
from apimd.loader import loader
from importlib.machinery import EXTENSION_SUFFIXES

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('apimd.loader.logger')

@pytest.fixture
def mock_parser(mocker):
    mock_parser = mocker.patch('apimd.loader.Parser')
    mock_parser.new.return_value = mock_parser
    return mock_parser

@pytest.fixture
def mock_isfile(mocker):
    return mocker.patch('apimd.loader.isfile')

@pytest.fixture
def mock_read(mocker):
    return mocker.patch('apimd.loader._read')

@pytest.fixture
def mock_load_module(mocker):
    return mocker.patch('apimd.loader._load_module')

@pytest.fixture
def mock_walk_packages(mocker):
    return mocker.patch('apimd.loader.walk_packages')

def test_loader_pure_python(mock_logger, mock_parser, mock_isfile, mock_read, mock_load_module, mock_walk_packages):
    mock_walk_packages.return_value = [('module', '/path/to/module')]
    mock_isfile.side_effect = lambda path: path.endswith('.py')
    mock_read.return_value = 'def foo(): pass'

    result = loader('root', 'pwd', True, 1, True)

    mock_parser.new.assert_called_once_with(True, 1, True)
    mock_parser.parse.assert_called_once_with('module', 'def foo(): pass')
    mock_parser.compile.assert_called_once()
    assert result == mock_parser.compile.return_value

def test_loader_extension_module(mock_logger, mock_parser, mock_isfile, mock_read, mock_load_module, mock_walk_packages):
    mock_walk_packages.return_value = [('module', '/path/to/module')]
    mock_isfile.side_effect = lambda path: any(path.endswith(ext) for ext in EXTENSION_SUFFIXES)
    mock_load_module.return_value = True

    result = loader('root', 'pwd', True, 1, True)

    mock_parser.new.assert_called_once_with(True, 1, True)
    expected_ext = next(ext for ext in EXTENSION_SUFFIXES if mock_isfile(f'/path/to/module{ext}'))
    mock_load_module.assert_called_once_with('module', f'/path/to/module{expected_ext}', mock_parser)
    mock_parser.compile.assert_called_once()
    assert result == mock_parser.compile.return_value

def test_loader_no_module(mock_logger, mock_parser, mock_isfile, mock_read, mock_load_module, mock_walk_packages):
    mock_walk_packages.return_value = [('module', '/path/to/module')]
    mock_isfile.return_value = False

    result = loader('root', 'pwd', True, 1, True)

    mock_parser.new.assert_called_once_with(True, 1, True)
    mock_logger.warning.assert_called_once_with('no module for module in this platform')
    mock_parser.compile.assert_called_once()
    assert result == mock_parser.compile.return_value
