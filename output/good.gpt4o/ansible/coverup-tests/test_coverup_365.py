# file lib/ansible/config/manager.py:37-45
# lines [37, 39, 40, 41, 42, 43, 44, 45]
# branches ['40->41', '40->44', '42->43', '42->44']

import pytest
from ansible.config.manager import _get_entry

def test_get_entry_with_plugin_type_and_name():
    result = _get_entry('test_type', 'test_name', 'test_config')
    assert result == 'plugin_type: test_type plugin: test_name setting: test_config '

def test_get_entry_with_plugin_type_only():
    result = _get_entry('test_type', None, 'test_config')
    assert result == 'plugin_type: test_type setting: test_config '

def test_get_entry_with_no_plugin_type():
    result = _get_entry(None, None, 'test_config')
    assert result == 'setting: test_config '
