# file: httpie/plugins/manager.py:25-26
# asked: {"lines": [25, 26], "branches": []}
# gained: {"lines": [25, 26], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

class DummyPlugin(BasePlugin):
    name = 'dummy'
    description = 'A dummy plugin'
    package_name = 'dummy_package'

def test_unregister_plugin():
    manager = PluginManager()
    plugin = DummyPlugin
    manager.append(plugin)
    
    assert plugin in manager
    
    manager.unregister(plugin)
    
    assert plugin not in manager
