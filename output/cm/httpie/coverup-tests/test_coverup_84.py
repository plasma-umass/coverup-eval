# file httpie/plugins/manager.py:28-29
# lines [28, 29]
# branches []

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

# Mock plugin classes
class PluginA(BasePlugin):
    pass

class PluginB(BasePlugin):
    pass

class UnrelatedClass:
    pass

@pytest.fixture
def plugin_manager():
    manager = PluginManager()
    manager.append(PluginA)
    manager.append(PluginB)
    manager.append(UnrelatedClass)
    return manager

def test_plugin_manager_filter_by_base_plugin_type(plugin_manager):
    filtered_plugins = plugin_manager.filter(by_type=BasePlugin)
    assert PluginA in filtered_plugins
    assert PluginB in filtered_plugins
    assert UnrelatedClass not in filtered_plugins

def test_plugin_manager_filter_by_unrelated_class_type(plugin_manager):
    filtered_plugins = plugin_manager.filter(by_type=UnrelatedClass)
    assert PluginA not in filtered_plugins
    assert PluginB not in filtered_plugins
    assert UnrelatedClass in filtered_plugins  # UnrelatedClass is a subclass of object, which is the default

def test_plugin_manager_filter_without_type(plugin_manager):
    filtered_plugins = plugin_manager.filter(by_type=object)
    assert PluginA in filtered_plugins
    assert PluginB in filtered_plugins
    assert UnrelatedClass in filtered_plugins  # Filtering by object should include all classes
