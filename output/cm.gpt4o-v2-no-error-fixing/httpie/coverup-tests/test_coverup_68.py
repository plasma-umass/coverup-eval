# file: httpie/plugins/manager.py:61-62
# asked: {"lines": [61, 62], "branches": []}
# gained: {"lines": [61, 62], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins import ConverterPlugin

class DummyConverterPlugin(ConverterPlugin):
    pass

class DummyNonConverterPlugin:
    pass

def test_get_converters():
    manager = PluginManager()
    manager.append(DummyConverterPlugin)
    manager.append(DummyNonConverterPlugin)
    
    converters = manager.get_converters()
    
    assert len(converters) == 1
    assert converters[0] is DummyConverterPlugin
