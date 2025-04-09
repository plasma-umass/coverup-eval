# file: httpie/plugins/manager.py:68-69
# asked: {"lines": [68, 69], "branches": []}
# gained: {"lines": [68, 69], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager

def test_plugin_manager_repr_empty():
    pm = PluginManager()
    assert repr(pm) == '<PluginManager: []>'

def test_plugin_manager_repr_with_items():
    pm = PluginManager()
    pm.append('plugin1')
    pm.append('plugin2')
    assert repr(pm) == "<PluginManager: ['plugin1', 'plugin2']>"

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_plugin_manager_repr_with_fixture(plugin_manager):
    plugin_manager.append('plugin1')
    plugin_manager.append('plugin2')
    assert repr(plugin_manager) == "<PluginManager: ['plugin1', 'plugin2']>"

def test_plugin_manager_repr_cleanup(plugin_manager):
    plugin_manager.append('plugin1')
    assert repr(plugin_manager) == "<PluginManager: ['plugin1']>"
    plugin_manager.clear()
    assert repr(plugin_manager) == "<PluginManager: []>"
