# file: httpie/plugins/manager.py:61-62
# asked: {"lines": [61, 62], "branches": []}
# gained: {"lines": [61, 62], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins import ConverterPlugin

class DummyConverterPlugin(ConverterPlugin):
    def __init__(self):
        super().__init__(mime='application/dummy')

    def convert(self, content_bytes):
        return content_bytes

    @classmethod
    def supports(cls, mime):
        return mime == 'application/dummy'

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_get_converters(plugin_manager, monkeypatch):
    dummy_plugin = DummyConverterPlugin()
    
    def mock_filter(by_type):
        if by_type is ConverterPlugin:
            return [dummy_plugin]
        return []

    monkeypatch.setattr(plugin_manager, 'filter', mock_filter)
    
    converters = plugin_manager.get_converters()
    
    assert len(converters) == 1
    assert converters[0] is dummy_plugin
