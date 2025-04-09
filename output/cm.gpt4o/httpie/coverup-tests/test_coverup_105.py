# file httpie/plugins/manager.py:61-62
# lines [62]
# branches []

import pytest
from httpie.plugins.manager import PluginManager, ConverterPlugin

class DummyConverterPlugin(ConverterPlugin):
    def __init__(self):
        super().__init__(mime='application/test')

def test_get_converters(mocker):
    plugin_manager = PluginManager()
    dummy_plugin = DummyConverterPlugin()
    plugin_manager.append(dummy_plugin)
    
    mocker.patch.object(plugin_manager, 'filter', return_value=[dummy_plugin])
    
    converters = plugin_manager.get_converters()
    
    assert converters == [dummy_plugin]
    plugin_manager.filter.assert_called_once_with(ConverterPlugin)
