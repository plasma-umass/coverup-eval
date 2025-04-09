# file: lib/ansible/vars/clean.py:69-95
# asked: {"lines": [], "branches": [[78, 77], [85, 90]]}
# gained: {"lines": [], "branches": [[78, 77]]}

import pytest
from ansible.errors import AnsibleError
from ansible.vars.clean import strip_internal_keys
from collections.abc import MutableMapping, MutableSequence
import six

def test_strip_internal_keys_with_mutable_sequence(monkeypatch):
    data = [
        {'_ansible_internal': 'value', 'key': 'value'},
        ['_ansible_internal', {'_ansible_internal': 'value', 'key': 'value'}]
    ]
    expected = [
        {'key': 'value'},
        ['_ansible_internal', {'key': 'value'}]
    ]
    result = strip_internal_keys(data)
    assert result == expected

def test_strip_internal_keys_with_exceptions(monkeypatch):
    data = {
        '_ansible_internal': 'value',
        '_ansible_special': 'value',
        'key': 'value'
    }
    exceptions = ('_ansible_special',)
    expected = {
        '_ansible_special': 'value',
        'key': 'value'
    }
    result = strip_internal_keys(data, exceptions=exceptions)
    assert result == expected

def test_strip_internal_keys_with_invalid_type():
    with pytest.raises(AnsibleError, match="Cannot strip invalid keys from <class 'int'>"):
        strip_internal_keys(42)
