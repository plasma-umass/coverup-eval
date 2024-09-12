# file: httpie/plugins/manager.py:21-23
# asked: {"lines": [21, 22, 23], "branches": [[22, 0], [22, 23]]}
# gained: {"lines": [21, 22, 23], "branches": [[22, 0], [22, 23]]}

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

class DummyPlugin(BasePlugin):
    name = 'dummy'
    description = 'A dummy plugin'
    package_name = 'dummy_package'

def test_register_plugin():
    manager = PluginManager()
    manager.register(DummyPlugin)
    
    assert len(manager) == 1
    assert manager[0] == DummyPlugin

def test_register_multiple_plugins():
    class AnotherDummyPlugin(BasePlugin):
        name = 'another_dummy'
        description = 'Another dummy plugin'
        package_name = 'another_dummy_package'
    
    manager = PluginManager()
    manager.register(DummyPlugin, AnotherDummyPlugin)
    
    assert len(manager) == 2
    assert manager[0] == DummyPlugin
    assert manager[1] == AnotherDummyPlugin
