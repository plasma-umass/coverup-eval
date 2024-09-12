# file: lib/ansible/plugins/loader.py:546-552
# asked: {"lines": [546, 548, 549, 550, 552], "branches": [[549, 550], [549, 552]]}
# gained: {"lines": [546, 548, 549, 550, 552], "branches": [[549, 550], [549, 552]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    return PluginLoader(class_name="test_class", package="test_package", config=None, subdir="test_subdir")

def test_find_plugin_resolved(plugin_loader):
    mock_context = Mock()
    mock_context.resolved = True
    mock_context.plugin_resolved_path = "/path/to/plugin"
    
    with patch.object(plugin_loader, 'find_plugin_with_context', return_value=mock_context):
        result = plugin_loader.find_plugin("test_plugin")
        assert result == "/path/to/plugin"

def test_find_plugin_not_resolved(plugin_loader):
    mock_context = Mock()
    mock_context.resolved = False
    mock_context.plugin_resolved_path = None
    
    with patch.object(plugin_loader, 'find_plugin_with_context', return_value=mock_context):
        result = plugin_loader.find_plugin("test_plugin")
        assert result is None
