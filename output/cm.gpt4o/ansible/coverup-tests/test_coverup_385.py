# file lib/ansible/plugins/loader.py:257-274
# lines [257, 262, 263, 264, 265, 266, 267, 269, 270, 272, 273, 274]
# branches []

import pytest
from unittest.mock import patch

# Assuming the PluginLoader class is imported from ansible.plugins.loader
from ansible.plugins.loader import PluginLoader, PATH_CACHE, PLUGIN_PATH_CACHE

@pytest.fixture
def mock_path_cache(mocker):
    original_path_cache = mocker.patch.dict(PATH_CACHE, {}, clear=True)
    original_plugin_path_cache = mocker.patch.dict(PLUGIN_PATH_CACHE, {}, clear=True)
    yield
    mocker.stopall()

def test_plugin_loader_setstate(mock_path_cache):
    data = {
        'class_name': 'TestPlugin',
        'package': 'test_package',
        'config': 'test_config',
        'subdir': 'test_subdir',
        'aliases': ['alias1', 'alias2'],
        'base_class': 'BaseClass',
        'PATH_CACHE': 'test_path_cache',
        'PLUGIN_PATH_CACHE': 'test_plugin_path_cache',
        '_extra_dirs': ['extra_dir1', 'extra_dir2'],
        '_searched_paths': {'path1', 'path2'}
    }

    with patch.object(PluginLoader, '__init__', return_value=None) as mock_init:
        loader = PluginLoader.__new__(PluginLoader)  # Bypass __init__ by using __new__
        loader.__setstate__(data)

        mock_init.assert_called_once_with(
            'TestPlugin', 'test_package', 'test_config', 'test_subdir', ['alias1', 'alias2'], 'BaseClass'
        )
        assert loader._extra_dirs == ['extra_dir1', 'extra_dir2']
        assert loader._searched_paths == {'path1', 'path2'}
        assert PATH_CACHE['TestPlugin'] == 'test_path_cache'
        assert PLUGIN_PATH_CACHE['TestPlugin'] == 'test_plugin_path_cache'
