# file httpie/plugins/manager.py:28-29
# lines [28, 29]
# branches []

import pytest
from httpie.plugins.manager import PluginManager, BasePlugin

class DummyPlugin(BasePlugin):
    pass

class AnotherPlugin:
    pass

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_plugin_manager_filter(plugin_manager):
    plugin_manager.append(DummyPlugin)
    plugin_manager.append(AnotherPlugin)
    
    filtered_plugins = plugin_manager.filter(by_type=BasePlugin)
    
    assert len(filtered_plugins) == 1
    assert filtered_plugins[0] is DummyPlugin
