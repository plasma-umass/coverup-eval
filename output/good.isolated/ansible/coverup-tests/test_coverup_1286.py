# file lib/ansible/plugins/loader.py:241-255
# lines [243, 244, 247, 248, 249, 252, 253, 254, 255]
# branches ['243->244', '243->247']

import pytest
from ansible.plugins.loader import PluginLoader, MODULE_CACHE, PATH_CACHE, PLUGIN_PATH_CACHE
from collections import defaultdict
from unittest.mock import patch, MagicMock

# Assuming C is a configuration object that contains OLD_PLUGIN_CACHE_CLEARING
# Since the import failed, we'll mock C for the purpose of this test
C = MagicMock()
C.OLD_PLUGIN_CACHE_CLEARING = False

@pytest.fixture
def plugin_loader():
    # Mock the required arguments for PluginLoader
    class_name = 'test_plugin'
    package = 'ansible.plugins'
    config = {}
    subdir = ''
    return PluginLoader(class_name, package, config, subdir)

@pytest.fixture
def cleanup():
    # Cleanup function to reset the caches after the test
    yield
    MODULE_CACHE.clear()
    PATH_CACHE.clear()
    PLUGIN_PATH_CACHE.clear()

def test_plugin_loader_clear_caches_old_cache_clearing(plugin_loader, cleanup):
    # Set the OLD_PLUGIN_CACHE_CLEARING to True to test the old cache clearing code
    with patch('ansible.plugins.loader.C.OLD_PLUGIN_CACHE_CLEARING', True):
        plugin_loader._clear_caches()
        assert plugin_loader._paths is None

def test_plugin_loader_clear_caches_new_cache_clearing(plugin_loader, cleanup):
    # Set the OLD_PLUGIN_CACHE_CLEARING to False to test the new cache clearing code
    with patch('ansible.plugins.loader.C.OLD_PLUGIN_CACHE_CLEARING', False):
        plugin_loader._clear_caches()
        assert MODULE_CACHE[plugin_loader.class_name] == {}
        assert PATH_CACHE[plugin_loader.class_name] is None
        assert isinstance(PLUGIN_PATH_CACHE[plugin_loader.class_name], defaultdict)
        assert plugin_loader._module_cache == MODULE_CACHE[plugin_loader.class_name]
        assert plugin_loader._paths == PATH_CACHE[plugin_loader.class_name]
        assert plugin_loader._plugin_path_cache == PLUGIN_PATH_CACHE[plugin_loader.class_name]
        assert plugin_loader._searched_paths == set()
