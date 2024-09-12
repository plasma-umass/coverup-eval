# file: lib/ansible/config/manager.py:263-274
# asked: {"lines": [263, 265, 266, 267, 269, 270, 271, 272, 273, 274], "branches": [[266, 0], [266, 267], [269, 0], [269, 270], [271, 269], [271, 272], [272, 271], [272, 273], [273, 271], [273, 274]]}
# gained: {"lines": [263, 265, 266, 267, 269, 270, 271, 272, 273, 274], "branches": [[266, 0], [266, 267], [269, 0], [269, 270], [271, 269], [271, 272], [272, 273], [273, 271], [273, 274]]}

import pytest

from ansible.config.manager import _add_base_defs_deprecations

@pytest.fixture
def base_defs():
    return {
        'dummy1': {
            'deprecated': {'some_key': 'some_value'},
            'ini': [{'deprecated': {'some_key': 'some_value'}}],
            'env': [{'deprecated': {'some_key': 'some_value'}}],
            'vars': [{'deprecated': {'some_key': 'some_value'}}]
        },
        'dummy2': {
            'ini': [{'deprecated': {'some_key': 'some_value'}}],
            'env': [{'deprecated': {'some_key': 'some_value'}}],
            'vars': [{'deprecated': {'some_key': 'some_value'}}]
        },
        'dummy3': {
            'ini': [{'some_key': 'some_value'}],
            'env': [{'some_key': 'some_value'}],
            'vars': [{'some_key': 'some_value'}]
        }
    }

def test_add_base_defs_deprecations(base_defs):
    _add_base_defs_deprecations(base_defs)

    assert base_defs['dummy1']['deprecated']['collection_name'] == 'ansible.builtin'
    for section in ('ini', 'env', 'vars'):
        for entry in base_defs['dummy1'][section]:
            assert entry['deprecated']['collection_name'] == 'ansible.builtin'

    for section in ('ini', 'env', 'vars'):
        for entry in base_defs['dummy2'][section]:
            assert entry['deprecated']['collection_name'] == 'ansible.builtin'

    for section in ('ini', 'env', 'vars'):
        for entry in base_defs['dummy3'][section]:
            assert 'collection_name' not in entry.get('deprecated', {})
