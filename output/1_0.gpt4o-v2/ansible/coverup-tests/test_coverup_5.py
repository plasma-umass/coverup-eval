# file: lib/ansible/utils/fqcn.py:21-33
# asked: {"lines": [21, 27, 28, 29, 30, 31, 32, 33], "branches": [[28, 29], [28, 33], [30, 28], [30, 31]]}
# gained: {"lines": [21, 27, 28, 29, 30, 31, 32, 33], "branches": [[28, 29], [28, 33], [30, 28], [30, 31]]}

import pytest
from ansible.utils.fqcn import add_internal_fqcns

def test_add_internal_fqcns_with_fqcn():
    names = ['ansible.builtin.command', 'ansible.legacy.copy']
    expected = ['ansible.builtin.command', 'ansible.legacy.copy']
    result = add_internal_fqcns(names)
    assert result == expected

def test_add_internal_fqcns_without_fqcn():
    names = ['command', 'copy']
    expected = [
        'command', 'ansible.builtin.command', 'ansible.legacy.command',
        'copy', 'ansible.builtin.copy', 'ansible.legacy.copy'
    ]
    result = add_internal_fqcns(names)
    assert result == expected

def test_add_internal_fqcns_mixed():
    names = ['ansible.builtin.command', 'copy']
    expected = [
        'ansible.builtin.command',
        'copy', 'ansible.builtin.copy', 'ansible.legacy.copy'
    ]
    result = add_internal_fqcns(names)
    assert result == expected
