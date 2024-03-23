# file httpie/plugins/manager.py:54-59
# lines [54, 55, 56, 57, 58]
# branches []

import pytest
from httpie.plugins.manager import PluginManager
from httpie.plugins.base import FormatterPlugin
from operator import attrgetter
from itertools import groupby
from typing import Type, Dict, List

# Mock FormatterPlugin classes with different group names
class FormatterPluginA(FormatterPlugin):
    group_name = 'A'

class FormatterPluginB(FormatterPlugin):
    group_name = 'B'

class FormatterPluginC(FormatterPlugin):
    group_name = 'A'  # Same group as FormatterPluginA

@pytest.fixture
def plugin_manager():
    manager = PluginManager()
    # Add the plugins in a sorted order by group_name to ensure groupby works correctly
    manager.extend(sorted([FormatterPluginA, FormatterPluginB, FormatterPluginC], key=attrgetter('group_name')))
    return manager

def test_get_formatters_grouped(plugin_manager):
    grouped_formatters = plugin_manager.get_formatters_grouped()
    assert isinstance(grouped_formatters, dict)
    assert set(grouped_formatters.keys()) == {'A', 'B'}
    # Check if the correct classes are in the correct group
    assert all(issubclass(plugin, FormatterPlugin) for plugin in grouped_formatters['A'])
    assert all(issubclass(plugin, FormatterPlugin) for plugin in grouped_formatters['B'])
    assert len(grouped_formatters['A']) == 2
    assert len(grouped_formatters['B']) == 1
    # Check if the specific classes are in the groups
    assert FormatterPluginA in grouped_formatters['A']
    assert FormatterPluginC in grouped_formatters['A']
    assert FormatterPluginB in grouped_formatters['B']
