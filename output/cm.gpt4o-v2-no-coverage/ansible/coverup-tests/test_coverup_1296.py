# file: lib/ansible/plugins/loader.py:546-552
# asked: {"lines": [552], "branches": [[549, 552]]}
# gained: {"lines": [552], "branches": [[549, 552]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    return PluginLoader(class_name="test_class", package="test_package", config=None, subdir="test_subdir")

def test_find_plugin_resolved(plugin_loader):
    mock_result = MagicMock()
    mock_result.resolved = True
    mock_result.plugin_resolved_path = "/path/to/plugin"
    
    with patch.object(plugin_loader, 'find_plugin_with_context', return_value=mock_result):
        result = plugin_loader.find_plugin("test_plugin")
        assert result == "/path/to/plugin"

def test_find_plugin_not_resolved(plugin_loader):
    mock_result = MagicMock()
    mock_result.resolved = False
    mock_result.plugin_resolved_path = None
    
    with patch.object(plugin_loader, 'find_plugin_with_context', return_value=mock_result):
        result = plugin_loader.find_plugin("test_plugin")
        assert result is None
