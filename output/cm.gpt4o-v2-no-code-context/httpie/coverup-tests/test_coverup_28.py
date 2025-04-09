# file: httpie/plugins/manager.py:31-36
# asked: {"lines": [31, 32, 33, 34, 35, 36], "branches": [[32, 0], [32, 33], [33, 32], [33, 34]]}
# gained: {"lines": [31, 32, 33, 34, 35, 36], "branches": [[32, 0], [32, 33], [33, 32], [33, 34]]}

import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_load_installed_plugins(plugin_manager, monkeypatch):
    mock_entry_point = MagicMock()
    mock_entry_point.load.return_value = MagicMock()
    mock_entry_point.dist.key = 'mock_package'

    mock_iter_entry_points = MagicMock(return_value=[mock_entry_point])
    monkeypatch.setattr('httpie.plugins.manager.iter_entry_points', mock_iter_entry_points)

    mock_entry_point_names = ['httpie.plugins.auth.v1', 'httpie.plugins.transport.v1']
    with patch('httpie.plugins.manager.ENTRY_POINT_NAMES', mock_entry_point_names):
        plugin_manager.load_installed_plugins()

    assert len(plugin_manager) == len(mock_entry_point_names)
    for plugin in plugin_manager:
        assert plugin.package_name == 'mock_package'
