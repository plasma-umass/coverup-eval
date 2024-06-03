# file httpie/plugins/base.py:1-11
# lines [1, 4, 8, 11]
# branches []

import pytest
from httpie.plugins.base import BasePlugin

def test_base_plugin_attributes():
    class TestPlugin(BasePlugin):
        name = "Test Plugin"
        description = "A test plugin"
        package_name = "test_package"

    plugin = TestPlugin()

    assert plugin.name == "Test Plugin"
    assert plugin.description == "A test plugin"
    assert plugin.package_name == "test_package"

@pytest.fixture(autouse=True)
def cleanup_plugin_attributes():
    yield
    BasePlugin.name = None
    BasePlugin.description = None
    BasePlugin.package_name = None
