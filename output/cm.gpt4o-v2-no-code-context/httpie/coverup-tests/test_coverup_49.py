# file: httpie/plugins/manager.py:54-59
# asked: {"lines": [54, 55, 56, 57, 58], "branches": []}
# gained: {"lines": [54, 55, 56, 57, 58], "branches": []}

import pytest
from httpie.plugins.manager import PluginManager
from unittest.mock import MagicMock, patch
from itertools import groupby
from operator import attrgetter

class MockFormatterPlugin:
    def __init__(self, group_name):
        self.group_name = group_name

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_get_formatters_grouped(plugin_manager, monkeypatch):
    # Create mock formatter plugins
    formatter1 = MockFormatterPlugin(group_name='group1')
    formatter2 = MockFormatterPlugin(group_name='group1')
    formatter3 = MockFormatterPlugin(group_name='group2')

    # Mock the get_formatters method to return the mock formatters
    monkeypatch.setattr(plugin_manager, 'get_formatters', lambda: [formatter1, formatter2, formatter3])

    # Call the method under test
    grouped_formatters = plugin_manager.get_formatters_grouped()

    # Verify the result
    assert 'group1' in grouped_formatters
    assert 'group2' in grouped_formatters
    assert grouped_formatters['group1'] == [formatter1, formatter2]
    assert grouped_formatters['group2'] == [formatter3]
