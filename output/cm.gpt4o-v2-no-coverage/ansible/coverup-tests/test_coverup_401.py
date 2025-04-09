# file: lib/ansible/plugins/loader.py:276-292
# asked: {"lines": [276, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291], "branches": []}
# gained: {"lines": [276, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291], "branches": []}

import pytest
from ansible.plugins.loader import PluginLoader
from ansible.plugins import PATH_CACHE, PLUGIN_PATH_CACHE

@pytest.fixture
def setup_plugin_loader():
    class MockPluginLoader(PluginLoader):
        def __init__(self):
            self.class_name = 'test_class'
            self.base_class = 'test_base_class'
            self.package = 'test_package'
            self.config = 'test_config'
            self.subdir = 'test_subdir'
            self.aliases = 'test_aliases'
            self._extra_dirs = 'test_extra_dirs'
            self._searched_paths = 'test_searched_paths'
            PATH_CACHE[self.class_name] = 'test_path_cache'
            PLUGIN_PATH_CACHE[self.class_name] = 'test_plugin_path_cache'
    
    loader = MockPluginLoader()
    yield loader
    
    # Cleanup
    del PATH_CACHE[loader.class_name]
    del PLUGIN_PATH_CACHE[loader.class_name]

def test_getstate(setup_plugin_loader):
    loader = setup_plugin_loader
    state = loader.__getstate__()
    
    assert state['class_name'] == 'test_class'
    assert state['base_class'] == 'test_base_class'
    assert state['package'] == 'test_package'
    assert state['config'] == 'test_config'
    assert state['subdir'] == 'test_subdir'
    assert state['aliases'] == 'test_aliases'
    assert state['_extra_dirs'] == 'test_extra_dirs'
    assert state['_searched_paths'] == 'test_searched_paths'
    assert state['PATH_CACHE'] == 'test_path_cache'
    assert state['PLUGIN_PATH_CACHE'] == 'test_plugin_path_cache'
