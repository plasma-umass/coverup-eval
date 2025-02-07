# file: httpie/plugins/manager.py:54-59
# asked: {"lines": [54, 55, 56, 57, 58], "branches": []}
# gained: {"lines": [54, 55, 56, 57, 58], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager, FormatterPlugin

class MockFormatterPlugin(FormatterPlugin):
    group_name = 'test_group'
    
    def __init__(self, **kwargs):
        self.enabled = True
        self.kwargs = kwargs
        self.format_options = kwargs.get('format_options', {})

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_get_formatters_grouped(plugin_manager):
    mock_formatter = MockFormatterPlugin(format_options={})
    
    with patch.object(plugin_manager, 'get_formatters', return_value=[mock_formatter]):
        grouped_formatters = plugin_manager.get_formatters_grouped()
        
        assert 'test_group' in grouped_formatters
        assert grouped_formatters['test_group'] == [mock_formatter]
