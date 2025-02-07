# file: httpie/plugins/manager.py:39-40
# asked: {"lines": [39, 40], "branches": []}
# gained: {"lines": [39, 40], "branches": []}

from typing import List, Type
from httpie.plugins import AuthPlugin
from httpie.plugins.manager import PluginManager

def test_get_auth_plugins(monkeypatch):
    class MockAuthPlugin(AuthPlugin):
        name = 'mock'

    class MockNonAuthPlugin:
        pass

    plugins = [MockAuthPlugin, MockNonAuthPlugin]
    manager = PluginManager(plugins)

    def mock_filter(self, by_type):
        return [plugin for plugin in self if issubclass(plugin, by_type)]

    monkeypatch.setattr(PluginManager, 'filter', mock_filter)

    auth_plugins = manager.get_auth_plugins()
    assert auth_plugins == [MockAuthPlugin]
