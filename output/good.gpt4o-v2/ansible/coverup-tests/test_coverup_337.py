# file: lib/ansible/plugins/loader.py:257-274
# asked: {"lines": [257, 262, 263, 264, 265, 266, 267, 269, 270, 272, 273, 274], "branches": []}
# gained: {"lines": [257, 262, 263, 264, 265, 266, 267, 269, 270, 272, 273, 274], "branches": []}

import pytest
from unittest.mock import patch
from ansible.plugins.loader import PluginLoader, PATH_CACHE, PLUGIN_PATH_CACHE

@pytest.fixture
def plugin_loader_data():
    return {
        'class_name': 'test_class',
        'package': 'test_package',
        'config': ['test_config'],
        'subdir': 'test_subdir',
        'aliases': {'alias1': 'test_alias'},
        'base_class': 'test_base_class',
        'PATH_CACHE': 'test_path_cache',
        'PLUGIN_PATH_CACHE': {'plugin1': 'test_plugin_cache'},
        '_extra_dirs': ['extra_dir1'],
        '_searched_paths': {'path1', 'path2'}
    }

def test_plugin_loader_setstate(plugin_loader_data):
    loader = PluginLoader.__new__(PluginLoader)
    
    with patch.dict(PATH_CACHE, {}, clear=True), patch.dict(PLUGIN_PATH_CACHE, {}, clear=True):
        loader.__setstate__(plugin_loader_data)
        
        assert loader.class_name == 'test_class'
        assert loader.package == 'test_package'
        assert loader.config == ['test_config']
        assert loader.subdir == 'test_subdir'
        assert loader.aliases == {'alias1': 'test_alias'}
        assert loader.base_class == 'test_base_class'
        assert PATH_CACHE['test_class'] == 'test_path_cache'
        assert PLUGIN_PATH_CACHE['test_class'] == {'plugin1': 'test_plugin_cache'}
        assert loader._extra_dirs == ['extra_dir1']
        assert loader._searched_paths == {'path1', 'path2'}
