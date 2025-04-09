# file: httpie/plugins/manager.py:28-29
# asked: {"lines": [28, 29], "branches": []}
# gained: {"lines": [28, 29], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

class DummyPlugin(BasePlugin):
    pass

class AnotherPlugin:
    pass

def test_plugin_manager_filter_with_base_plugin():
    manager = PluginManager()
    manager.append(DummyPlugin)
    manager.append(AnotherPlugin)
    
    filtered_plugins = manager.filter(by_type=BasePlugin)
    
    assert len(filtered_plugins) == 1
    assert filtered_plugins[0] is DummyPlugin

def test_plugin_manager_filter_with_another_plugin():
    manager = PluginManager()
    manager.append(AnotherPlugin)
    
    filtered_plugins = manager.filter(by_type=BasePlugin)
    
    assert len(filtered_plugins) == 0
