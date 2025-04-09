# file: httpie/plugins/manager.py:39-40
# asked: {"lines": [39, 40], "branches": []}
# gained: {"lines": [39, 40], "branches": []}

from typing import List, Type
from httpie.plugins import AuthPlugin
from httpie.plugins.manager import PluginManager
import pytest

class DummyAuthPlugin(AuthPlugin):
    name = 'dummy-auth'

class DummyNonAuthPlugin:
    pass

def test_get_auth_plugins():
    manager = PluginManager()
    manager.append(DummyAuthPlugin)
    manager.append(DummyNonAuthPlugin)
    
    auth_plugins = manager.get_auth_plugins()
    
    assert len(auth_plugins) == 1
    assert auth_plugins[0] is DummyAuthPlugin

def test_get_auth_plugins_empty():
    manager = PluginManager()
    
    auth_plugins = manager.get_auth_plugins()
    
    assert len(auth_plugins) == 0

def test_get_auth_plugins_no_auth():
    manager = PluginManager()
    manager.append(DummyNonAuthPlugin)
    
    auth_plugins = manager.get_auth_plugins()
    
    assert len(auth_plugins) == 0
