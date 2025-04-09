# file httpie/plugins/manager.py:25-26
# lines [26]
# branches []

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

class DummyPlugin(BasePlugin):
    name = 'dummy'

def test_unregister_plugin():
    manager = PluginManager()
    plugin = DummyPlugin
    manager.append(plugin)
    
    assert plugin in manager  # Ensure the plugin is registered
    
    manager.unregister(plugin)
    
    assert plugin not in manager  # Ensure the plugin is unregistered
