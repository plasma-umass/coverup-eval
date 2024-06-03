# file lib/ansible/vars/clean.py:98-115
# lines [98, 102, 103, 104, 105, 108, 109, 110, 113, 114, 115]
# branches ['102->103', '102->108', '103->102', '103->104', '108->109', '108->113', '109->108', '109->110', '113->exit', '113->114', '114->113', '114->115']

import pytest
from unittest import mock
from ansible.vars.clean import remove_internal_keys
from ansible.utils.display import Display

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch.object(Display, 'warning')

def test_remove_internal_keys(mock_display_warning):
    data = {
        '_ansible_foo': 'bar',
        '_ansible_parsed': True,
        'warnings': [],
        'deprecations': [],
        'ansible_facts': {
            'discovered_interpreter_python': '/usr/bin/python',
            'ansible_discovered_interpreter_python': '/usr/bin/python3',
            'some_fact': 'value'
        },
        'some_key': 'some_value'
    }

    remove_internal_keys(data)

    # Check that the internal keys were removed
    assert '_ansible_foo' not in data
    assert '_ansible_parsed' in data  # This should not be removed
    assert 'warnings' not in data
    assert 'deprecations' not in data
    assert 'discovered_interpreter_python' not in data['ansible_facts']
    assert 'ansible_discovered_interpreter_python' not in data['ansible_facts']
    assert 'some_fact' in data['ansible_facts']
    assert 'some_key' in data

    # Check that the warning was called for the removed internal key
    mock_display_warning.assert_called_once_with("Removed unexpected internal key in module return: _ansible_foo = bar")
