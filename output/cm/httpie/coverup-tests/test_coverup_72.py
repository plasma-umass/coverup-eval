# file httpie/plugins/manager.py:68-69
# lines [68, 69]
# branches []

import pytest
from httpie.plugins.manager import PluginManager

def test_plugin_manager_repr():
    plugin_manager = PluginManager()
    plugin_manager.append('plugin1')
    plugin_manager.append('plugin2')

    expected_repr = "<PluginManager: ['plugin1', 'plugin2']>"
    actual_repr = repr(plugin_manager)

    assert actual_repr == expected_repr
