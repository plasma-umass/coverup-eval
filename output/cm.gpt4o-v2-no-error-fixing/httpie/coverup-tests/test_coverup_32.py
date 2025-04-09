# file: httpie/plugins/manager.py:21-23
# asked: {"lines": [21, 22, 23], "branches": [[22, 0], [22, 23]]}
# gained: {"lines": [21, 22, 23], "branches": [[22, 0], [22, 23]]}

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

class DummyPlugin(BasePlugin):
    name = 'dummy'

def test_register_plugin():
    manager = PluginManager()
    plugin = DummyPlugin

    # Register the plugin
    manager.register(plugin)

    # Assert that the plugin was added to the manager
    assert plugin in manager

    # Clean up
    manager.clear()
