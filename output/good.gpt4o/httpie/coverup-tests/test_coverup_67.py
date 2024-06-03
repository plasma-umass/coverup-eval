# file httpie/plugins/manager.py:68-69
# lines [68, 69]
# branches []

import pytest
from httpie.plugins.manager import PluginManager

def test_plugin_manager_repr():
    # Create an instance of PluginManager
    pm = PluginManager()
    
    # Add some mock plugins to the manager
    pm.append('plugin1')
    pm.append('plugin2')
    
    # Check the __repr__ output
    expected_repr = "<PluginManager: ['plugin1', 'plugin2']>"
    assert repr(pm) == expected_repr

    # Clean up by clearing the PluginManager instance
    pm.clear()
    assert len(pm) == 0
