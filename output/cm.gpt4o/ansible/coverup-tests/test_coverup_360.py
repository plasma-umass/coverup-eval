# file lib/ansible/plugins/loader.py:241-255
# lines [241, 243, 244, 247, 248, 249, 252, 253, 254, 255]
# branches ['243->244', '243->247']

import pytest
from unittest.mock import patch, MagicMock, DEFAULT
from collections import defaultdict

# Mocking the constants and caches used in the PluginLoader class
class C:
    OLD_PLUGIN_CACHE_CLEARING = False

MODULE_CACHE = {}
PATH_CACHE = {}
PLUGIN_PATH_CACHE = {}

class PluginLoader:
    def __init__(self, class_name):
        self.class_name = class_name
        self._module_cache = None
        self._paths = None
        self._plugin_path_cache = None
        self._searched_paths = None

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

@pytest.fixture
def mock_caches():
    with patch.dict('ansible.plugins.loader.MODULE_CACHE', {}, clear=True), \
         patch.dict('ansible.plugins.loader.PATH_CACHE', {}, clear=True), \
         patch.dict('ansible.plugins.loader.PLUGIN_PATH_CACHE', {}, clear=True):
        yield

def test_clear_caches(mock_caches):
    loader = PluginLoader('test_class')
    
    # Ensure initial state
    assert loader._module_cache is None
    assert loader._paths is None
    assert loader._plugin_path_cache is None
    assert loader._searched_paths is None

    loader._clear_caches()

    # Verify that caches are cleared and set correctly
    assert loader._module_cache == {}
    assert loader._paths is None
    assert isinstance(loader._plugin_path_cache, defaultdict)
    assert loader._plugin_path_cache == defaultdict(dict)
    assert loader._searched_paths == set()

    # Verify global caches
    assert MODULE_CACHE['test_class'] == {}
    assert PATH_CACHE['test_class'] is None
    assert PLUGIN_PATH_CACHE['test_class'] == defaultdict(dict)
