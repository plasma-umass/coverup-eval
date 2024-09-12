# file: lib/ansible/config/manager.py:263-274
# asked: {"lines": [263, 265, 266, 267, 269, 270, 271, 272, 273, 274], "branches": [[266, 0], [266, 267], [269, 0], [269, 270], [271, 269], [271, 272], [272, 271], [272, 273], [273, 271], [273, 274]]}
# gained: {"lines": [263, 265, 266, 267, 269, 270, 271, 272, 273, 274], "branches": [[266, 0], [266, 267], [269, 0], [269, 270], [271, 269], [271, 272], [272, 273], [273, 271], [273, 274]]}

import pytest

from ansible.config.manager import _add_base_defs_deprecations

def test_add_base_defs_deprecations():
    base_defs = {
        'dummy1': {
            'deprecated': {},
            'ini': [{'deprecated': {}}],
            'env': [{'deprecated': {}}],
            'vars': [{'deprecated': {}}]
        },
        'dummy2': {
            'ini': [{'deprecated': {}}],
            'env': [{'deprecated': {}}],
            'vars': [{'deprecated': {}}]
        }
    }

    _add_base_defs_deprecations(base_defs)

    assert base_defs['dummy1']['deprecated']['collection_name'] == 'ansible.builtin'
    for section in ('ini', 'env', 'vars'):
        for entry in base_defs['dummy1'][section]:
            assert entry['deprecated']['collection_name'] == 'ansible.builtin'
        for entry in base_defs['dummy2'][section]:
            assert entry['deprecated']['collection_name'] == 'ansible.builtin'
