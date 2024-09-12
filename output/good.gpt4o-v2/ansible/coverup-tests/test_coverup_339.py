# file: lib/ansible/plugins/loader.py:241-255
# asked: {"lines": [241, 243, 244, 247, 248, 249, 252, 253, 254, 255], "branches": [[243, 244], [243, 247]]}
# gained: {"lines": [241, 243, 244, 247, 248, 249, 252, 253, 254, 255], "branches": [[243, 244], [243, 247]]}

import pytest
from collections import defaultdict
from ansible.plugins.loader import PluginLoader
from ansible import constants as C
from ansible.plugins import MODULE_CACHE, PATH_CACHE, PLUGIN_PATH_CACHE

@pytest.fixture
def plugin_loader():
    class_name = 'test_class'
    package = 'test_package'
    config = None
    subdir = 'test_subdir'
    return PluginLoader(class_name, package, config, subdir)

def test_clear_caches_old_plugin_cache_clearing(monkeypatch, plugin_loader):
    monkeypatch.setattr(C, 'OLD_PLUGIN_CACHE_CLEARING', True)
    plugin_loader._paths = 'some_path'
    plugin_loader._clear_caches()
    assert plugin_loader._paths is None

def test_clear_caches_new_plugin_cache_clearing(monkeypatch, plugin_loader):
    monkeypatch.setattr(C, 'OLD_PLUGIN_CACHE_CLEARING', False)
    plugin_loader._clear_caches()
    assert MODULE_CACHE[plugin_loader.class_name] == {}
    assert PATH_CACHE[plugin_loader.class_name] is None
    assert isinstance(PLUGIN_PATH_CACHE[plugin_loader.class_name], defaultdict)
    assert plugin_loader._module_cache == MODULE_CACHE[plugin_loader.class_name]
    assert plugin_loader._paths == PATH_CACHE[plugin_loader.class_name]
    assert plugin_loader._plugin_path_cache == PLUGIN_PATH_CACHE[plugin_loader.class_name]
    assert plugin_loader._searched_paths == set()
