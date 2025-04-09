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

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_unregister_plugin(plugin_manager):
    plugin = DummyPlugin
    plugin_manager.append(plugin)
    assert plugin in plugin_manager

    plugin_manager.unregister(plugin)
    assert plugin not in plugin_manager
