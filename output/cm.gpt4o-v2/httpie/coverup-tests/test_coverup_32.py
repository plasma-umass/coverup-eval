# file: httpie/plugins/manager.py:31-36
# asked: {"lines": [31, 32, 33, 34, 35, 36], "branches": [[32, 0], [32, 33], [33, 32], [33, 34]]}
# gained: {"lines": [31, 32, 33, 34, 35, 36], "branches": [[32, 0], [32, 33], [33, 32], [33, 34]]}

import pytest
from unittest.mock import MagicMock, patch
from httpie.plugins.manager import PluginManager

@pytest.fixture
def mock_entry_point():
    mock = MagicMock()
    mock.load.return_value = MagicMock()
    mock.dist.key = 'mock_package'
    return mock

@pytest.fixture
def mock_iter_entry_points(mock_entry_point):
    with patch('httpie.plugins.manager.iter_entry_points', return_value=[mock_entry_point]) as mock_iter:
        yield mock_iter

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_load_installed_plugins(plugin_manager, mock_iter_entry_points, mock_entry_point):
    ENTRY_POINT_NAMES = ['httpie.plugins']
    
    with patch('httpie.plugins.manager.ENTRY_POINT_NAMES', ENTRY_POINT_NAMES):
        plugin_manager.load_installed_plugins()
    
    mock_iter_entry_points.assert_called_once_with('httpie.plugins')
    mock_entry_point.load.assert_called()
    assert len(plugin_manager) == 1
    assert plugin_manager[0].package_name == 'mock_package'
