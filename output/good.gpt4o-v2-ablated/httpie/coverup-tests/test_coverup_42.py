# file: httpie/plugins/manager.py:28-29
# asked: {"lines": [29], "branches": []}
# gained: {"lines": [29], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager, BasePlugin

class DummyPlugin(BasePlugin):
    pass

class AnotherPlugin(BasePlugin):
    pass

class NotAPlugin:
    pass

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_filter_with_matching_type(plugin_manager):
    plugin_manager.append(DummyPlugin)
    plugin_manager.append(AnotherPlugin)
    plugin_manager.append(NotAPlugin)
    
    filtered_plugins = plugin_manager.filter(by_type=BasePlugin)
    
    assert DummyPlugin in filtered_plugins
    assert AnotherPlugin in filtered_plugins
    assert NotAPlugin not in filtered_plugins

def test_filter_with_no_matching_type(plugin_manager):
    plugin_manager.append(NotAPlugin)
    
    filtered_plugins = plugin_manager.filter(by_type=BasePlugin)
    
    assert len(filtered_plugins) == 0

def test_filter_with_empty_manager(plugin_manager):
    filtered_plugins = plugin_manager.filter(by_type=BasePlugin)
    
    assert len(filtered_plugins) == 0
