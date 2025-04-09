# file: lib/ansible/plugins/loader.py:203-236
# asked: {"lines": [217], "branches": [[216, 217]]}
# gained: {"lines": [217], "branches": [[216, 217]]}

import pytest
from collections import defaultdict

# Mocking the MODULE_CACHE, PATH_CACHE, and PLUGIN_PATH_CACHE
MODULE_CACHE = {}
PATH_CACHE = {}
PLUGIN_PATH_CACHE = {}

from ansible.plugins.loader import PluginLoader

@pytest.fixture
def reset_caches():
    global MODULE_CACHE, PATH_CACHE, PLUGIN_PATH_CACHE
    MODULE_CACHE = {}
    PATH_CACHE = {}
    PLUGIN_PATH_CACHE = {}
    yield
    MODULE_CACHE.clear()
    PATH_CACHE.clear()
    PLUGIN_PATH_CACHE.clear()

def test_plugin_loader_initialization_with_aliases(reset_caches):
    class_name = 'test_class'
    package = 'test_package'
    config = None
    subdir = 'test_subdir'
    aliases = {'alias1': 'value1'}
    required_base_class = object

    loader = PluginLoader(class_name, package, config, subdir, aliases, required_base_class)

    assert loader.class_name == class_name
    assert loader.base_class == required_base_class
    assert loader.package == package
    assert loader.subdir == subdir
    assert loader.aliases == aliases
    assert loader.config == []
    assert loader._extra_dirs == []
    assert loader._module_cache == {}
    assert loader._paths is None
    assert isinstance(loader._plugin_path_cache, defaultdict)
    assert loader._searched_paths == set()

def test_plugin_loader_initialization_without_aliases(reset_caches):
    class_name = 'test_class'
    package = 'test_package'
    config = None
    subdir = 'test_subdir'
    required_base_class = object

    loader = PluginLoader(class_name, package, config, subdir, required_base_class=required_base_class)

    assert loader.class_name == class_name
    assert loader.base_class == required_base_class
    assert loader.package == package
    assert loader.subdir == subdir
    assert loader.aliases == {}
    assert loader.config == []
    assert loader._extra_dirs == []
    assert loader._module_cache == {}
    assert loader._paths is None
    assert isinstance(loader._plugin_path_cache, defaultdict)
    assert loader._searched_paths == set()

def test_plugin_loader_initialization_with_config_list(reset_caches):
    class_name = 'test_class'
    package = 'test_package'
    config = ['config1', 'config2']
    subdir = 'test_subdir'
    required_base_class = object

    loader = PluginLoader(class_name, package, config, subdir, required_base_class=required_base_class)

    assert loader.class_name == class_name
    assert loader.base_class == required_base_class
    assert loader.package == package
    assert loader.subdir == subdir
    assert loader.aliases == {}
    assert loader.config == config
    assert loader._extra_dirs == []
    assert loader._module_cache == {}
    assert loader._paths is None
    assert isinstance(loader._plugin_path_cache, defaultdict)
    assert loader._searched_paths == set()

def test_plugin_loader_initialization_with_single_config(reset_caches):
    class_name = 'test_class'
    package = 'test_package'
    config = 'single_config'
    subdir = 'test_subdir'
    required_base_class = object

    loader = PluginLoader(class_name, package, config, subdir, required_base_class=required_base_class)

    assert loader.class_name == class_name
    assert loader.base_class == required_base_class
    assert loader.package == package
    assert loader.subdir == subdir
    assert loader.aliases == {}
    assert loader.config == [config]
    assert loader._extra_dirs == []
    assert loader._module_cache == {}
    assert loader._paths is None
    assert isinstance(loader._plugin_path_cache, defaultdict)
    assert loader._searched_paths == set()
