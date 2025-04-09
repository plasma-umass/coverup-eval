# file httpie/plugins/manager.py:25-26
# lines [25, 26]
# branches []

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

class DummyPlugin(BasePlugin):
    pass

def test_unregister_plugin():
    manager = PluginManager()
    manager.append(DummyPlugin)
    
    # Ensure the plugin is registered
    assert DummyPlugin in manager
    
    # Unregister the plugin
    manager.unregister(DummyPlugin)
    
    # Ensure the plugin is no longer registered
    assert DummyPlugin not in manager
