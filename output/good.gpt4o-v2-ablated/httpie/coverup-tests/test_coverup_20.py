# file: httpie/plugins/manager.py:21-23
# asked: {"lines": [21, 22, 23], "branches": [[22, 0], [22, 23]]}
# gained: {"lines": [21, 22, 23], "branches": [[22, 0], [22, 23]]}

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

class DummyPlugin(BasePlugin):
    pass

class AnotherDummyPlugin(BasePlugin):
    pass

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_register_single_plugin(plugin_manager):
    plugin_manager.register(DummyPlugin)
    assert len(plugin_manager) == 1
    assert plugin_manager[0] is DummyPlugin

def test_register_multiple_plugins(plugin_manager):
    plugin_manager.register(DummyPlugin, AnotherDummyPlugin)
    assert len(plugin_manager) == 2
    assert plugin_manager[0] is DummyPlugin
    assert plugin_manager[1] is AnotherDummyPlugin

def test_register_no_plugins(plugin_manager):
    plugin_manager.register()
    assert len(plugin_manager) == 0
