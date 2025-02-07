# file: httpie/plugins/manager.py:68-69
# asked: {"lines": [68, 69], "branches": []}
# gained: {"lines": [68, 69], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager

def test_plugin_manager_repr():
    pm = PluginManager()
    pm.append('plugin1')
    pm.append('plugin2')
    assert repr(pm) == "<PluginManager: ['plugin1', 'plugin2']>"
