# file: httpie/plugins/manager.py:28-29
# asked: {"lines": [28, 29], "branches": []}
# gained: {"lines": [28, 29], "branches": []}

import pytest
from typing import Type
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

class DummyPlugin(BasePlugin):
    pass

class AnotherPlugin:
    pass

def test_plugin_manager_filter():
    manager = PluginManager([DummyPlugin, AnotherPlugin])
    
    filtered_plugins = manager.filter(by_type=BasePlugin)
    
    assert filtered_plugins == [DummyPlugin]
