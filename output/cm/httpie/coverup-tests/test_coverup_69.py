# file httpie/plugins/manager.py:61-62
# lines [61, 62]
# branches []

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import ConverterPlugin

# Mock plugin classes
class MockConverterPlugin(ConverterPlugin):
    pass

class MockNonConverterPlugin:
    pass

@pytest.fixture
def plugin_manager():
    manager = PluginManager()
    yield manager
    manager.clear()

def test_get_converters(plugin_manager):
    # Add a ConverterPlugin and a non-ConverterPlugin to the manager
    plugin_manager.append(MockConverterPlugin)
    plugin_manager.append(MockNonConverterPlugin)

    # Get the converters
    converters = plugin_manager.get_converters()

    # Assert that only ConverterPlugin subclasses are returned
    assert len(converters) == 1
    assert issubclass(converters[0], ConverterPlugin)
    assert not issubclass(converters[0], MockNonConverterPlugin)

    # Clean up is handled by the fixture
