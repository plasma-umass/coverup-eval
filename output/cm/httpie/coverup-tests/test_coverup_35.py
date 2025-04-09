# file httpie/plugins/manager.py:21-23
# lines [21, 22, 23]
# branches ['22->exit', '22->23']

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import BasePlugin

# Mock plugin class
class MockPlugin(BasePlugin):
    pass

# Test function to improve coverage
def test_plugin_manager_register():
    manager = PluginManager()
    mock_plugin = MockPlugin

    # Before registering
    assert mock_plugin not in manager

    # Register the mock plugin
    manager.register(mock_plugin)

    # After registering
    assert mock_plugin in manager

    # Clean up (though in this case, the manager is a local variable and will be discarded)
