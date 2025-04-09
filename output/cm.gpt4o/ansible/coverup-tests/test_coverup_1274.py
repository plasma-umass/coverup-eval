# file lib/ansible/plugins/loader.py:203-236
# lines [217]
# branches ['216->217']

import pytest
from collections import defaultdict
from ansible.plugins.loader import PluginLoader

MODULE_CACHE = {}
PATH_CACHE = {}
PLUGIN_PATH_CACHE = {}

@pytest.fixture
def reset_caches():
    global MODULE_CACHE, PATH_CACHE, PLUGIN_PATH_CACHE
    MODULE_CACHE = {}
    PATH_CACHE = {}
    PLUGIN_PATH_CACHE = {}
    yield
    MODULE_CACHE = {}
    PATH_CACHE = {}
    PLUGIN_PATH_CACHE = {}

def test_plugin_loader_no_config(reset_caches):
    class_name = 'test_class'
    package = 'test_package'
    config = None
    subdir = 'test_subdir'
    aliases = None
    required_base_class = None

    loader = PluginLoader(class_name, package, config, subdir, aliases, required_base_class)

    assert loader.class_name == class_name
    assert loader.package == package
    assert loader.subdir == subdir
    assert loader.aliases == {}
    assert loader.config == []
    assert loader._module_cache == {}
    assert loader._paths is None
    assert isinstance(loader._plugin_path_cache, defaultdict)
    assert loader._searched_paths == set()
