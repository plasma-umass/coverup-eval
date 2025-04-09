# file: lib/ansible/vars/clean.py:98-115
# asked: {"lines": [102, 103, 104, 105, 108, 109, 110, 113, 114, 115], "branches": [[102, 103], [102, 108], [103, 102], [103, 104], [108, 109], [108, 113], [109, 108], [109, 110], [113, 0], [113, 114], [114, 113], [114, 115]]}
# gained: {"lines": [102, 103, 104, 105, 108, 109, 110, 113, 114, 115], "branches": [[102, 103], [102, 108], [103, 102], [103, 104], [108, 109], [108, 113], [109, 110], [113, 0], [113, 114], [114, 113], [114, 115]]}

import pytest
from unittest.mock import MagicMock, patch

# Mocking ansible.constants and display
@pytest.fixture
def mock_ansible_constants():
    with patch('ansible.constants.INTERNAL_RESULT_KEYS', new=['internal_key1', 'internal_key2']):
        yield

@pytest.fixture
def mock_display():
    with patch('ansible.vars.clean.display') as mock_display:
        yield mock_display

from ansible.vars.clean import remove_internal_keys

def test_remove_internal_keys(mock_ansible_constants, mock_display):
    data = {
        '_ansible_keep': 'value1',
        '_ansible_remove': 'value2',
        '_ansible_parsed': 'value3',
        'internal_key1': 'value4',
        'warnings': [],
        'deprecations': [],
        'ansible_facts': {
            'discovered_interpreter_python': 'value5',
            'ansible_discovered_interpreter_perl': 'value6',
            'keep_fact': 'value7'
        }
    }

    remove_internal_keys(data)

    assert '_ansible_keep' not in data
    assert '_ansible_remove' not in data
    assert '_ansible_parsed' in data
    assert 'internal_key1' not in data
    assert 'warnings' not in data
    assert 'deprecations' not in data
    assert 'discovered_interpreter_python' not in data['ansible_facts']
    assert 'ansible_discovered_interpreter_perl' not in data['ansible_facts']
    assert 'keep_fact' in data['ansible_facts']

    mock_display.warning.assert_any_call("Removed unexpected internal key in module return: _ansible_remove = value2")
    mock_display.warning.assert_any_call("Removed unexpected internal key in module return: internal_key1 = value4")
