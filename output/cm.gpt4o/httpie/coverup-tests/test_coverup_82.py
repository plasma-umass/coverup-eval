# file httpie/plugins/manager.py:19-20
# lines [19]
# branches []

import pytest
from httpie.plugins.manager import PluginManager

@pytest.fixture
def mock_plugin_manager():
    return PluginManager()

def test_plugin_manager_append(mock_plugin_manager):
    plugin = "test_plugin"
    mock_plugin_manager.append(plugin)
    assert plugin in mock_plugin_manager

def test_plugin_manager_extend(mock_plugin_manager):
    plugins = ["plugin1", "plugin2"]
    mock_plugin_manager.extend(plugins)
    assert all(plugin in mock_plugin_manager for plugin in plugins)

def test_plugin_manager_insert(mock_plugin_manager):
    plugin = "test_plugin"
    mock_plugin_manager.insert(0, plugin)
    assert mock_plugin_manager[0] == plugin

def test_plugin_manager_remove(mock_plugin_manager):
    plugin = "test_plugin"
    mock_plugin_manager.append(plugin)
    mock_plugin_manager.remove(plugin)
    assert plugin not in mock_plugin_manager

def test_plugin_manager_pop(mock_plugin_manager):
    plugin = "test_plugin"
    mock_plugin_manager.append(plugin)
    popped_plugin = mock_plugin_manager.pop()
    assert popped_plugin == plugin
    assert plugin not in mock_plugin_manager

def test_plugin_manager_clear(mock_plugin_manager):
    plugins = ["plugin1", "plugin2"]
    mock_plugin_manager.extend(plugins)
    mock_plugin_manager.clear()
    assert len(mock_plugin_manager) == 0

def test_plugin_manager_index(mock_plugin_manager):
    plugin = "test_plugin"
    mock_plugin_manager.append(plugin)
    index = mock_plugin_manager.index(plugin)
    assert index == 0

def test_plugin_manager_count(mock_plugin_manager):
    plugin = "test_plugin"
    mock_plugin_manager.append(plugin)
    count = mock_plugin_manager.count(plugin)
    assert count == 1

def test_plugin_manager_sort(mock_plugin_manager):
    plugins = ["plugin2", "plugin1"]
    mock_plugin_manager.extend(plugins)
    mock_plugin_manager.sort()
    assert mock_plugin_manager == ["plugin1", "plugin2"]

def test_plugin_manager_reverse(mock_plugin_manager):
    plugins = ["plugin1", "plugin2"]
    mock_plugin_manager.extend(plugins)
    mock_plugin_manager.reverse()
    assert mock_plugin_manager == ["plugin2", "plugin1"]
