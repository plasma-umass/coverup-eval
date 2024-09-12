# file: httpie/plugins/manager.py:25-26
# asked: {"lines": [25, 26], "branches": []}
# gained: {"lines": [25, 26], "branches": []}

import pytest
from httpie.plugins.base import BasePlugin
from httpie.plugins.manager import PluginManager

class DummyPlugin(BasePlugin):
    name = 'dummy'

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_unregister_existing_plugin(plugin_manager):
    plugin = DummyPlugin
    plugin_manager.append(plugin)
    assert plugin in plugin_manager
    plugin_manager.unregister(plugin)
    assert plugin not in plugin_manager

def test_unregister_non_existing_plugin(plugin_manager):
    plugin = DummyPlugin
    assert plugin not in plugin_manager
    with pytest.raises(ValueError):
        plugin_manager.unregister(plugin)
