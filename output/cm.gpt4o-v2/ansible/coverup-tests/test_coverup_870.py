# file: lib/ansible/plugins/loader.py:806-807
# asked: {"lines": [806, 807], "branches": []}
# gained: {"lines": [806, 807], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    return PluginLoader(class_name='TestPlugin', package='test_package', config=None, subdir='test_subdir')

def test_get_method_executes_get_with_context(plugin_loader):
    with patch.object(plugin_loader, 'get_with_context') as mock_get_with_context:
        mock_plugin = MagicMock()
        mock_get_with_context.return_value = MagicMock(object=mock_plugin)
        
        result = plugin_loader.get('test_plugin')
        
        mock_get_with_context.assert_called_once_with('test_plugin')
        assert result == mock_plugin
