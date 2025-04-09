# file: lib/ansible/plugins/loader.py:257-274
# asked: {"lines": [257, 262, 263, 264, 265, 266, 267, 269, 270, 272, 273, 274], "branches": []}
# gained: {"lines": [257, 262, 263, 264, 265, 266, 267, 269, 270, 272, 273, 274], "branches": []}

import pytest
from ansible.plugins.loader import PluginLoader
from ansible.plugins import PATH_CACHE, PLUGIN_PATH_CACHE

@pytest.fixture
def plugin_loader_data():
    return {
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

@pytest.fixture(autouse=True)
def clear_caches():
    original_path_cache = PATH_CACHE.copy()
    original_plugin_path_cache = PLUGIN_PATH_CACHE.copy()
    PATH_CACHE.clear()
    PLUGIN_PATH_CACHE.clear()
    yield
    PATH_CACHE.clear()
    PLUGIN_PATH_CACHE.clear()
    PATH_CACHE.update(original_path_cache)
    PLUGIN_PATH_CACHE.update(original_plugin_path_cache)

def test_plugin_loader_setstate(plugin_loader_data):
    loader = PluginLoader.__new__(PluginLoader)
    loader.__setstate__(plugin_loader_data)

    assert PATH_CACHE['TestPlugin'] == 'test_path_cache'
    assert PLUGIN_PATH_CACHE['TestPlugin'] == 'test_plugin_path_cache'
    assert loader._extra_dirs == ['extra_dir1', 'extra_dir2']
    assert loader._searched_paths == {'path1', 'path2'}
    assert loader.class_name == 'TestPlugin'
    assert loader.package == 'test_package'
    assert loader.config == ['test_config']
    assert loader.subdir == 'test_subdir'
    assert loader.aliases == ['alias1', 'alias2']
    assert loader.base_class == 'BaseClass'
