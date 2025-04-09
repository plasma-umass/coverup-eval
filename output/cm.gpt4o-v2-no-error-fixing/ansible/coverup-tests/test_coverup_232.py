# file: lib/ansible/plugins/loader.py:257-274
# asked: {"lines": [257, 262, 263, 264, 265, 266, 267, 269, 270, 272, 273, 274], "branches": []}
# gained: {"lines": [257, 262, 263, 264, 265, 266, 267, 269, 270, 272, 273, 274], "branches": []}

import pytest
from ansible.plugins.loader import PluginLoader
from ansible.plugins import PATH_CACHE, PLUGIN_PATH_CACHE

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
        'PLUGIN_PATH_CACHE': {'key': 'value'},
        '_extra_dirs': ['extra_dir1', 'extra_dir2'],
        '_searched_paths': {'path1', 'path2'}
    }

def test_plugin_loader_setstate(plugin_loader_data):
    loader = PluginLoader('dummy', 'dummy', 'dummy', 'dummy')
    loader.__setstate__(plugin_loader_data)

    assert loader.class_name == 'test_class'
    assert loader.package == 'test_package'
    assert loader.config == ['test_config']
    assert loader.subdir == 'test_subdir'
    assert loader.aliases == {'alias1': 'test_alias'}
    assert loader.base_class == 'test_base_class'
    assert loader._extra_dirs == ['extra_dir1', 'extra_dir2']
    assert loader._searched_paths == {'path1', 'path2'}
    assert PATH_CACHE['test_class'] == 'test_path_cache'
    assert PLUGIN_PATH_CACHE['test_class'] == {'key': 'value'}

    # Clean up
    del PATH_CACHE['test_class']
    del PLUGIN_PATH_CACHE['test_class']
