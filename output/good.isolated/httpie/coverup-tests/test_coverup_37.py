# file httpie/plugins/base.py:1-11
# lines [1, 4, 8, 11]
# branches []

import pytest
from httpie.plugins.base import BasePlugin

def test_base_plugin_attributes():
    class TestPlugin(BasePlugin):
        name = "Test Plugin"
        description = "Test Description"

    plugin = TestPlugin()
    assert plugin.name == "Test Plugin"
    assert plugin.description == "Test Description"
    assert plugin.package_name is None

    # Simulate the plugin loading process where package_name would be set
    plugin.package_name = "test_package"
    assert plugin.package_name == "test_package"
