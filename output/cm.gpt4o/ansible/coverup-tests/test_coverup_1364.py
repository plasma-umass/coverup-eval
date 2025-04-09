# file lib/ansible/vars/clean.py:98-115
# lines []
# branches ['109->108']

import pytest
from unittest import mock
from ansible.vars.clean import remove_internal_keys

def test_remove_internal_keys_empty_warnings_deprecations():
    data = {
        'warnings': [],
        'deprecations': [],
        '_ansible_parsed': True,
        '_ansible_foo': 'bar',
        'ansible_facts': {
            'discovered_interpreter_python': '/usr/bin/python',
            'ansible_discovered_interpreter_python': '/usr/bin/python3'
        }
    }

    with mock.patch('ansible.vars.clean.display.warning') as mock_warning:
        remove_internal_keys(data)

    assert 'warnings' not in data
    assert 'deprecations' not in data
    assert '_ansible_foo' not in data
    assert 'discovered_interpreter_python' not in data['ansible_facts']
    assert 'ansible_discovered_interpreter_python' not in data['ansible_facts']
    assert '_ansible_parsed' in data

    mock_warning.assert_called_once_with("Removed unexpected internal key in module return: _ansible_foo = bar")

def test_remove_internal_keys_non_empty_warnings_deprecations():
    data = {
        'warnings': ['some warning'],
        'deprecations': ['some deprecation'],
        '_ansible_parsed': True,
        '_ansible_foo': 'bar',
        'ansible_facts': {
            'discovered_interpreter_python': '/usr/bin/python',
            'ansible_discovered_interpreter_python': '/usr/bin/python3'
        }
    }

    with mock.patch('ansible.vars.clean.display.warning') as mock_warning:
        remove_internal_keys(data)

    assert 'warnings' in data
    assert 'deprecations' in data
    assert '_ansible_foo' not in data
    assert 'discovered_interpreter_python' not in data['ansible_facts']
    assert 'ansible_discovered_interpreter_python' not in data['ansible_facts']
    assert '_ansible_parsed' in data

    mock_warning.assert_called_once_with("Removed unexpected internal key in module return: _ansible_foo = bar")
