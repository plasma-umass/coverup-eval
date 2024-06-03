# file httpie/plugins/manager.py:39-40
# lines [39, 40]
# branches []

import pytest
from typing import List, Type
from httpie.plugins.manager import PluginManager
from httpie.plugins import AuthPlugin

class DummyAuthPlugin(AuthPlugin):
    name = 'dummy'
    auth_type = 'dummy'

def test_get_auth_plugins(mocker):
    # Create a mock for AuthPlugin
    mock_auth_plugin = mocker.patch('httpie.plugins.manager.AuthPlugin', DummyAuthPlugin)
    
    # Create an instance of PluginManager and add a dummy auth plugin
    plugin_manager = PluginManager()
    plugin_manager.append(DummyAuthPlugin)
    
    # Call get_auth_plugins and assert the result
    auth_plugins = plugin_manager.get_auth_plugins()
    assert len(auth_plugins) == 1
    assert auth_plugins[0] is DummyAuthPlugin
    
    # Clean up
    mocker.stopall()
