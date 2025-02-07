# file: lib/ansible/vars/clean.py:98-115
# asked: {"lines": [98, 102, 103, 104, 105, 108, 109, 110, 113, 114, 115], "branches": [[102, 103], [102, 108], [103, 102], [103, 104], [108, 109], [108, 113], [109, 108], [109, 110], [113, 0], [113, 114], [114, 113], [114, 115]]}
# gained: {"lines": [98, 102, 103, 104, 105, 108, 109, 110, 113, 114, 115], "branches": [[102, 103], [102, 108], [103, 102], [103, 104], [108, 109], [108, 113], [109, 108], [109, 110], [113, 0], [113, 114], [114, 113], [114, 115]]}

import pytest
from unittest.mock import patch

# Mocking the display.warning function
@pytest.fixture
def mock_display_warning(monkeypatch):
    with patch('ansible.vars.clean.display.warning') as mock_warning:
        yield mock_warning

def test_remove_internal_keys(mock_display_warning):
    from ansible.vars.clean import remove_internal_keys
    from ansible import constants as C

    # Test case 1: Remove keys starting with '_ansible_' except '_ansible_parsed'
    data = {
        '_ansible_foo': 'bar',
        '_ansible_parsed': 'parsed_value',
        'normal_key': 'value'
    }
    remove_internal_keys(data)
    assert '_ansible_foo' not in data
    assert '_ansible_parsed' in data
    assert 'normal_key' in data
    mock_display_warning.assert_called_once_with("Removed unexpected internal key in module return: _ansible_foo = bar")

    # Test case 2: Remove keys in C.INTERNAL_RESULT_KEYS
    data = {
        'key_in_internal_result_keys': 'value',
        'normal_key': 'value'
    }
    C.INTERNAL_RESULT_KEYS = {'key_in_internal_result_keys'}
    remove_internal_keys(data)
    assert 'key_in_internal_result_keys' not in data
    assert 'normal_key' in data
    mock_display_warning.assert_called_with("Removed unexpected internal key in module return: key_in_internal_result_keys = value")

    # Test case 3: Remove empty 'warnings' and 'deprecations' keys
    data = {
        'warnings': [],
        'deprecations': [],
        'normal_key': 'value'
    }
    remove_internal_keys(data)
    assert 'warnings' not in data
    assert 'deprecations' not in data
    assert 'normal_key' in data

    # Test case 4: Remove keys starting with 'discovered_interpreter_' or 'ansible_discovered_interpreter_' in 'ansible_facts'
    data = {
        'ansible_facts': {
            'discovered_interpreter_python': 'value',
            'ansible_discovered_interpreter_python': 'value',
            'normal_fact': 'value'
        }
    }
    remove_internal_keys(data)
    assert 'discovered_interpreter_python' not in data['ansible_facts']
    assert 'ansible_discovered_interpreter_python' not in data['ansible_facts']
    assert 'normal_fact' in data['ansible_facts']
