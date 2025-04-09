# file: lib/ansible/plugins/loader.py:257-274
# asked: {"lines": [257, 262, 263, 264, 265, 266, 267, 269, 270, 272, 273, 274], "branches": []}
# gained: {"lines": [257, 262, 263, 264, 265, 266, 267, 269, 270, 272, 273, 274], "branches": []}

import pytest
from ansible.plugins.loader import PluginLoader

# Mocking the global caches
PATH_CACHE = {}
PLUGIN_PATH_CACHE = {}

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

def test_plugin_loader_setstate(plugin_loader_data, monkeypatch):
    # Mock the __init__ method to avoid actual initialization
    def mock_init(self, class_name, package, config, subdir, aliases, base_class):
        self.class_name = class_name
        self.package = package
        self.config = config
        self.subdir = subdir
        self.aliases = aliases
        self.base_class = base_class

    monkeypatch.setattr(PluginLoader, '__init__', mock_init)
    monkeypatch.setattr('ansible.plugins.loader.PATH_CACHE', PATH_CACHE)
    monkeypatch.setattr('ansible.plugins.loader.PLUGIN_PATH_CACHE', PLUGIN_PATH_CACHE)

    loader = PluginLoader.__new__(PluginLoader)
    loader.__setstate__(plugin_loader_data)

    assert loader.class_name == 'TestPlugin'
    assert loader.package == 'test_package'
    assert loader.config == 'test_config'
    assert loader.subdir == 'test_subdir'
    assert loader.aliases == ['alias1', 'alias2']
    assert loader.base_class == 'BaseClass'
    assert loader._extra_dirs == ['extra_dir1', 'extra_dir2']
    assert loader._searched_paths == {'path1', 'path2'}
    assert PATH_CACHE['TestPlugin'] == 'test_path_cache'
    assert PLUGIN_PATH_CACHE['TestPlugin'] == 'test_plugin_path_cache'
