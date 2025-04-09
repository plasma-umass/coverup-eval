# file: lib/ansible/config/manager.py:37-45
# asked: {"lines": [37, 39, 40, 41, 42, 43, 44, 45], "branches": [[40, 41], [40, 44], [42, 43], [42, 44]]}
# gained: {"lines": [37, 39, 40, 41, 42, 43, 44, 45], "branches": [[40, 41], [40, 44], [42, 43], [42, 44]]}

import pytest

from ansible.config.manager import _get_entry

def test_get_entry_with_plugin_type_and_name():
    result = _get_entry('type1', 'name1', 'config1')
    assert result == 'plugin_type: type1 plugin: name1 setting: config1 '

def test_get_entry_with_plugin_type_only():
    result = _get_entry('type1', '', 'config1')
    assert result == 'plugin_type: type1 setting: config1 '

def test_get_entry_with_plugin_name_only():
    result = _get_entry('', 'name1', 'config1')
    assert result == 'setting: config1 '

def test_get_entry_with_no_plugin_type_and_name():
    result = _get_entry('', '', 'config1')
    assert result == 'setting: config1 '
