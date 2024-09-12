# file: lib/ansible/plugins/loader.py:304-305
# asked: {"lines": [305], "branches": []}
# gained: {"lines": [305], "branches": []}

import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def plugin_loader():
    from ansible.plugins.loader import PluginLoader
    return PluginLoader(class_name='test_class', package='test_package', config=[], subdir='test_subdir')

def test_print_paths(plugin_loader):
    with patch.object(plugin_loader, '_get_paths', return_value=['/path/to/plugin1', '/path/to/plugin2']) as mock_get_paths, \
         patch.object(plugin_loader, 'format_paths', return_value='/path/to/plugin1:/path/to/plugin2') as mock_format_paths:
        
        result = plugin_loader.print_paths()
        
        mock_get_paths.assert_called_once_with(subdirs=False)
        mock_format_paths.assert_called_once_with(['/path/to/plugin1', '/path/to/plugin2'])
        assert result == '/path/to/plugin1:/path/to/plugin2'
