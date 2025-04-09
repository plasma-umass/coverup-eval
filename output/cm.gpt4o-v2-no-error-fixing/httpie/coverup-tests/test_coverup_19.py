# file: httpie/plugins/manager.py:31-36
# asked: {"lines": [31, 32, 33, 34, 35, 36], "branches": [[32, 0], [32, 33], [33, 32], [33, 34]]}
# gained: {"lines": [31, 32, 33, 34, 35, 36], "branches": [[32, 0], [32, 33], [33, 32], [33, 34]]}

import pytest
from unittest.mock import MagicMock, patch
from httpie.plugins.manager import PluginManager

@pytest.fixture
def plugin_manager():
    return PluginManager()

@patch('httpie.plugins.manager.iter_entry_points')
def test_load_installed_plugins(mock_iter_entry_points, plugin_manager):
    # Mock entry points
    mock_entry_point = MagicMock()
    mock_entry_point.load.return_value = MagicMock()
    mock_entry_point.dist.key = 'mock_package'
    mock_iter_entry_points.return_value = [mock_entry_point]

    # Mock ENTRY_POINT_NAMES
    with patch('httpie.plugins.manager.ENTRY_POINT_NAMES', ['mock_entry_point']):
        plugin_manager.load_installed_plugins()

    # Assertions
    assert len(plugin_manager) == 1
    assert plugin_manager[0].package_name == 'mock_package'
    mock_entry_point.load.assert_called()

    # Clean up
    plugin_manager.clear()
