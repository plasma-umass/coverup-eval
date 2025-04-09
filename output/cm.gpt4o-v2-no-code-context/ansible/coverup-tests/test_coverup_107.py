# file: lib/ansible/vars/clean.py:98-115
# asked: {"lines": [98, 102, 103, 104, 105, 108, 109, 110, 113, 114, 115], "branches": [[102, 103], [102, 108], [103, 102], [103, 104], [108, 109], [108, 113], [109, 108], [109, 110], [113, 0], [113, 114], [114, 113], [114, 115]]}
# gained: {"lines": [98, 102, 103, 104, 105, 108, 109, 110, 113, 114, 115], "branches": [[102, 103], [102, 108], [103, 102], [103, 104], [108, 109], [108, 113], [109, 108], [109, 110], [113, 0], [113, 114], [114, 113], [114, 115]]}

import pytest
from unittest.mock import patch

# Assuming the function remove_internal_keys is imported from ansible/vars/clean.py
from ansible.vars.clean import remove_internal_keys

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch('ansible.vars.clean.display.warning')

def test_remove_internal_keys_with_ansible_keys(mock_display_warning):
    data = {
        '_ansible_foo': 'bar',
        '_ansible_parsed': True,
        'some_key': 'some_value'
    }
    remove_internal_keys(data)
    assert '_ansible_foo' not in data
    assert '_ansible_parsed' in data
    assert 'some_key' in data
    mock_display_warning.assert_called_once_with("Removed unexpected internal key in module return: _ansible_foo = bar")

def test_remove_internal_keys_with_internal_result_keys(mock_display_warning):
    data = {
        'some_internal_key': 'value',
        'another_key': 'another_value'
    }
    with patch('ansible.vars.clean.C.INTERNAL_RESULT_KEYS', new=['some_internal_key']):
        remove_internal_keys(data)
    assert 'some_internal_key' not in data
    assert 'another_key' in data
    mock_display_warning.assert_called_once_with("Removed unexpected internal key in module return: some_internal_key = value")

def test_remove_internal_keys_with_empty_warnings_and_deprecations():
    data = {
        'warnings': [],
        'deprecations': [],
        'some_key': 'some_value'
    }
    remove_internal_keys(data)
    assert 'warnings' not in data
    assert 'deprecations' not in data
    assert 'some_key' in data

def test_remove_internal_keys_with_ansible_facts():
    data = {
        'ansible_facts': {
            'discovered_interpreter_python': '/usr/bin/python',
            'ansible_discovered_interpreter_python': '/usr/bin/python',
            'some_fact': 'some_value'
        }
    }
    remove_internal_keys(data)
    assert 'discovered_interpreter_python' not in data['ansible_facts']
    assert 'ansible_discovered_interpreter_python' not in data['ansible_facts']
    assert 'some_fact' in data['ansible_facts']
