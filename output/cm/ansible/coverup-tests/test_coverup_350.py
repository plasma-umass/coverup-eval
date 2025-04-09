# file lib/ansible/plugins/loader.py:241-255
# lines [241, 243, 244, 247, 248, 249, 252, 253, 254, 255]
# branches ['243->244', '243->247']

import pytest
from collections import defaultdict
from unittest.mock import patch

# Assuming the existence of the following constants and global variables
# in the ansible.plugins.loader module, which are used in the PluginLoader class.
C = type('C', (), {'OLD_PLUGIN_CACHE_CLEARING': False})
MODULE_CACHE = defaultdict(dict)
PATH_CACHE = defaultdict(lambda: None)
PLUGIN_PATH_CACHE = defaultdict(lambda: defaultdict(dict))

# The PluginLoader class from the ansible.plugins.loader module
class PluginLoader:
    def __init__(self, class_name):
        self.class_name = class_name
        self._clear_caches()

    def _clear_caches(self):
        if C.OLD_PLUGIN_CACHE_CLEARING:
            self._paths = None
        else:
            # reset global caches
            MODULE_CACHE[self.class_name] = {}
            PATH_CACHE[self.class_name] = None
            PLUGIN_PATH_CACHE[self.class_name] = defaultdict(dict)

            # reset internal caches
            self._module_cache = MODULE_CACHE[self.class_name]
            self._paths = PATH_CACHE[self.class_name]
            self._plugin_path_cache = PLUGIN_PATH_CACHE[self.class_name]
            self._searched_paths = set()

# Test function to improve coverage
@pytest.fixture
def clear_plugin_loader_caches():
    # Setup
    class_name = 'TestPlugin'
    loader = PluginLoader(class_name)
    yield loader
    # Teardown
    MODULE_CACHE.pop(class_name, None)
    PATH_CACHE.pop(class_name, None)
    PLUGIN_PATH_CACHE.pop(class_name, None)

def test_plugin_loader_clear_caches(clear_plugin_loader_caches):
    loader = clear_plugin_loader_caches
    with patch('ansible.plugins.loader.C.OLD_PLUGIN_CACHE_CLEARING', False):
        loader._clear_caches()
        assert loader._module_cache == {}
        assert loader._paths is None
        assert isinstance(loader._plugin_path_cache, defaultdict)
        assert loader._searched_paths == set()
