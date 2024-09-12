# file: httpie/plugins/manager.py:61-62
# asked: {"lines": [61, 62], "branches": []}
# gained: {"lines": [61, 62], "branches": []}

from typing import List, Type
from httpie.plugins import ConverterPlugin
from httpie.plugins.manager import PluginManager
import pytest

class MockConverterPlugin(ConverterPlugin):
    pass

class MockNonConverterPlugin:
    pass

def test_get_converters():
    manager = PluginManager()
    manager.append(MockConverterPlugin)
    manager.append(MockNonConverterPlugin)
    
    converters = manager.get_converters()
    
    assert len(converters) == 1
    assert converters[0] is MockConverterPlugin
