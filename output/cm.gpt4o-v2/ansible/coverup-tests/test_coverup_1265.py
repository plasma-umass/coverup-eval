# file: lib/ansible/plugins/loader.py:865-876
# asked: {"lines": [], "branches": [[870, 873], [873, 876]]}
# gained: {"lines": [], "branches": [[870, 873], [873, 876]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    return PluginLoader(class_name='test_class', package='test_package', config=None, subdir='test_subdir')

@patch('ansible.plugins.loader.C.DEFAULT_DEBUG', True)
@patch('ansible.plugins.loader.display.debug')
def test_display_plugin_load_multiple_searched_paths(mock_debug, plugin_loader):
    class_name = 'test_class'
    name = 'test_name'
    searched_paths = ['path1', 'path2']
    path = 'test_path'
    
    with patch.object(plugin_loader, 'format_paths', return_value='path1, path2'):
        plugin_loader._display_plugin_load(class_name, name, searched_paths, path)
    
    expected_msg = "Loading test_class 'test_name' from test_path (searched paths: path1, path2)"
    mock_debug.assert_called_once_with(expected_msg)

@patch('ansible.plugins.loader.C.DEFAULT_DEBUG', True)
@patch('ansible.plugins.loader.display.debug')
def test_display_plugin_load_found_in_cache_class_only(mock_debug, plugin_loader):
    class_name = 'test_class'
    name = 'test_name'
    searched_paths = ['path1']
    path = 'test_path'
    found_in_cache = True
    class_only = True
    
    plugin_loader._display_plugin_load(class_name, name, searched_paths, path, found_in_cache, class_only)
    
    expected_msg = "Loading test_class 'test_name' from test_path (found_in_cache=True, class_only=True)"
    mock_debug.assert_called_once_with(expected_msg)
