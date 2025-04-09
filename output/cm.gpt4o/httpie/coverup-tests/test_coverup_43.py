# file httpie/plugins/manager.py:21-23
# lines [21, 22, 23]
# branches ['22->exit', '22->23']

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

class DummyPlugin(BasePlugin):
    name = 'DummyPlugin'

def test_plugin_manager_register():
    manager = PluginManager()
    assert len(manager) == 0

    manager.register(DummyPlugin)
    assert len(manager) == 1
    assert manager[0] is DummyPlugin

    manager.register(DummyPlugin, DummyPlugin)
    assert len(manager) == 3
    assert manager[1] is DummyPlugin
    assert manager[2] is DummyPlugin
