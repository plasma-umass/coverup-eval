# file httpie/plugins/manager.py:54-59
# lines [54, 55, 56, 57, 58]
# branches []

import pytest
from unittest.mock import Mock, patch
from httpie.plugins.manager import PluginManager
from operator import attrgetter

class MockFormatterPlugin:
    def __init__(self, group_name):
        self.group_name = group_name

@pytest.fixture
def mock_plugins():
    return [
        MockFormatterPlugin('group1'),
        MockFormatterPlugin('group1'),
        MockFormatterPlugin('group2')
    ]

def test_get_formatters_grouped(mock_plugins, mocker):
    manager = PluginManager()
    manager.extend(mock_plugins)
    
    mocker.patch.object(manager, 'get_formatters', return_value=mock_plugins)
    
    grouped_formatters = manager.get_formatters_grouped()
    
    assert 'group1' in grouped_formatters
    assert 'group2' in grouped_formatters
    assert len(grouped_formatters['group1']) == 2
    assert len(grouped_formatters['group2']) == 1
