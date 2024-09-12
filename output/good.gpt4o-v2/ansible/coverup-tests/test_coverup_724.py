# file: lib/ansible/plugins/loader.py:384-388
# asked: {"lines": [384, 387, 388], "branches": []}
# gained: {"lines": [384, 387, 388], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    return PluginLoader(class_name='test', package='test_package', config=['/test/config'], subdir='test_subdir')

def test_get_paths(plugin_loader):
    with patch.object(plugin_loader, '_get_paths_with_context', return_value=[MagicMock(path='/test/path1'), MagicMock(path='/test/path2')]) as mock_get_paths_with_context:
        paths = plugin_loader._get_paths()
        assert paths == ['/test/path1', '/test/path2']
        mock_get_paths_with_context.assert_called_once_with(subdirs=True)
