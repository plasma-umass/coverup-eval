# file lib/ansible/config/manager.py:37-45
# lines [39, 40, 41, 42, 43, 44, 45]
# branches ['40->41', '40->44', '42->43', '42->44']

import pytest
from ansible.config.manager import _get_entry

def test_get_entry_with_plugin_type_and_name():
    plugin_type = 'test_plugin_type'
    plugin_name = 'test_plugin_name'
    config = 'test_config'
    
    expected_entry = 'plugin_type: test_plugin_type plugin: test_plugin_name setting: test_config '
    entry = _get_entry(plugin_type, plugin_name, config)
    
    assert entry == expected_entry

def test_get_entry_with_plugin_type_without_name():
    plugin_type = 'test_plugin_type'
    plugin_name = None
    config = 'test_config'
    
    expected_entry = 'plugin_type: test_plugin_type setting: test_config '
    entry = _get_entry(plugin_type, plugin_name, config)
    
    assert entry == expected_entry

def test_get_entry_without_plugin_type():
    plugin_type = None
    plugin_name = None
    config = 'test_config'
    
    expected_entry = 'setting: test_config '
    entry = _get_entry(plugin_type, plugin_name, config)
    
    assert entry == expected_entry
