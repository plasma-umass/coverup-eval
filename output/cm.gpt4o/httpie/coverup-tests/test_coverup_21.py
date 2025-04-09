# file httpie/plugins/manager.py:31-36
# lines [31, 32, 33, 34, 35, 36]
# branches ['32->exit', '32->33', '33->32', '33->34']

import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

@pytest.fixture
def mock_entry_point():
    mock_entry_point = MagicMock()
    mock_entry_point.load.return_value = MagicMock()
    mock_entry_point.dist.key = 'mock_package'
    return mock_entry_point

@pytest.fixture
def mock_iter_entry_points(mock_entry_point):
    with patch('httpie.plugins.manager.iter_entry_points', return_value=[mock_entry_point]) as mock_iter:
        yield mock_iter

@pytest.fixture
def mock_entry_point_names():
    with patch('httpie.plugins.manager.ENTRY_POINT_NAMES', ['mock_entry_point_name']):
        yield

def test_load_installed_plugins(mock_iter_entry_points, mock_entry_point_names, mock_entry_point):
    manager = PluginManager()
    manager.register = MagicMock()
    manager.load_installed_plugins()
    
    mock_iter_entry_points.assert_called_once_with('mock_entry_point_name')
    mock_entry_point.load.assert_called()
    manager.register.assert_called_with(mock_entry_point.load())
    assert mock_entry_point.load().package_name == 'mock_package'
